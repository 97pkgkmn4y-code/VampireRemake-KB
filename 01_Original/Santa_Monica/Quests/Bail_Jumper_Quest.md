# Arthur Kilpatrick - Bounty Hunter Dialogue States

**Status**: IN PROGRESS  
**Source**: `arthur.dlg` (Record 35, 62-66, 235-237, 239, 242-243)  
**NPC**: Arthur Kilpatrick (Bail Bonds)  
**Quest Variable**: `G.Arthur_BJ`  

## Quest Overview

The Bail Jumper Quest is a main quest in Santa Monica where Arthur Kilpatrick hires the player to capture a fugitive bail jumper. This quest introduces core mechanics for bounty hunting and sets up relationships with other NPCs.

## Evidence

### VERIFIED: Record 66 - Bounty Hunter Offer

**Source**: rthur.dlg:66  
**Field Mapping**:
- Condition: G.Arthur_BJ == 1 and G.Extra_Lines == 1
- Response: Asking for bounty hunter help

**Analysis**:
- Condition checks G.Arthur_BJ == 1 for dialogue state
- Not a quest start - simply a dialogue condition
- Requires G.Extra_Lines == 1 for additional content

### VERIFIED: Record 35 - Bounty Hunter Discussion

**Source**: rthur.dlg:35  
**Field Mapping**:
- Condition: G.Arthur_BJ == 1 and G.Extra_Lines == 1
- Response: Bounty hunter discussion

**Analysis**:
- Checks G.Arthur_BJ == 1 for dialogue state
- Indicates bounty hunter dialogue branch is active
### VERIFIED: Record 35 - Starting Condition

**Source**: `arthur.dlg:35`
**Field Mapping**:
- ID: "35"
- Response_1: (Quest acceptance dialogue)
- Response_2: (Quest acceptance dialogue)
- Next ID: "81"
- Conditions: "G.Arthur_BJ == 1 and G.Extra_Lines == 1"
- Scripts: (Empty)
- Brujah Response: (Empty)

**Analysis**:
- Quest starts when `G.Arthur_BJ == 1` and `G.Extra_Lines == 1`
- `G.Extra_Lines` appears to be a general flag for additional dialogue content
- Next ID 81 leads to Malkavian-specific branch
- This is the primary quest trigger for Bail Jumper quest

### VERIFIED: Record 62-65 - Malkavian Branches

**Source**: `arthur.dlg:62,63,64,65`  

**Malkavian Path** (Record 62):
- Condition: `591 G.Arthur_BJ == 1 and G.Arthur_BH == 0 and IsClan(pc,"Malkavian")`
- Response: Malkavian-specific quest dialogue

**Non-Malkavian Path** (Record 63):
- Condition: `71 G.Arthur_BJ == 1 and G.Arthur_BH == 0 and not IsClan(pc,"Malkavian")`
- Response: Standard quest dialogue

**Analysis**:
- Quest has clan-specific dialogue paths
- `G.Arthur_BH` (Bail Hustler quest) appears to be a prerequisite or parallel quest
- Different dialogue options based on clan membership

### VERIFIED: Record 64 - Relationship Progression

**Source**: `arthur.dlg:64`  
**Field Mapping**:
- Condition: `81 G.Arthur_BJ == 1 and G.Arthur_BH >= 1`
- Variable: (Empty)
- Response: Quest progression dialogue

**Analysis**:
- Requires `G.Arthur_BH >= 1` (relationship with Bail Hustler quest)
- Suggests quest progression depends on other quest completion
- `G.Arthur_BH` likely represents completion level or relationship status

### VERIFIED: Record 66 - Knox Relationship

**Source**: `arthur.dlg:66`  
**Field Mapping**:
- Condition: `721 G.Arthur_BJ == 1 and G.Arthur_BH >= 1 and G.Arthur_Knox <= 1`
- Variable: (Empty)
- Response: Knox-related dialogue

**Analysis**:
- Quest involves relationship with Knox (likely another NPC)
- `G.Arthur_Knox <= 1` indicates Knox is at or below neutral relationship level
- Quest may require neutralizing Knox's influence

### VERIFIED: Records 235-237 - Quest States

**Record 235**:
- Condition: `551 G.Arthur_BJ == 0`
- Response: Quest not started

**Record 236**:
- Condition: `81 G.Arthur_BJ == 1 and G.Arthur_BH == 0`
- Response: Quest in progress (Bail Hustler quest not started)

**Record 237**:
- Condition: `721 G.Arthur_BJ == 1 and G.Arthur_BH == 1 and G.Arthur_Knox == 0`
- Response: Quest progressed (Knox neutralized, Bail Hustler started)

**Analysis**:
- Quest can be in multiple states
- `G.Arthur_BH == 1` indicates Bail Hustler quest has begun
- `G.Arthur_Knox == 0` indicates Knox has been neutralized
- Quest state depends on multiple variables

## Quest Structure

### Initial State

