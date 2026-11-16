# Thin Bloods on the Pier: Copper and Lily

Static findings from the installed Unofficial Patch 12.0 Plus files. The NPC and relay records below were read from the installed `Unofficial_Patch/maps/sm_pier_1.bsp` entity lump (BSP v17, entity lump 13,784,988–14,036,721); this establishes entity presence and I/O declarations, not runtime spawning, dialogue reachability, or successful gameplay.

Related location/system notes: [[../Locations/diner1/SM-15_Diner_02_Systems|Diner]], [[../Locations/medical1/SM-14_Medical_03_Quests|Clinic]], [[../Space/Surface|Santa Monica surface and Pier]]. Dialogue tests such as `Persuasion 3` and `Humanity 6` are engine-evaluated DLG conditions; the tables report the condition text and scripted action, not a runtime result.

## Installed Pier entities

| BSP entity | Verified fields | Meaning / limit |
|---|---|---|
| `Copper` | `npc_VVampire`; `dlg/Santa Monica/Copper.dlg`; `OnDialogEnd=copperDialog()`; `OnDeath=copperDeath()`; origin `3002.75 -1205 -618` | Copper is placed in `sm_pier_1`; script callbacks are declared. |
| `E` | `npc_VVampire`; `dlg/Santa Monica/E.dlg`; `OnDialogEnd=eAtOceanEdge()`; `OnDeath=eDeath()`; origin `2857 -1395.75 -606` | E is placed in the same BSP and has a death callback. |
| `Lily` | `npc_VVampire`; `dlg/Santa Monica/Lily.dlg`; origin `2854 -1320.35 -606` | Lily is placed in the same BSP. |
| `thinblood_killer` | enabled `logic_relay`; trigger I/O unhides then kills Lily, kills Rosa, Copper, and E | Script calls this relay at the late-story cutoff. The relay's literal I/O also names NPCs not covered in this note. |

## Copper — Plus quest “Daydream Believer”

Quest title is `Copper`, display name `Daydream Believer`. Its states and XP awards are defined in `vdata/system/quests_santamonica.txt`.

| DLG node(s) | Condition / action | Result |
|---|---|---|
| 13 | `Persuasion 3`; sets `G.Copper_Stake=1` | Tells Copper a Holy Stake can make him human; opens the stake sale branch. |
| 33 | `Persuasion 3`; sets `G.Copper_Uni=1` | Tells him unicorn blood could reverse vampirism; opens the blood sale branch. |
| 92 | `Persuasion 5` and no Stake/Uni flag | Claims vampirism is reversible; this is a deceptive dialogue branch, with no action on the node itself. |
| 82 | `G.Patch_Plus==1`; `pc.SetQuest("Copper",1)` | Opens the Plus quest after the gum offer. |
| 102 / 163 | Plus, no prior gum, player has Ming's tentacle; removes the item and adds $100 | sells the “special chewing gum” story. |
| 142–146 | Player has blood packs and Copper's current count permits the quantity; removes 1–3 packs and adds $120 per pack | Fulfills the fake unicorn-blood request. Node 161 sets `Copper_Uni=2`; node 117 ends with quest state 4 if no stake flag. |
| 105 / 121 | `Copper_Stake==1` and player has `item_g_stake`; node 121 consumes stake and pays $100 | Fulfills the fake Holy Stake request. |
| 107 / 112 | `Intimidate 3` and no gum; node 107 sets `Copper_Rob=1` and pays $200 advance, node 112 (Plus) sets quest state 4 | Scams Copper for an advance without supplying the requested item. |
| 122–130 → 131 → 133 | Response conditions split on Humanity and Plus; node 131 sets `Copper_Slayer=1`; Plus node 133 sets quest state 2 | Names LaCroix, Nines, or the US President as the “head vampire,” persuading Copper to go after them. Some high-Humanity Plus lies reduce Humanity; the President lie also flags a Masquerade violation. State 2 is described as the suicide-mission success and awards `Copper01`. |

