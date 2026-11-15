"""Probe sample routes against installed Bloodlines VBSP v17 brush collision.

Only model 0 and explicitly placed brush submodels participate. Displacements,
model/prop physics, scripted entity state and live movement are outside this probe.
Coordinates, hull dimensions, grid and step thresholds are in Source units.
"""

import argparse
from collections import defaultdict, deque
import hashlib
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


def lift(point, height):
    return point[0], point[1], point[2] + height


def read_models(data):
    if data[:8] != b"VBSP\x11\x00\x00\x00":
        raise ValueError("Expected uncompressed Bloodlines VBSP v17")

    def records(index, fmt):
        offset, size, version, compression = struct.unpack_from("<4I", data, 8 + 16 * index)
        if offset + size > len(data) or version or compression:
            raise ValueError(f"Unsupported lump {index} header")
        return list(struct.iter_unpack(fmt, data[offset:offset + size]))

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
    def __init__(self, data, inline_models):
        self.brushes = []
        self.bins = defaultdict(list)
        self.unbinned = []
        model_brushes = read_models(data)
        for model, position in [(0, (0.0, 0.0, 0.0)), *inline_models]:
            for brush, _, planes in model_brushes(model, WORLD_SOLID_MASK):
                self.add_brush(model, brush, planes, position)

    def add_brush(self, model, brush, planes, position):
        expanded = []
        for x, y, z, distance in planes:
            normal = x, y, z
            nearest = sum(
                n * (lo if n >= 0 else hi)
                for n, lo, hi in zip(normal, HULL_MINS, HULL_MAXS)
            )
            distance += dot(normal, position) - nearest
            expanded.append((normal, distance))
        minimum, maximum = axis_bounds(expanded)
        index = len(self.brushes)
        self.brushes.append(((model, brush), minimum, maximum, expanded))
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
        if not normal or normal[2] < 0.7:
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


def try_step(world, point, x, y, step):
    for rise in (0.0, step):
        upper = lift(point, rise)
        target = x, y, upper[2]
        if rise and world.trace(point, upper)[0] < 1:
            continue
        if world.trace(upper, target)[0] < 1:
            continue
        landing = world.ground(target, step + rise + CLEARANCE)
        if landing is not None:
            return landing
    return None


def find_route(world, start, finish, grid, step, margin, limit):
    start = world.ground(start, 128)
    finish = world.ground(finish, 128)
    if start is None or finish is None:
        return {"status": "ungrounded", "start": start, "finish": finish}
    queue = deque([start])
    key = lambda p: (p[0], p[1], round(p[2], 2))
    parents = {key(start): None}
    terminal = None
    while queue and len(parents) < limit:
        point = queue.popleft()
        x, y, z = point
        if abs(x - finish[0]) <= grid and abs(y - finish[1]) <= grid:
            ending = try_step(world, point, finish[0], finish[1], step)
            if ending and abs(ending[2] - finish[2]) < 0.15:
                terminal = key(ending)
                parents.setdefault(terminal, key(point))
                break
        for dx, dy in ((grid, 0), (-grid, 0), (0, grid), (0, -grid)):
            nx, ny = x + dx, y + dy
            if any(
                value < min(a, b) - margin or value > max(a, b) + margin
                for value, a, b in zip((nx, ny), start, finish)
            ):
                continue
            landing = try_step(world, point, nx, ny, step)
            if landing is not None and key(landing) not in parents:
                parents[key(landing)] = key(point)
                queue.append(landing)
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
    parser.add_argument("--brush-model", nargs=4, action="append", default=[], metavar=("N", "X", "Y", "Z"),
                        help="Include submodel N translated to XYZ, without rotation")
    parser.add_argument("--grid", type=int, default=12)
    parser.add_argument("--step", type=float, default=18)
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
    models = [(int(index), tuple(map(float, xyz))) for index, *xyz in args.brush_model]
    if not all(math.isfinite(value) for value in (*args.start, *args.finish, args.step,
                                                   *(v for _, xyz in models for v in xyz))):
        parser.error("Coordinates and step must be finite")
    world = BrushWorld(data, models)
    result = find_route(world, tuple(args.start), tuple(args.finish),
                        args.grid, args.step, args.margin, args.limit)
    print(json.dumps(result | source | {
        "selected_brushes": len(world.brushes),
        "inline_models": models,
        "hull": [HULL_MINS, HULL_MAXS],
        "grid": args.grid,
        "step": args.step,
        "margin": args.margin,
        "limit": args.limit,
    }, indent=2))


if __name__ == "__main__":
    main()