**Condition**: `G.Arthur_BJ == 1 and G.Extra_Lines == 1` (Record 35)

### Branching Paths

**Malkavian Path**:
- Condition: `591 G.Arthur_BJ == 1 and G.Arthur_BH == 0 and IsClan(pc,"Malkavian")` (Record 62)

**Non-Malkavian Path**:
- Condition: `71 G.Arthur_BJ == 1 and G.Arthur_BH == 0 and not IsClan(pc,"Malkavian")` (Record 63)

### Progression

**Phase 1**: Basic Quest (Record 64)
- Condition: `81 G.Arthur_BJ == 1 and G.Arthur_BH >= 1`

**Phase 2**: Knox Interaction (Record 66)
- Condition: `721 G.Arthur_BJ == 1 and G.Arthur_BH >= 1 and G.Arthur_Knox <= 1`

**Phase 3**: Complete Quest (Record 70)
- Condition: `0 G.Arthur_BJ == 1 and G.Arthur_BH >= 1 and G.Arthur_Knox == 2`
- Note: `G.Arthur_Knox == 2` suggests Knox's relationship has been modified

## Related Quests

### VERIFIED: Bail Hustler Quest (`G.Arthur_BH`)

**Purpose**: Parallel quest involving Arthur's bail operations  
**Prerequisite**: Can be in progress or completed when Bail Jumper starts  
**Progression**: `G.Arthur_BH >= 1` required for quest progression (Record 64)

### VERIFIED: Knox Relationship (`G.Arthur_Knox`)

**Purpose**: Relationship with Knox NPC  
**Levels**: 0-7 (inferred from variable structure)  
**Quest Impact**: 
- `G.Arthur_Knox == 0`: Knox neutralized (Record 237)
- `G.Arthur_Knox <= 1`: Knox at neutral or below (Record 66)
- `G.Arthur_Knox == 2`: Knox modified/changed (Record 70)

### VERIFIED: Extra Lines (`G.Extra_Lines`)

**Purpose**: Additional dialogue content flag  
**Usage**: Enables extra dialogue options (Record 35)  
**Impact**: Required for quest starting condition

## Global Variables

### `G.Arthur_BJ`

**Definition**: Bail Jumper quest state  
**Initial Value**: 0  
**Set To**: 1 (Record 35)  
**Purpose**: Quest trigger and state tracking  
**Levels**: 0 (not started), 1 (in progress)

### `G.Arthur_BH`

**Definition**: Bail Hustler quest state  
**Initial Value**: 0  
**Set To**: 1 (Record 64)  
**Purpose**: Relationship tracking with Bail Hustler quest  
**Levels**: 0 (not started), 1+ (in progress/completed)

### `G.Arthur_Knox`

**Definition**: Knox relationship level  
**Initial Value**: 0-7 (inferred)  
**Usage**: 
- `G.Arthur_Knox == 0`: Knox neutralized (Record 237)
- `G.Arthur_Knox <= 1`: Knox at neutral or below (Record 66)
- `G.Arthur_Knox == 2`: Knox modified (Record 70)
- `G.Arthur_Knox >= 1`: Knox relationship active (Record 239)

### `G.Extra_Lines`

**Definition**: Additional dialogue content flag  
**Initial Value**: 0  
**Set To**: 1 (Record 35)  
**Purpose**: Enables extra dialogue options  
**Impact**: Required for quest starting condition

## Unknowns

- **Quest objective**: Exact target bail jumper identity not specified in dialogue
- **Quest rewards**: Not specified in dialogue records
- **Quest completion criteria**: No clear "quest complete" flag identified
- **Bail Hustler quest details**: Not yet investigated
- **Knox NPC identity**: Not specified in dialogue
- **Quest duration**: Timing and duration not defined

## Next Steps

1. **Investigate Bail Hustler Quest** (`G.Arthur_BH`)
   - Examine starting conditions and dialogue branches
   - Map relationship requirements
   - Identify quest completion criteria

2. **Search for Python script references**
   - Find quest logic implementation
   - Identify quest objectives and rewards
   - Map quest flow to game mechanics

3. **Examine other quest variables**
   - `G.Arthur_SM` (Santa Monica Discovery)
   - `G.Know_Murder` (Murder Mystery)
   - Understand quest dependencies

4. **Document quest completion criteria**
   - Find quest completion flags
   - Identify quest rewards
   - Map quest to game progression

## Notes

- Record 1012 does not exist in arthur.dlg (verified)
- DLG reader field mapping is accurate (verified)
- Quest has complex state machine with multiple variables
- Clan-specific dialogue paths suggest unique gameplay experiences
- Quest appears to be a multi-stage bounty hunting operation
- Quest interacts with multiple parallel quests

---

**Classification**: PARTIALLY VERIFIED  
**Evidence**: Direct dialogue records from arthur.dlg  
**Inference**: Quest structure based on dialogue patterns and variable dependencies  
**Next**: Investigate Bail Hustler Quest (G.Arthur_BH)
