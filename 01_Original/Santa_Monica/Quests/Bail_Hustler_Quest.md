# Arthur Kilpatrick - Business Dialogue States

**Status**: VERIFIED_STATIC for the listed fields.  
**Source**: UP+ 12.0 `Unofficial_Patch/dlg/santa monica/arthur.dlg`, SHA-256 `06d552f31c1f171dc46d1ab37061f7b0c8d33f3424603b11333a869e4ed62b2f`.  
**NPC**: Arthur Kilpatrick (Bail Bonds)  
**Dialogue variable**: `G.Arthur_BH`

## Overview

This document tracks the business and bounty-hunter dialogue gates. The `Bail Jumper` and `Arthur Knox` journal entries use `pc.SetQuest(...)` and have separate definitions in `Unofficial_Patch/vdata/system/quests_santamonica.txt:35–88,94–131` (SHA-256 `d1f4cc18f44d4f231d0764a1d49da314fe4fb383ca70cddae8ef23db28b02f38`). No entry named `Bail Hustler` occurs in that file.

## Evidence

| `arthur.dlg` ID | Literal next | Condition | Action / text |
|---|---|---|---|
| 34 | 181 | `G.Arthur_BH == 0 and G.Arthur_Knox < 1` | Empty action. Bounty-hunter work question. |
| 43 | 71 | `G.Arthur_BH == 0` | Empty action. Bail-jumper frequency question. |
| 73 | 671 | `G.Arthur_BH >= 1 and G.Arthur_Knox < 1` | Empty action. Bounty-hunter question. |
| 554 | 671 | `G.Arthur_BH >= 1 and G.Arthur_Knox < 1` | Empty action. Another bounty-hunter question. |
| 122, 602, 702 | Empty | Empty | Numbered rows with empty payloads. |
| 181, 711 | `#` | Disposition expressions in field 5 | `G.Arthur_BH = 1`. |
| 671 | `#` | `npc.SetDisposition("Neutral",1)` | Names Carson and writes `G.Arthur_BH = 2`. |
| 741 | `#` | `npc.SetDisposition("Anger",1)` | Writes `G.Arthur_BJ = 1; G.Arthur_BH = 2`. |

The additional variants for IDs 34 and 43 occupy field 13. The listed numeric targets establish literal references. Runtime eligibility and selection are UNVERIFIED.

## Variable Status

- **VERIFIED_STATIC**: `G.Arthur_BH` is checked and written by the records above. ID 554 references ID 671, where the `BH = 2` write occurs.
- **INFERRED**: `G.Arthur_BH` tracks conversation progress on Arthur's business and Carson. The full runtime semantics of `G.Arthur_BH` and `G.Arthur_Knox` are UNVERIFIED.
- Related evidence: [[Arthur's_Introduction]], [[Bail_Jumper_Quest]] and [[Knox_Quest]].
