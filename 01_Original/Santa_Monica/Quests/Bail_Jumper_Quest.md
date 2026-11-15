# Arthur Kilpatrick - Bounty Hunter Dialogue States

**Status**: VERIFIED_STATIC for the listed source evidence. Runtime reachability is UNVERIFIED.  
**Sources**: UP+ 12.0 `Unofficial_Patch/dlg/santa monica/arthur.dlg`, SHA-256 `06d552f31c1f171dc46d1ab37061f7b0c8d33f3424603b11333a869e4ed62b2f`, and `Unofficial_Patch/vdata/system/quests_santamonica.txt`, SHA-256 `d1f4cc18f44d4f231d0764a1d49da314fe4fb383ca70cddae8ef23db28b02f38`.  
**NPC**: Arthur Kilpatrick (Bail Bonds)  
**Dialogue variable**: `G.Arthur_BJ`

## Quest Overview

The journal defines `Bail Jumper` (Jumpin' The Bail) at `quests_santamonica.txt:94–131`. The assignment is to find a clue to Mike “Muddy” Durbin's whereabouts. `G.Arthur_BJ` and related globals gate dialogue options. Journal progress is written separately by `pc.SetQuest("Bail Jumper", ...)`.

## Dialogue Evidence

| `arthur.dlg` ID | Literal next | Condition | Action |
|---|---|---|---|
| 35 | 81 | `G.Arthur_BJ == 1 and G.Extra_Lines == 1` | Empty. |
| 62 | 591 | `G.Arthur_BJ == 0 and G.Arthur_BH == 0 and IsClan(pc,"Malkavian")` | Empty. |
| 63 | 71 | `G.Arthur_BJ == 1 and G.Arthur_BH == 0 and not IsClan(pc,"Malkavian")` | Empty. |
| 64 | 81 | `G.Arthur_BJ == 1 and G.Arthur_BH >= 1` | Empty. |
| 65 | 181 | `G.Arthur_BJ == 1 and G.Arthur_BH == 0` | Empty. |
| 66 | 721 | `G.Arthur_BJ == 1 and G.Arthur_BH >= 1 and G.Arthur_Knox < 2` | `G.Arthur_Asked = 1`. |
| 70 | 0 | `G.Arthur_BJ == 1 and G.Arthur_BH >= 1 and G.Arthur_Knox == 2` | Empty. |
| 235 | 551 | `G.Arthur_BJ == 0` | Empty. |
| 236 | 81 | `G.Arthur_BJ == 1 and G.Arthur_BH == 0` | Empty. |
| 237 | 721 | `G.Arthur_BJ == 1 and G.Arthur_BH >= 1 and G.Arthur_Knox == 0` | `G.Player_Asked = 1`. |
| 239 | 81 | `G.Arthur_BJ == 1 and G.Arthur_BH >= 1 and G.Arthur_Knox >= 1` | Empty. |

ID 41 contains `G.Arthur_BJ = 1` in field 5 alongside a disposition expression. ID 741 writes `G.Arthur_BJ = 1; G.Arthur_BH = 2` in field 6. IDs 242→991 and 243→261 concern Carson's fate, with `G.Extra_Lines == 1` on 243. The Plus introduction start is ID 1012 → 2. See [[Arthur's_Introduction]] for its condition and alternatives.

## Journal Progression

| Journal ID | VERIFIED_STATIC writer | Evidence |
|---|---|---|
| 1 | `arthur.dlg:331` | Arthur gives the Durbin assignment and sets `G.Arthur_Muddy = 2`. |
| 2 | `santamonica.py:1420–1425`, `updateBailJumperQuest()` | If `G.Muddy_Message == 0`, writes stage 2, `G.Muddy_Message = 1` and `G.SK_Downtown = 1`. Journal XP key `Bail01`. |
| 3 | `arthur.dlg:361` | Report back to Arthur. Writes `G.Arthur_Muddy = 4` and stage 3. Journal success with XP key `Bail02`. ID 325 has a literal reference to 361 when `G.Muddy_Message == 1`. |
| 4 | `arthur.dlg:532–533` | Failure state write when `pc.GetQuestState("Bail Jumper") < 3`. |
| 5 | `santamonica.py:396–398`, `kilpatrickDeath()` | Failure state write if the prior state is outside 0/3/4. Arthur's `OnDeath` calls the function in SDK `sm_bailbonds_1_d.vmf:5081` and installed `sm_bailbonds_1.bsp`. |

`SDKContent/MapSrc/up sources/sm_pawnshop_1_d.vmf:80665–80666` and the installed `Unofficial_Patch/maps/sm_pawnshop_1.bsp` entity lump contain two `OnPressed` outputs for the message. One plays `muddy_message_sound`. The other calls `updateBailJumperQuest()` with delay 20 and fire count 1. The Python source is `Unofficial_Patch/python/santamonica/santamonica.py`, SHA-256 `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff`.

## Unknowns

- **UNVERIFIED**: dialogue entry priority, reachability of particular responses, exact awarded XP and runtime ordering of terminal/button and dialogue events.
- **INFERRED**: the globals gate conversation branches. Conditions such as `G.Arthur_Knox == 0` have no demonstrated relationship or neutralization meaning. Related context is in [[Bail_Hustler_Quest]] and [[Knox_Quest]].
