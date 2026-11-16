# Santa Monica — Research Completion

The target milestone is `SANTA_MONICA_RESEARCH_V1.0_COMPLETE`. The reference is the installed Vampire: The Masquerade — Bloodlines (2004), Unofficial Patch Plus 12.0. The research supports later Unity 6 development. Implementation remains a separate milestone requiring the owner's approval.

**Acceptance status: `BLOCKED`.** This document records the evidence and the open acceptance checks. It is the active status record for this research.

## Acceptance matrix

| Criterion | Acceptance test | Evidence |
|---|---|---|
| A — Maps | Each of the 22 installed maps has a linked package covering purpose, layout, transitions, important actors and mechanisms, quest links, and version provenance. | 22/22 packages indexed. Verified against the installed BSP and SDK VMF filename sets. [[Santa_Monica_Research_Index]] · [[Locations/Index]] |
| B — Transitions and space | Classify all 65 BSP changelevels with landmark evidence, activation conditions and reachability. Explain and test critical physical routes. | 65/65 classified, 60 landmark pairs, 101 brush/terrain/PHY probes. Conditional geometry is documented for the eastern Beach House landings, the Warehouse west route, and the Ocean House collapse to the breaker. Native movement and remaining seams require playthroughs. [[Space/Transitions]] · [[Space/Santa_Monica_BSP_Changelevels.csv]] · [[Space/Santa_Monica_BSP_Brush_Routes.csv]] · [BSP tracer](../../Research/trace_bsp_brush_route.py) |
| C — Scenario logic | Link prerequisites, player actions, branches, state writes and outcomes for significant chains. | The installed BSP, DLG, Python and journal now link the critical progression, including three Asylum outcomes to Bertram, Warehouse to Downtown, and Luckee Star to the Junkyard gate. Known native results remain in the runtime plan. [[Quests/Index]] |
| D — Game runtime | Test each critical scenario through its intended interactions from a recorded starting state on a disposable copy. Record expectation, observation and outcome. An unrun critical test requires explicit owner acceptance to close. | No end-to-end run is verified. Direct loads exist for Haven and Foxy Boxes. The 17 November console telemetry attempt ended before any intended transition. [[Space/Runtime_Verification]] |
| E — Integrity | Check indices, live links, CSV shape, BSP identity, version conflicts, probe reproducibility and `git diff --check`. Give each remaining unknown a reason and impact. | Active links and both matrices checked. Historical source conflicts and the open native cases are recorded below. [[#Integrity audit]] |

## Open blockers

| Area | Open proof | Current evidence |
|---|---|---|
| Late Haven ↔ Hub 2 | Exercise both doors at the Bloodhunt stage and observe the destination or broken route. | The Hub 2 door starts locked and names the absent `HavenTeleport1`. The installed Python search found no definition for the Haven exit callback `werewolfBloodHavenExit()`. [[Locations/pawnshop1/SM-29_Pawnshop_1_Passport]] |
| Pier ↔ Beach House and Astrolite | Observe the runtime ascent from the gate, the real arrival, the connection from arrival to Brian, item pickup and return. | The elevated-step PHY probe reaches both Pier trigger brushes together at 14 positions. Four translated landings link to Brian and then to Astrolite. The actual activation position and landing are open. [[Space/Surface]] |
| Ocean House | Exercise B7, the key or skill check, the playable interior progression and return with the pendant. | B7 ladder sweep reaches the transition volume. Exterior probes connect B7, the trailer key and the hotel door. Interior probes connect the lobby, left stair collapse and breaker. The powered return to the cabin, upper route and exit still need the game. [[Space/Sewers]] · [[Locations/oceanhouse/SM-20_Ocean_House_00_Index]] |
| Warehouse | Exercise Bertram's actual arrival, connective path, ladder, explosive, timed escape and finale. | The western station, low arch, west ladder and vent form a conditional route to the bomb. The bomb to Beckett yard route reaches a local 64-unit clearance test at *109. Ladder dismount, the escape movement and timed outcome remain open. [[Locations/warehouse/SM-21_Warehouse_00_Index]] |
| Foxy Boxes, Junkyard and quest-gated transitions | Exercise the key gates and report, fight/exit, both Killer resolutions, and normal exit interactions. | [[Space/Runtime_Verification]] |

## Known limitations and exceptions

For installed map behavior, the UP+ 12.0 BSP, installed scripts and actual game observations have priority. Runtime observations and practical route blockers are tracked above. The following isolated uncertainties do not prevent specification of the cited scenarios.

| Uncertainty | Reason and effect on development |
|---|---|
| Legacy VMF provenance | Some reconstructions lack their input BSP. Use the installed BSP for current names, geometry and collisions. Legacy provenance does not block development. |
| Missing `sm_apartment_1b`, `taxi`, `sewer_map` and `sp_soc_3/dane_mark` | Checked BSP and VPK indexes rule out those loose targets or landmark matches. Keep the unproven records and use the separate installed routes or menu handlers. These specific records do not block development of identified paths. The late Haven return remains a separate blocker above. |
| Unnamed special Haven transitions and local Bloodhunt H stub | The BSP disables touch and lacks a found activator. The paired logic in the target maps is separate. Preserve the records as unproven optional links. |
| Clinic orphan output and Tattoo phone mismatch | A second Clinic branch targets the existing warning entity. Tattoo has differing names on a delayed Disable and its Basic trigger. Preserve literal I/O and test the variants. The unresolved engine response does not block specification of the primary chains. |
| Knox 494, `Killer_double`, `Arthur Knox=8` | The sources contain a malformed condition, an unresolved duplicate actor reference and a state beyond the journal definition. Retain those mismatches. They do not block writing the documented quest state graphs. Foxy Boxes and Junkyard gameplay acceptance still requires the runs above. |
| Optional dialogue detail | Individual line referents and cosmetic timings remain unknown when the cited sources lack state effects. [[Quests/Santa_Monica_Discovery]] |

The owner has granted no exception for an unrun critical test.

## Integrity audit

- The installed, SDK, index and CSV map sets contain the same 22 names. Installed BSP SHA-256 values match each matrix. Entity-lump comparison reproduces all 65 transition tuples. SDK differences, base exceptions and absent landmarks are documented with the indices rather than inferred from visual similarity. [[Santa_Monica_Research_Index]] · [[Space/Transitions]]
- All 37 CSV files and 8,729 data rows parsed with unique headers and a consistent field count. The 101 route case IDs are distinct. All 86 prior route cases replayed after the probe options were extended. The 15 additional records were reproduced by the CLI. The Pier replay used VPK extraction and matching MDL/PHY checksums. Reproduce with the parameters from each row and the invocation and decoder examples. [[Space/Index]] · [[Space/Surface]]
- Active Obsidian and relative Markdown references resolved in the filesystem audit after archive collisions were replaced with explicit paths. Archived snapshots retain their historical links and research. `git diff --check` passed. [[../../KNOWLEDGE_BASE_AUDIT|Historical KB audit]]

## Development handover

Use [[Santa_Monica_Research_Index]] to select the package for an individual map, [[Space/Transitions]] for inter-map access and [[Quests/Index]] for cross-map scenario state. Use the open-blocker list above to select the next acceptance run.
