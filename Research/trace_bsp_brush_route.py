"""Probe sample routes against installed Bloodlines VBSP v17 brush collision.

By default only model 0 brushes and explicitly placed brush submodels participate.
Optional displacement triangles are treated as two-sided surfaces. Selected
props can use decoded convex PHY sections. Scripted state and live movement
are outside this probe.
Coordinates, hull dimensions, grid and step thresholds are in Source units.
"""

import argparse
from collections import Counter, defaultdict
import hashlib
import heapq
import itertools
import json
import math
from pathlib import Path
import struct


WORLD_SOLID_MASK = 0x1000B  # solid, window, grate, playerclip
LADDER_MASK = 0x20000000
HULL_MINS = (-16.0, -16.0, 0.0)
HULL_MAXS = (16.0, 16.0, 72.0)
CLEARANCE = 0.05
BIN_SIZE = 128
AXES = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def lift(point, height):
    return point[0], point[1], point[2] + height


def bsp_records(data):
    if data[:8] != b"VBSP\x11\x00\x00\x00":
        raise ValueError("Expected uncompressed Bloodlines VBSP v17")

    def records(index, fmt):
        offset, size, version, compression = struct.unpack_from("<4I", data, 8 + 16 * index)
        if offset + size > len(data) or version or compression:
            raise ValueError(f"Unsupported lump {index} header")
        return list(struct.iter_unpack(fmt, data[offset:offset + size]))

    return records


def read_models(data):
    records = bsp_records(data)
    planes = records(1, "<4fi")
    nodes = records(5, "<3i6h2Hh2x")
    leaves = records(10, "<ihH6h4Hh2x")
    models = records(14, "<9f3i")
    leaf_brushes = [i for i, in records(17, "<H")]
    brushes = records(18, "<iiI")
    sides = records(19, "<H3h")

    def model_brushes(model_index, mask):
        if not 0 <= model_index < len(models):
            raise ValueError(f"Unknown model *{model_index}")
        pending = [models[model_index][9]]
        visited = set()
        indices = set()
        while pending:
            node = pending.pop()
            if node in visited:
                continue
            visited.add(node)
            if node >= 0:
                pending.extend(nodes[node][1:3])
                continue
            first, count = leaves[-node - 1][11:13]
            if count and first + count > len(leaf_brushes):
                raise ValueError("Invalid leafbrush span")
            indices.update(leaf_brushes[first:first + count])
        for brush_id in sorted(indices):
            first, count, contents = brushes[brush_id]
            if not contents & mask:
                continue
            if first < 0 or count <= 0 or first + count > len(sides):
                raise ValueError(f"Invalid brush {brush_id} sides")
            yield brush_id, contents, [planes[side[0]][:4] for side in sides[first:first + count]]

    return model_brushes


def read_displacement_triangles(data):
    records = bsp_records(data)
    infos = records(26, "<3f4ifiH2x2i128x")
    if not infos:
        return
    vertices = records(3, "<3f")
    faces = records(7, "<32BHBBi4h24bif5iI")
    edges = records(12, "<2H")
    surfedges = [edge for edge, in records(13, "<i")]
    fields = records(33, "<5f")
    tags = [tag for tag, in records(48, "<H")]
    first_face, face_count = records(14, "<9f3i")[0][-2:]
    for face_id in range(first_face, first_face + face_count):
        start, length, _, disp_id = faces[face_id][35:39]
        if disp_id < 0:
            continue
        info = infos[disp_id]
        vert_start, tri_start, power = info[3:6]
        if not info[8] & WORLD_SOLID_MASK:
            continue
        if (
            length != 4 or power not in (2, 3, 4) or face_id != info[9]
            or not 0 <= start <= len(surfedges) - length
        ):
            raise ValueError(f"Invalid displacement face {face_id}")
        n = (1 << power) + 1
        vertex_count = n * n
        triangle_count = 2 * (n - 1) ** 2
        if not (
            0 <= vert_start <= len(fields) - vertex_count
            and 0 <= tri_start <= len(tags) - triangle_count
        ):
            raise ValueError(f"Invalid displacement {disp_id} data range")
        corners = [vertices[edges[abs(edge)][edge < 0]] for edge in surfedges[start:start + length]]
        matches = [i for i, point in enumerate(corners) if math.dist(point, info[:3]) <= 0.1]
        if len(matches) != 1:
            raise ValueError(f"Displacement {disp_id} has no unique start corner")
        first = matches[0]
        corners = corners[first:] + corners[:first]
        grid = []
        for row in range(n):
            t = row / (n - 1)
            for col in range(n):
                s = col / (n - 1)
                field = fields[vert_start + row*n + col]
                grid.append(tuple(
                    ((1-t)*corners[0][axis] + t*corners[1][axis]) * (1-s)
                    + ((1-t)*corners[3][axis] + t*corners[2][axis]) * s
                    + field[axis] * field[3]
                    for axis in range(3)
                ))
        for row in range(n - 1):
            for col in range(n - 1):
                i = row*n + col
                triangles = ((i, i+n, i+1), (i+1, i+n, i+n+1)) if i % 2 else (
                    (i, i+n, i+n+1), (i, i+n+1, i+1)
                )
                for j, triangle in enumerate(triangles):
                    index = 2*(row*(n-1) + col) + j
                    if not tags[tri_start + index] & 0x20:  # DISPTRI_TAG_REMOVE
                        yield (disp_id, index), tuple(grid[v] for v in triangle)