Quest state 4 is “exploited … for easy money” and also awards `Copper01`. State 3 is failure. The dialogue contains engine checks and Python actions; actual trait-check outcomes are not established by static inspection.

## Lily / E — “Thinned Blood”

The quest is named `Lily`, display name `Thinned Blood`. Its broader clue chain passes through the Diner and Clinic; see the linked notes above rather than repeating those investigations here.

| DLG / script node | Condition / action | Journal or consequence |
|---|---|---|
| `e.dlg` 119 / 139 / 149 / 159 | `G.E_Info==0`; sets `G.E_Quest=1`, Lily quest state 1 | E asks the player to investigate thin blood. |
| `diaryPickup()` | when Lily quest state is not 10, sets `E_Quest=2`, Lily state 2 | Journal stage 2; XP `Thinned02` is attached to this state. |
| Clinic Lily scene | `lilyDialog()` runs the release sequence when `G.Lily_Release` and not `G.Lily_Free`; when freed, starts her leave sequence | Lily quest state 3 / XP `Thinned03` is specified by journal data and the clinic interaction chain. The exact reachability is covered in the Clinic note. |
| `lily.dlg` 171 | Sets `E_Quest=3`, Lily state 3, adds 1 Humanity | Lily explains her sire and the thin-blood stigma. |
| `lily.dlg` 183 / 192 | `Humanity 6` | Tells player E forgives her and directs Lily back to E. Nodes 185 and 193 are different Humanity-gated responses, not equivalent success actions. |
| `e.dlg` 221 | Sets Lily state 8 | Successful reunion; awards `Thinned04`. |

Death and cutoff handling:

- Installed BSP wires `OnDeath` to `lilyKilled()` only when present in Clinic; it sets Lily state 4. `eDeath()` on the Pier sets Lily state 10 if the quest is active and not already at 4 or 8.
- `thinBloodsGone()` runs its cutoff branch at `G.Story_State >= 35`: activates `thinblood_killer`; converts current Lily state 2→5 or 3→6; for Plus Copper state 1→3. The journal defines Lily states 5 and 6 as failures and Copper state 3 as failure.
- `copperDeath()` sets Copper state 3 only in Plus and only when current Copper quest state is 1. `copperDialog()` handles Copper's leave state and triggers the leave sequence when `Copper_Slayer` is set; the installed BSP callback confirms this function is bound to Copper's dialogue end.

These are source-declared transitions. Whether entity callbacks occur in a particular playthrough, and when a player encounters them relative to the late-story cutoff, remains runtime-dependent.

## Sources and hashes

Hashes are SHA-256 of installed files:

| Source | SHA-256 |
|---|---|
| `Unofficial_Patch/maps/sm_pier_1.bsp` | `24206a31a00d56fba0d068011b212173503168d6baef43a60785213398db1df0` |
| `Unofficial_Patch/dlg/santa monica/copper.dlg` | `6671f208621f94e9665f78a3d7a5f3e4763a58c38ed1393b3920703c50c4f3b3` |
| `Unofficial_Patch/dlg/santa monica/e.dlg` | `73a9c91e80842ab9de131c756c0cbd00a0327d0e736dec5ae25a5afbf99adb23` |
| `Unofficial_Patch/dlg/santa monica/lily.dlg` | `67f23ea3acf8c42f9d505c6ea62b6e0d19b513388fa79749da2736ecaf5a251a` |
| `Unofficial_Patch/python/santamonica/santamonica.py` | `634c5a2e97566d709157f4cd43424509689199302a6433708f3d2ced53f13fff` |
| `Unofficial_Patch/python/vamputil.py` | `a2873d3a2a230c0ac9f38398e093910810f7ab3c51fa06bae71a7b004168e491` |
| `Unofficial_Patch/vdata/system/quests_santamonica.txt` | `d1f4cc18f44d4f231d0764a1d49da314fe4fb383ca70cddae8ef23db28b02f38` |
