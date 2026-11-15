# Knox Quest Research

**Date**: 2026-11-09  
**Status**: VERIFIED_STATIC for the observations below. Runtime selection and event order are UNVERIFIED.  
**Sources**: UP+ 12.0 `Unofficial_Patch/dlg/santa monica/knox.dlg` (974 numbered records, SHA-256 `94c9144670f74d72fe3a9402cc77be4d3f968b946c05806fe5646d733983a794`) and `Unofficial_Patch/python/santamonica/santamonica.py` (SHA-256 `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff`). Map evidence uses SDK `SDKContent/MapSrc/up sources/` and the installed `Unofficial_Patch/maps/` BSP entity lumps.

## Quest Variables

`G.Knox_Quest` and `G.Knox_Done` are globals. `Knox Asian` (The Hunted Hunter) and `Arthur Knox` (A Bounty For The Hunter, about Carson) are separate journal entries in `Unofficial_Patch/vdata/system/quests_santamonica.txt` (lines 137–214 and 35–88 respectively, SHA-256 `d1f4cc18f44d4f231d0764a1d49da314fe4fb383ca70cddae8ef23db28b02f38`).

Other globals catalogued for follow-up are `Knox_TT`, `Knox_Vamp`, `Knox_Ghoul`, `Knox_Master`, `Knox_Likes`, `Knox_Bertram`, `Knox_Outbound`, `Knox_Powerful`, `Knox_Appear`, `Knox_Questions`, `Knox_Arthur`, `Knox_Artbound`, `Trip_Know` and `Knox_Knowledge`. Their complete ranges and runtime meanings are UNVERIFIED.

### Quest Progression

| `knox.dlg` ID | Literal next | VERIFIED_STATIC fields |
|---|---|---|
| 211 | `#` | Bertram surveillance account. `npc.SetDisposition("Neutral",1)` and `G.Knox_Quest = 1`. |
| 231 | `#` | Knox describes the threat. `npc.SetDisposition("Neutral",1)`, `G.Knox_Quest = 2` and `G.Knox_Questions = 1`. |
| 263 | Empty | Numbered row with empty payload. |
| 266 | `#` | `npc.SetDisposition("Neutral",1)` and `pc.GiveItem("item_g_driver_license_gimble")`. No stage write on this row. |
| 267 | 281 | `G.VirgilCrumbKnowledge == 0`. Writes `G.Knox_Quest = 5` and `pc.SetQuest("Knox Asian", 1)`. |
| 268 | 281 | `G.VirgilCrumbKnowledge == 1`. Writes `G.Knox_Quest = 5` and `pc.SetQuest("Knox Asian", 10)`. |
| 271 | `#` | Refusal response. `npc.SetDisposition("Sad",2)` and `G.Knox_Quest = 4`. |
| 381 | `#` | Report of success. `npc.SetDisposition("Joy",2)`, `G.Knox_Quest = 7`, `G.Knox_Done = 1` and `pc.SetQuest("Knox Asian", 4)`. |

`vdata/hackterminals/krime_computer.txt:68` contains `runscript → virgilViewed()`. `santamonica.py:412–417` writes `G.VirgilCrumbKnowledge = 1` and sets `Knox Asian` to 9 when the prior journal state is 1, 2 or 5. Journal states 1 and 10 describe the accepted assignment with different prior knowledge of Virgil Crumb.

## VMF and BSP Source Analysis

| Map | VERIFIED_STATIC SDK VMF / installed BSP output | VERIFIED_STATIC Python effect |
|---|---|---|
| `sm_hub_1` | `sm_hub_1_d.vmf:153175` and BSP entity `Knox` have `OnDeath → knoxDead()`. `logic_auto.OnMapLoad → knoxState()` is present in VMF L151246 and BSP. | `santamonica.py:2038–2041` sets `Knox Asian` to 8 if the previous state is neither 0 nor 4. L2044–2057 contains the Nosferatu teleport/trigger changes and conditional `Knox.Kill()`. |
| `sm_bailbonds_1` | `sm_bailbonds_1_d.vmf:5081` and BSP entity `Arthur` have `OnDeath → kilpatrickDeath()`. | L391–398 sets `Arthur Knox` to 7 if its state is neither 0 nor 5, and `Bail Jumper` to 5 if its state is outside 0/3/4. |
| `sm_vamparena` | `sm_vamparena.vmf:13192,13253` and BSP entities `AsianVamp` / `AsianVamp_plus` have `OnDeath → asianVampDeath()`. These are two placed outputs per checked map representation. | L142–144 writes `G.Kjspy_Dead = 1` and `Knox Asian` stage 3. L145–160 adds an item-spawn branch conditional on `G.Patch_Plus == 2`. |
| `sm_basement_1` | `sm_basement_1.vmf:16753–16756` identifies `Stan_Gimble` as entity ID 994. L50460–50462 independently uses ID 994 for a brush side. VMF L16816–16817 and the BSP entity `Stan_Gimble` contain both outputs below. | L429–431 sets `Arthur Knox` to 3 and `G.Gimble_Dead = 1`. |

### Gimble Death Flow

`Stan_Gimble.OnDeath` has two sibling outputs, `gimble_dead_relay.Trigger` and `gimbleDeath()`. The relay configures doors, fade, player teleport and the Carson release sequence (`sm_basement_1.vmf:23158–23172`). The Python call is a separate output on `Stan_Gimble`. See [[../Locations/basement1/SM-18_Basement_02_Systems|SM-18 systems]] for the detailed I/O graph.

**UNVERIFIED**: actual dispatch order of sibling outputs, whether scripted `Kill` dispatches the corresponding `OnDeath` in a given route, dialogue-entry priority, and which arena NPC appears in each runtime state. Historical default/UP entity dumps in the old audit are additional representations. Their provenance and correspondence to the installed BSP remain UNVERIFIED.