def triangle_planes(triangle):
    """Finite SAT axes for a fixed-orientation AABB against a triangle."""
    sides = [
        tuple(b - a for a, b in zip(triangle[i], triangle[(i + 1) % 3]))
        for i in range(3)
    ]
    normal = cross(sides[0], sides[1])
    if dot(normal, normal) <= 1e-16:
        return
    yield from projection_planes(triangle, [normal], sides)


def projection_planes(vertices, normals, edges):
    axes = [*AXES, *normals, *(cross(a, edge) for a in AXES for edge in edges)]
    seen = set()
    for axis in axes:
        length = math.sqrt(dot(axis, axis))
        if length <= 1e-8:
            continue
        n = tuple(c / length for c in axis)
        if next(c for c in n if abs(c) > 1e-8) < 0:
            n = tuple(-c for c in n)
        if n in seen:
            continue
        seen.add(n)
        projected = [dot(n, vertex) for vertex in vertices]
        yield (*n, max(projected))
        yield (*(-c for c in n), -min(projected))


def add_physics_props(world, decoded, placements):
    registry = {entry["path"].lower(): entry for entry in decoded}
    for i, (name, origin, yaw) in enumerate(placements):
        source = registry.get(name.lower())
        if not source or source["status"] != "decoded" or not source["pieces"]:
            raise ValueError(f"No decoded physics for {name}")
        sine, cosine = math.sin(math.radians(yaw)), math.cos(math.radians(yaw))
        for piece_index, piece in enumerate(source["pieces"]):
            if piece["bone"] != 0:
                raise ValueError(f"Unsupported non-root physics bone in {name}")
            raw_vertices = piece["vertices"]
            if len(raw_vertices) % 3 or not all(math.isfinite(v) for v in raw_vertices):
                raise ValueError(f"Invalid physics vertices in {name}")
            local_points = [raw_vertices[i:i + 3] for i in range(0, len(raw_vertices), 3)]
            vertices = [
                ((cosine*x - sine*z) / 0.0254, (sine*x + cosine*z) / 0.0254, -y / 0.0254)
                for x, y, z in local_points
            ]
            faces = [face["indices"] for face in piece["faces"]]
            if any(len(face) != 3 or any(k < 0 or k >= len(vertices) for k in face) for face in faces):
                raise ValueError(f"Invalid physics faces in {name}")
            edges = Counter(
                tuple(sorted((a, b)))
                for face in faces
                for a, b in zip(face, face[1:] + face[:1])
            )
            volume = sum(dot(vertices[a], cross(vertices[b], vertices[c])) for a, b, c in faces)
            if not edges or any(count != 2 for count in edges.values()) or abs(volume) < 1e-6:
                raise ValueError(f"Open or degenerate physics piece in {name}")
            edge_vectors = [tuple(y-x for x, y in zip(vertices[a], vertices[b])) for a, b in edges]
            normals = [
                cross(
                    tuple(y-x for x, y in zip(vertices[a], vertices[b])),
                    tuple(y-x for x, y in zip(vertices[a], vertices[c])),
                )
                for a, b, c in faces
            ]
            world.add_shape(("physics", i, piece_index), projection_planes(vertices, normals, edge_vectors), origin)


