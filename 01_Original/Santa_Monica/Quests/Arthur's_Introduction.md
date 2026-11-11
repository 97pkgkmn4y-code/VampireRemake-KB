# Arthur\'s Introduction Quest

**Status**: IN PROGRESS  
**Source**: `arthur.dlg` (Record 11-1010)  
**NPC**: Arthur Kilpatrick (Bail Bonds)  
**Location**: Santa Monica - Kilpatrick 24-Hour Bail Bonds

## Quest Overview

Arthur\'s Introduction is the initial quest that establishes the player\'s first interaction with Arthur Kilpatrick, the bail bondsman in Santa Monica. This quest introduces basic dialogue mechanics and sets up several related quests.

## Evidence

### VERIFIED: Record 11 - Initial Greeting

**Source**: `arthur.dlg:11`
**Field Mapping**:
- ID: "11"
- Response_1: "[with the panache of a hubcap salesman]Welcome to Kilpatrick 24-Hour Bail Bonds. My name\'s Arthur Kilpatrick. How can I help you?"
- Response_2: (Identical to Response_1)
- Next ID: "#"
- Conditions: "npc.SetDisposition(\"Joy\",1)"
- Scripts: "G.Arthur_Talked = 1"
- Brujah Response: (Empty)

**Analysis**:
- Sets player\'s disposition to "Joy" when entering dialogue (field 5)
- Sets global variable `G.Arthur_Talked = 1` to track interaction (field 6)
- Identical response_1 and response_2 suggest this is the primary greeting

### VERIFIED: Record 21 - Business Explanation

**Source**: `arthur.dlg:21`
**Field Mapping**:
- ID: "21"
- Response_1: (Business explanation)
- Next ID: "#"
- Conditions: "npc.SetDisposition(\"Neutral\",1)"
- Scripts: "G.Arthur_Run = 1"
- Brujah Response: (Empty)

**Analysis**:
- Changes disposition to "Neutral" (field 5)
- Sets global variable `G.Arthur_Run = 1` (field 6)
- Reveals Arthur\'s business model

### VERIFIED: Record 31 - Employees and Location

**Source**: `arthur.dlg:31`
**Field Mapping**:
- ID: "31"
- Response_1: (Explains employees)
- Next ID: "#"
- Conditions: "npc.SetDisposition(\"Neutral\",1)"
- Scripts: (Empty)
- Brujah Response: (Empty)

**Analysis**:
- Changes disposition to "Neutral" (field 5)
- Explains Arthur\'s staff and operations
- Provides context about Santa Monica location

## Dialogue Structure

### Initial Branching (Records 11-35)

**Malkavian-Specific Paths**:
- Record 12: `not IsClan(pc,"Malkavian")`
- Record 13: `not IsClan(pc,"Malkavian") and G.Extra_Lines == 1`
- Record 14: `711 not IsClan(pc,"Malkavian")`
- Record 15: `571 IsClan(pc,"Malkavian")`
- Record 16: `0 IsClan(pc,"Malkavian")`
- Record 20: `0 not IsClan(pc,"Malkavian")`

**General Dialogue Paths**:
- Records 22-24: Player questions about business
- Records 33-34: General conversation
- Record 35: `G.Arthur_BJ == 1 and G.Extra_Lines == 1`

## Global Variables

### VERIFIED: `G.Arthur_Talked`

**Definition**: Tracks whether player has spoken to Arthur  
**Initial Value**: 0  
**Set To**: 1 (Record 11)  
**Purpose**: Basic interaction tracking

### VERIFIED: `G.Arthur_Run`

**Definition**: Indicates Arthur is running his business  
**Initial Value**: 0  
**Set To**: 1 (Record 21)  
**Purpose**: Business state tracking

### VERIFIED: `npc.SetDisposition`

**Definition**: Sets NPC disposition  
**Values**: "Joy", "Neutral", "Anger", "Fear", "Flirt", "Confused"  
**Usage**: Dynamic dialogue responses based on player actions


