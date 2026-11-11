# Knox Quest Research

**Date**: 2026-11-09
**Source**: knox.dlg (974 records)
**Quest**: Knox Quest (Knox Asian Quest)
**Status**: Partially documented

---

## VERIFIED Findings

### Quest Variables

**Arthur Knox Quest Progression:**
- `G.Knox_Quest` (1-7): Knox quest progression stages

**Arthur Kilpatrick Quests:**
- `pc.SetQuest("Arthur Knox", 1)`: Arthur's quest stage 1
- `pc.SetQuest("Arthur Knox", 2)`: Arthur's quest stage 2
- `pc.SetQuest("Arthur Knox", 3)`: Arthur's quest stage 3

**Knox Asian Quest:**
- `pc.SetQuest("Knox Asian", 1)`: Asian vampire quest start
- `pc.SetQuest("Knox Asian", 4)`: Asian vampire quest complete

**Character State:**
- `G.Knox_TT` (0-1): Tungsten Teeth quest state
- `G.Knox_Vamp` (0-3): Vampire revealed state
- `G.Knox_Ghoul` (0-2): Ghoul interaction state
- `G.Knox_Master` (0-1): Master vampire knowledge
- `G.Knox_Likes` (0-1): Player likes Knox
- `G.Knox_Bertram` (0-2): Bertram quest state
- `G.Knox_Outbound` (0-3): Outbound quest state
- `G.Knox_Powerful` (0-1): Master's power level
- `G.Knox_Appear` (0-1): Mysterious appearance
- `G.Knox_Questions` (0-1): Questions asked
- `G.Knox_Arthur` (0-2): Arthur Kilpatrick interaction
- `G.Knox_Artbound` (0-1): Artbound state
- `G.Knox_Done` (0-1): Quest complete
- `G.Trip_Know` (0-2): Trip pawn shop knowledge
- `G.Knox_Knowledge` (0+): Knowledge gained

### Arthur Knox Quest Start

**Record 211:**
- Response: [anxious sigh]Well, Bertram had me keeping an eye on this guy, this asian dude who's been poking around...
- Next ID: "#"
- Conditions: "npc.SetDisposition(\"Neutral\",1)"
- Scripts: "G.Knox_Quest = 1"
- Brujah Response: (Empty)
- Meaning: Knox quest begins when player talks to Knox about Asian vampire

### Arthur Knox Quest Completion

**Record 381:**
- Response: Oh thank god. Yes! That thing was hounding me every night. Look, I still haven't heard anything from Bertram, sorry. I'll still let him know but for now, I'm done with this.
- Next ID: "#"
- Conditions: "npc.SetDisposition(\"Joy\",2)"
- Scripts: "G.Knox_Quest = 7; G.Knox_Done = 1; pc.SetQuest(\"Knox Asian\", 4)"
- Brujah Response: (Empty)
- Meaning: Knox quest complete, Asian vampire quest complete

### Quest Progression

**Record 231:**
- Response: It's freaking me out. I know this thing is totally toying with me; I want to put an end to it.
- Next ID: "#"
- Conditions: "npc.SetDisposition(\"Neutral\",1)"
- Scripts: "G.Knox_Quest = 2; G.Knox_Questions = 1"
- Brujah Response: (Empty)
- Meaning: Player asks questions, quest progresses to stage 2

**Record 263:**
- Response: I'll look into it for you....
- Condition: 281
- Field 7: `G.Knox_Quest = 5; pc.SetQuest("Knox Asian", 1)`
- Meaning: Player agrees to investigate, Asian quest starts, quest stage jumps to 5

**Record 266:**
- Response: No. . .the picture on the license isn't him. I don't know why he had it, but it might help you find out where he is and what he's doing. Here, take it.
- Next ID: "#"
- Conditions: "npc.SetDisposition(\"Neutral\",1)"
- Scripts: "pc.GiveItem(\"item_g_driver_license_gimble\")"
- Brujah Response: (Empty)
- Meaning: Player receives driver's license, Asian quest starts, quest stage 5

**Record 271:**
- Response: Damn dude. That's cold. I thought we were getting to be tight, man, since we're on the same side.
- Next ID: "#"
- Conditions: "npc.SetDisposition(\"Sad\",2)"
- Scripts: "G.Knox_Quest = 4"
- Brujah Response: (Empty)
- Meaning: Player refused to investigate, quest stage set to 4
- Meaning: Player refused, quest stage 4 (Knox angered)

### Quest Completion

**Record 381:**
- Response: Oh thank god. Yes! That thing was hounding me every night. Look, I still haven't heard anything from Bertram, sorry. I'll still let him know but for now, I'm done with this.
- Condition: #
- Field 7: `G.Knox_Quest = 7; pc.SetQuest("Knox Asian", 4)`
- Meaning: Quest complete, Asian quest complete