def bins(x0, y0, x1, y1):
    return itertools.product(
        range(math.floor(min(x0, x1) / BIN_SIZE), math.floor(max(x0, x1) / BIN_SIZE) + 1),
        range(math.floor(min(y0, y1) / BIN_SIZE), math.floor(max(y0, y1) / BIN_SIZE) + 1),
    )


def axis_bounds(planes):
    minimum = [-math.inf] * 3
    maximum = [math.inf] * 3
    for normal, distance in planes:
        for axis, positive in enumerate(AXES):
            if normal == positive:
                maximum[axis] = min(maximum[axis], distance)
            if normal == tuple(-value for value in positive):
                minimum[axis] = max(minimum[axis], -distance)
    return minimum, maximum


class BrushWorld:
    def __init__(self, data, inline_models, terrain=False, minimum_ground_normal=0.7,
                 hull_height=None):
        self.brushes = []
        self.bins = defaultdict(list)
        self.unbinned = []
        self.minimum_ground_normal = minimum_ground_normal
        self.hull_maxs = HULL_MAXS if hull_height is None else (*HULL_MAXS[:2], hull_height)
        model_brushes = read_models(data)
        for model, position in [(0, (0.0, 0.0, 0.0)), *inline_models]:
            for brush, _, planes in model_brushes(model, WORLD_SOLID_MASK):
                self.add_shape((model, brush), planes, position)
        self.brush_count = len(self.brushes)
        if terrain:
            for key, triangle in read_displacement_triangles(data):
                planes = list(triangle_planes(triangle))
                if planes:
                    self.add_shape(("displacement", *key), planes, (0.0, 0.0, 0.0))
        self.terrain_count = len(self.brushes) - self.brush_count

    def add_shape(self, shape, planes, position):
        expanded = []
        for x, y, z, distance in planes:
            normal = x, y, z
            nearest = sum(
                n * (lo if n >= 0 else hi)
                for n, lo, hi in zip(normal, HULL_MINS, self.hull_maxs)
            )
            distance += dot(normal, position) - nearest
            expanded.append((normal, distance))
        minimum, maximum = axis_bounds(expanded)
        index = len(self.brushes)
        self.brushes.append((shape, minimum, maximum, expanded))
        x0, y0 = minimum[:2]
        x1, y1 = maximum[:2]
        if not all(math.isfinite(value) for value in (x0, y0, x1, y1)):
            self.unbinned.append(index)
            return
        for key in bins(x0, y0, x1, y1):
            self.bins[key].append(index)

    def trace(self, start, end):
        candidates = set(self.unbinned)
        for key in bins(start[0], start[1], end[0], end[1]):
            candidates.update(self.bins.get(key, ()))
        earliest = (1.0, None, None)
        for i in sorted(candidates):
            brush, minimum, maximum, planes = self.brushes[i]
            if any(
                max(a, b) <= lo or min(a, b) >= hi
                for a, b, lo, hi in zip(start, end, minimum, maximum)
            ):
                continue
            fraction, normal = clip_segment(start, end, planes)
            if fraction < earliest[0]:
                earliest = fraction, normal, brush
                if fraction == 0:
                    break
        return earliest

    def ground(self, point, maximum_drop):
        end = lift(point, -maximum_drop)
        fraction, normal, _ = self.trace(point, end)
        if not normal or normal[2] < self.minimum_ground_normal:
            return None
        return lift(point, -fraction * maximum_drop + CLEARANCE)


def clip_segment(start, end, planes):
    """Return entry fraction and normal, or 1 for no overlap."""
    enter, leave, hit = 0.0, 1.0, None
    for normal, distance in planes:
        before = dot(normal, start) - distance
        after = dot(normal, end) - distance
        if before >= 0 and after >= 0:
            return 1.0, None
        if before < 0 and after < 0:
            continue
        fraction = before / (before - after)
        if before >= 0 and fraction >= enter:
            enter, hit = fraction, normal
        elif before < 0:
            leave = min(leave, fraction)
        if enter >= leave:
            return 1.0, None
    return enter, hit