### Related Quests Identified

1. **Bail Jumper Quest** (`G.Arthur_BJ`)
2. **Bail Hustler Quest** (`G.Arthur_BH`)
3. **Santa Monica Discovery** (`G.Arthur_SM`)
4. **Knox Relationship** (`G.Arthur_Knox`)
5. **Murder Mystery** (`G.Know_Murder`, `G.Arthur_Killer`)

### Starting Conditions

- **Record 1010**: `G.Arthur_Muddy == 2`
- **Record 1011**: `G.Arthur_Talked > 0`

**Analysis**: The actual quest starts when player has `G.Arthur_Talked > 0` (verified by Record 1011)


## Dialogue State Variables (NOT Separate Quests)

### VERIFIED: G.Arthur_BH

**Definition**: Tracks Arthur's business/hustle dialogue state  
**Initial Value**: 0  
**Usage**: Appears in Record 34, 43, 122, 181 as condition checks  
**Purpose**: Tracks player's interaction with Arthur's business discussions  
**Status**: **STATIC VERIFIED** - Variable appears in DLG conditions

### VERIFIED: G.Arthur_BJ

**Definition**: Tracks player bounty hunter interactions with Arthur  
**Initial Value**: 0  
**Usage**: Appears in Record 66, 35 as condition checks  
**Purpose**: Tracks player bounty hunter dialogue branches  
**Status**: **STATIC VERIFIED** - Variable appears in DLG conditions

### VERIFIED: G.Arthur_Knox

**Definition**: Tracks player-Knox relationship state  
**Initial Value**: 0  
**Usage**: Appears in Record 34, 73, 122, 602, 702 as condition checks  
**Purpose**: Tracks player interactions with Knox  
**Status**: **STATIC VERIFIED** - Variable appears in DLG conditions

**INFERRED**: These variables track dialogue states and player-NPC relationships, not separate quest objectives. Claims that G.Arthur_BH, G.Arthur_BJ, G.Arthur_SM, G.Arthur_Knox, G.Know_Murder, or G.Arthur_Killer represent separate quests lack VMF evidence and are **INFERRED** based on variable names only.

## Starting Conditions

**Record 1010**: G.Arthur_Muddy == 2
**Record 1011**: G.Arthur_Talked > 0

**Analysis**: The actual quest interaction starts when player has G.Arthur_Talked > 0 (verified by Record 1011)

**STATIC VERIFIED**: Record 1011 exists in rthur.dlg and contains condition G.Arthur_Talked > 0.

## Inferred Structure

Based on dialogue pattern analysis:

1. **Entry Phase** (Records 11-20):
   - Initial greeting (Record 11)
   - Disposition change to Joy
   - Set `G.Arthur_Talked = 1`

2. **Explanation Phase** (Records 21-35):
   - Business explanation (Record 21)
   - Employee information (Record 31)
   - Clan-specific dialogue paths
   - General conversation options

3. **Advanced Dialogue** (Records 40-101):
   - Player questions about business
   - Thematic dialogue
   - Relationship development

## Unknowns

- **Exact quest completion criteria**: No clear "quest complete" flag identified
- **Quest rewards**: Not specified in dialogue records
- **Quest duration**: Timing and duration not defined
- **Relationship progression**: Exact progression mechanics unclear

## Next Steps

1. Investigate `G.Arthur_BJ` (Bail Jumper quest) starting conditions
2. Examine Python script references for quest logic
3. Search for quest completion conditions
4. Map dialogue connections to quest states

## Notes

- Record 1012 does not exist in arthur.dlg (verified)
- DLG reader field mapping is accurate (verified)
- Malkavian-specific dialogue paths suggest unique gameplay experiences
- Multiple parallel quests can be accessed simultaneously

---

**Classification**: PARTIALLY VERIFIED  
**Evidence**: Direct dialogue records  
**Inference**: Quest structure based on dialogue patterns  
**Next**: Investigate Bail Jumper quest