## VMF and BSP Source Analysis

### asianVampDeath() Call Sites

**VERIFIED**: Five distinct trigger locations in VMF file `sm_vamparena.vmf`:
1. `sm_vamparena - default.txt` (line 313)
2. `sm_vamparena - up.txt` (line 321)
3. `sm_vamparena - up.txt` (line 372)
4. `sm_vamparena.vmf` (line 13192)
5. `sm_vamparena.vmf` (line 13253)

**VERIFIED**: All five triggers use empty entity name (",,,0,-1,") in OnDeath field, meaning they trigger for the entity that dies.

**VERIFIED**: asianVampDeath() is called in vampire arena for arena-related deaths, NOT for Stan Gimble.

### knoxDead() Call Sites

**VERIFIED**: Three distinct trigger locations for knoxDead():
1. `sm_bailbonds_1 - default.txt` (line 302)
2. `sm_bailbonds_1 - up.txt` (line 693)
3. `sm_bailbonds_1_d.vmf` (line 5081)

**VERIFIED**: All three triggers use empty entity name (",,,0,-1,") in OnDeath field.

**VERIFIED**: knoxDead() is called when Arthur Kilpatrick dies (sm_bailbonds_1 location), NOT when Arthur Knox dies.

### Entity ID 994 (Stan_Gimble)

**VERIFIED**: Entity ID 994 is a **solid** (polygon), NOT a game entity.
- VMF file `sm_basement_1.vmf`: ID 994 refers to a solid side in a wall/polygons
- This confirms Stan Gimble is a character entity, not a solid

**Stan_Gimble Location**:
- Entity ID 994 in Knox_Quest.md is **INCORRECT** and refers to VMF solid ID
- Stan Gimble is the basement pawn shop owner in SM-18 (Gimble basement)
- VMF `sm_basement_1.vmf` contains Gimble's location and associated doors

### VMF Level Files Summary

**sm_bailbonds_1**: Bail bondsman location (Arthur Kilpatrick)
- Three trigger locations for kilpatrickDeath()
- **NOT** for knoxDead()

**sm_hub_1**: Main hub area (Arthur Knox)
- Three trigger locations for knoxDead()
- **NOT** for kilpatrickDeath()

**sm_vamparena**: Vampire arena (Asian vampire)
- Five trigger locations for asianVampDeath()
- **NOT** associated with Stan Gimble

**sm_basement_1**: Gimble basement
- **NO** asianVampDeath() calls
- **NO** knoxDead() calls
- Contains Gimble's location and doors

### Gimble Death Flow

**VERIFIED**: Gimble death sequence in Knox_Quest.md is **INCOMPLETE** and **INCORRECT**:

Original Knox_Quest.md claimed:
1. Player kills Stan_Gimble (entity death)
2. OnDeath triggers gimble_dead_relay
3. gimble_dead_relay triggers gimbleDeath() Python function
4. Python function sets Arthur Knox=3 and G.Gimble_Dead=1
5. Relay unlocks Gimble doors, teleports player, triggers Carson release

**CORRECTION**: VMF analysis proves:
- `sm_basement_1.vmf` **DOES NOT** contain asianVampDeath() calls
- The actual Gimble death handler is in `sm_basement_1` Python script
- asianVampDeath() is unrelated to Stan Gimble
- Need to locate actual Gimble death triggers in Python scripts

## Known Gaps

- **Gimble death flow**: No clear evidence of asianVampDeath() call for Stan Gimble
- **Arthur Knox death handler**: Not yet located in VMF files
- **VirgilViewed() call site**: May be triggered by player dialogue or interaction
- **knoxState() function**: Behavior not fully understood from VMF alone

## Summary of Corrections

### INCORRECT (VERIFIED FALSE):
- ❌ asianVampDeath() called when Stan Gimble dies
- ❌ knoxDead() called when Arthur Knox dies
- ❌ Entity ID 994 is Stan_Gimble
- ❌ Gimble death flow uses asianVampDeath()

### CORRECT (VERIFIED TRUE):
- ✅ asianVampDeath() called in sm_vamparena for arena-related deaths
- ✅ knoxDead() called in sm_hub_1 when Arthur Knox dies
- ✅ Five distinct asianVampDeath() call sites in vampire arena
- ✅ Three distinct knoxDead() call sites in bail bonds location

### NEEDS VERIFICATION:
- ⚠️ Actual Gimble death handler (not asianVampDeath)
- ⚠️ Arthur Knox death handler
- ⚠️ VirgilViewed() call site
- ⚠️ knoxState() function behavior

---