def try_step(world, point, x, y, step, *, rises=None, max_drop=None):
    if rises is None:
        rises = (0.0, step)
    if max_drop is None:
        max_drop = step
    for rise in rises:
        upper = lift(point, rise)
        target = x, y, upper[2]
        if rise and world.trace(point, upper)[0] < 1:
            continue
        if world.trace(upper, target)[0] < 1:
            continue
        landing = world.ground(target, max_drop + rise + CLEARANCE)
        if landing is not None:
            return landing
    return None


def find_route(world, start, finish, grid, step, margin, limit, goal_directed=False,
               *, diagonal=False, rise_increment=None, max_drop=None, bounds=None):
    start = world.ground(start, 128)
    finish = world.ground(finish, 128)
    if start is None or finish is None:
        return {"status": "ungrounded", "start": start, "finish": finish}
    queue = [(0.0, 0, start)]
    order = itertools.count(1)
    def key(point):
        if diagonal:
            return tuple(round(value, 3) for value in point)
        return point[0], point[1], round(point[2], 2)

    if bounds is None:
        bounds = (min(start[0], finish[0]) - margin, max(start[0], finish[0]) + margin,
                  min(start[1], finish[1]) - margin, max(start[1], finish[1]) + margin)
    min_x, max_x, min_y, max_y = bounds
    directions = ((grid, 0), (-grid, 0), (0, grid), (0, -grid))
    if diagonal:
        directions += ((grid, grid), (grid, -grid), (-grid, grid), (-grid, -grid))
    rises = None
    if rise_increment is not None:
        rises = (*range(0, math.ceil(step), rise_increment), step)

    parents = {key(start): None}
    terminal = None
    while queue and len(parents) < limit:
        _, _, point = heapq.heappop(queue)
        x, y, z = point
        if abs(x - finish[0]) <= grid and abs(y - finish[1]) <= grid:
            ending = try_step(world, point, finish[0], finish[1], step,
                              rises=rises, max_drop=max_drop)
            if ending and abs(ending[2] - finish[2]) < 0.15:
                terminal = key(ending)
                parents.setdefault(terminal, key(point))
                break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (min_x <= nx <= max_x and min_y <= ny <= max_y):
                continue
            landing = try_step(world, point, nx, ny, step, rises=rises, max_drop=max_drop)
            if landing is not None and key(landing) not in parents:
                parents[key(landing)] = key(point)
                priority = 0.0
                if goal_directed:
                    priority = math.dist(landing, finish) if diagonal else sum(
                        abs(a - b) for a, b in zip(landing, finish))
                heapq.heappush(queue, (priority, next(order), landing))
    path = []
    while terminal is not None:
        path.append(terminal)
        terminal = parents[terminal]
    return {
        "status": "route_found" if path else ("limit" if queue else "no_route_in_sample"),
        "start": start,
        "finish": finish,
        "visited": len(parents),
        "path": path[::-1],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bsp", type=Path)
    parser.add_argument("--start", nargs=3, type=float, metavar=("X", "Y", "Z"))
    parser.add_argument("--finish", nargs=3, type=float, metavar=("X", "Y", "Z"))
    parser.add_argument("--ladder-bounds", action="store_true", help="List static world ladder brush bounds")
    parser.add_argument("--terrain", action="store_true", help="Also trace compiled displacement triangles")
    parser.add_argument("--goal-directed", action="store_true", help="Visit positions closest to the finish first")
    parser.add_argument("--minimum-ground-normal", type=float, default=0.7,
                        help="Minimum Z component of a contact normal treated as support")
    parser.add_argument("--decoded-physics", type=Path, help="Decoded SDK PHY sections in JSON")
    parser.add_argument("--physics-prop", nargs=5, action="append", default=[],
                        metavar=("MDL_PATH", "X", "Y", "Z", "YAW"),
                        help="Place a decoded convex model with an independently verified identity root bone")
    parser.add_argument("--brush-model", nargs=4, action="append", default=[], metavar=("N", "X", "Y", "Z"),
                        help="Include submodel N translated to XYZ, without rotation")
    parser.add_argument("--grid", type=int, default=12)
    parser.add_argument("--step", type=float, default=18)
    parser.add_argument("--hull-height", type=float, help="Height of the 32-unit-wide hull")
    parser.add_argument("--rise-increment", type=int, help="Test intermediate rises up to --step")
    parser.add_argument("--max-drop", type=float, help="Use a separate drop limit in Source units")
    parser.add_argument("--diagonal", action="store_true",
                        help="Trace diagonal neighbors and use Euclidean goal distance")
    parser.add_argument("--bounds", nargs=4, type=float, metavar=("X_MIN", "X_MAX", "Y_MIN", "Y_MAX"),
                        help="Search limits in XY; overrides --margin")
    parser.add_argument("--margin", type=int, default=96)
    parser.add_argument("--limit", type=int, default=40000)
    args = parser.parse_args()
    data = args.bsp.read_bytes()
    source = {"bsp": args.bsp.name, "sha256": hashlib.sha256(data).hexdigest()}
    if args.ladder_bounds:
        model_brushes = read_models(data)
        ladders = []
        for brush, contents, planes in model_brushes(0, LADDER_MASK):
            bounds = axis_bounds([((x, y, z), distance) for x, y, z, distance in planes])
            ladders.append({
                "brush": brush,
                "contents": hex(contents),
                "bounds": [[v if math.isfinite(v) else None for v in side] for side in bounds],
            })
        print(json.dumps(source | {"ladders": ladders}, indent=2))
        return
    if args.start is None or args.finish is None:
        parser.error("Provide both --start and --finish for a route probe")
    if args.grid <= 0 or args.step <= 0 or args.margin < 0 or args.limit <= 0:
        parser.error("Grid, step and limit must be positive, and margin nonnegative")
    if args.hull_height is not None and not (math.isfinite(args.hull_height) and args.hull_height > 0):
        parser.error("Hull height must be positive and finite")
    if args.rise_increment is not None and args.rise_increment <= 0:
        parser.error("Rise increment must be positive")
    if args.max_drop is not None and not (math.isfinite(args.max_drop) and args.max_drop >= 0):
        parser.error("Drop limit must be nonnegative and finite")
    if args.bounds is not None:
        min_x, max_x, min_y, max_y = args.bounds
        if not all(map(math.isfinite, args.bounds)) or min_x > max_x or min_y > max_y:
            parser.error("Search bounds must be finite and ordered")
        for x, y, _ in (args.start, args.finish):
            if not (min_x <= x <= max_x and min_y <= y <= max_y):
                parser.error("Start and finish must lie inside the search bounds")
    if not 0 < args.minimum_ground_normal <= 1:
        parser.error("Minimum ground normal must be in (0, 1]")
    models = [(int(index), tuple(map(float, xyz))) for index, *xyz in args.brush_model]
    props = [(name, tuple(map(float, xyz)), float(yaw)) for name, *xyz, yaw in args.physics_prop]
    if bool(props) != bool(args.decoded_physics):
        parser.error("Physics props and decoded physics must be provided together")
    if not all(math.isfinite(value) for value in (*args.start, *args.finish, args.step,
                                                   *(v for _, xyz in models for v in xyz),
                                                   *(v for _, xyz, yaw in props for v in (*xyz, yaw)))):
        parser.error("Coordinates and step must be finite")
    world = BrushWorld(data, models, terrain=args.terrain, minimum_ground_normal=args.minimum_ground_normal,
                       hull_height=args.hull_height)
    if props:
        add_physics_props(world, json.loads(args.decoded_physics.read_text(encoding="utf-8-sig")), props)
    result = find_route(world, tuple(args.start), tuple(args.finish),
                        args.grid, args.step, args.margin, args.limit, args.goal_directed,
                        diagonal=args.diagonal, rise_increment=args.rise_increment,
                        max_drop=args.max_drop, bounds=args.bounds)
    print(json.dumps(result | source | {
        "selected_brushes": world.brush_count,
        "displacement_triangles": world.terrain_count,
        "physics_props": props,
        "physics_pieces": len(world.brushes) - world.brush_count - world.terrain_count,
        "inline_models": models,
        "hull": [HULL_MINS, world.hull_maxs],
        "grid": args.grid,
        "step": args.step,
        "margin": args.margin,
        "limit": args.limit,
        "goal_directed": args.goal_directed,
        "minimum_ground_normal": args.minimum_ground_normal,
        "diagonal": args.diagonal,
        "rise_increment": args.rise_increment,
        "max_drop": args.max_drop,
        "bounds": args.bounds,
    }, indent=2))


if __name__ == "__main__":
    main()
