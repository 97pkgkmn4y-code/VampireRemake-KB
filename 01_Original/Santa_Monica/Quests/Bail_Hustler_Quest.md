# Arthur Kilpatrick - Business Dialogue States

**Status**: IN PROGRESS  
**Source**: `arthur.dlg` (Record 34, 43, 73, 554, 122, 602, 702)  
**NPC**: Arthur Kilpatrick (Bail Bonds)  
**Quest Variable**: `G.Arthur_BH`  

## Overview

This document tracks Arthur Kilpatrick's business/hustle dialogue states (variable G.Arthur_BH) across multiple dialogue records in rthur.dlg. These are **dialogue state variables**, not separate quest objectives. The variable tracks player interactions about Arthur's bail bond operations.

## Evidence

### VERIFIED: Record 34 - Business Discussion Start

**Source**: `arthur.dlg:34`
**Field Mapping**:
- ID: "34"
- Response_1: (Bounty hunter discussion)
- Response_2: (Bounty hunter discussion)
- Next ID: "181"
- Conditions: "G.Arthur_BH == 0 and G.Arthur_Knox < 1"
- Scripts: (Empty)
- Brujah Response: "Hunting bounties sounds exciting."
- Malkavian Response: "Hunting bounties sounds exciting."

**Analysis**:
- Condition checks G.Arthur_BH == 0 (business state not yet engaged)
- G.Arthur_Knox < 1 indicates Knox relationship constraint
- Next ID 181 leads to Malkavian-specific dialogue
- This is a **dialogue state check**, not a quest objective

### VERIFIED: Record 43 - Business Discussion

**Source**: `arthur.dlg:43`
**Field Mapping**:
- ID: "43"
- Response_1: (Player asks about bail operations)
- Response_2: (Player asks about bail operations)
- Next ID: "71"
- Conditions: "G.Arthur_BH == 0"
- Scripts: (Empty)
- Brujah Response: "Do you get many people to hunt?"
- Malkavian Response: "Do you get many people to hunt?"

**Analysis**:
- Checks G.Arthur_BH == 0 for dialogue state
- Next ID 71 leads to Malkavian-specific dialogue
- Not a quest start - simply a dialogue condition

### VERIFIED: Record 73 - Business Discussion In Progress

**Source**: rthur.dlg:73  
**Field Mapping**:
- Condition: G.Arthur_BH == 1 and G.Arthur_Knox < 1
- Response: Continues business discussion

**Analysis**:
- Checks G.Arthur_BH == 1 for dialogue state
- Indicates business dialogue branch is active

### VERIFIED: Record 554 - Business Discussion End

**Source**: rthur.dlg:554  
**Field Mapping**:
- Condition: G.Arthur_BH == 1
- Response: Business discussion concludes

**Analysis**:
- Checks G.Arthur_BH == 1 to determine dialogue end
- Not a quest completion - dialogue state tracking

### VERIFIED: Records 122, 602, 702 - Business Dialogue State

**Record 122**:
- Condition: G.Arthur_BH < 2 and G.Arthru_Knox < 1

**Record 602**:
- Condition: G.Arthur_BH < 2 and G.Arthru_Knox < 1

**Record 702**:
- Condition: G.Arthur_BH < 2 and G.Arthru_Knox < 1

**Analysis**:
- Checks G.Arthur_BH < 2 for dialogue state progression
- Tracks multiple stages of business dialogue
- All are **dialogue state checks**, not quest milestones
### VERIFIED: Record 34 - Starting Condition (Knox Relationship)

**Source**: `arthur.dlg:34`  
**Field Mapping**:
- Condition: `181 G.Arthur_BH == 0 and G.Arthru_Knox < 1`
- Variable: (Empty)
- Response: Quest initiation dialogue

**Analysis**:
- Quest starts when `G.Arthur_BH == 0` and `G.Arthru_Knox < 1`
- `G.Arthru_Knox < 1` indicates Knox's relationship is at or below neutral
- Quest may involve dealing with Knox's interference

### VERIFIED: Record 43 - Starting Condition (Basic)

**Source**: `arthur.dlg:43`  
**Field Mapping**:
- Condition: `71 G.Arthur_BH == 0`
- Variable: (Empty)
- Response: Quest initiation dialogue

**Analysis**:
- Simpler starting condition without Knox relationship requirement
- `G.Arthur_BH == 0` indicates quest not started
- More accessible starting point for players who haven't dealt with Knox

### VERIFIED: Record 73 - Quest In Progress

**Source**: `arthur.dlg:73`  
**Field Mapping**:
- Condition: `671 G.Arthur_BH == 1 and G.Arthur_Knox < 1`
- Variable: (Empty)
- Response: Quest progression dialogue

**Analysis**:
- Quest in progress when `G.Arthur_BH == 1` and `G.Arthur_Knox < 1`
- `G.Arthur_Knox < 1` continues Knox relationship constraint
- Suggests ongoing interaction with Knox

### VERIFIED: Record 554 - Quest Completion

**Source**: `arthur.dlg:554`  
**Field Mapping**:
- Condition: `671 G.Arthur_BH == 1`
- Variable: (Empty)
- Response: Quest completion dialogue

**Analysis**:
- Quest completes when `G.Arthur_BH == 1`
- `671` may be a quest state or completion flag
- Suggests `G.Arthur_BH == 1` represents quest completion

### VERIFIED: Records 122, 602, 702 - Quest State Tracking

**Record 122**:
- Condition: `671 G.Arthur_BH < 2 and G.Arthru_Knox < 1`

**Record 602**:
- Condition: `671 G.Arthur_BH < 2 and G.Arthru_Knox < 1`

**Record 702**:
- Condition: `671 G.Arthur_BH < 2 and G.Arthru_Knox < 1`

**Analysis**:
- Quest state tracked with `G.Arthur_BH < 2`
- `G.Arthru_Knox < 1` continues Knox relationship constraint
- Quest may have multiple stages or completion levels
- Quest appears to be a multi-stage operation

## Quest Structure

### Initial State

**Condition**: `G.Arthur_BH == 0` (Records 34, 43)

### Quest In Progress

**Condition**: `G.Arthur_BH == 1 and G.Arthur_Knox < 1` (Record 73)

**Variants**:
- Knox Relationship Required: `G.Arthur_BH == 0 and G.Arthru_Knox < 1` (Record 34)
- Basic Access: `G.Arthur_BH == 0` (Record 43)

### Variable Status

**STATIC VERIFIED**: Variable G.Arthur_BH appears in multiple DLG records (34, 43, 73, 554, 122, 602, 702) with condition checks
**INFERRED**: Variable represents dialogue state tracking, not quest completion
**UNKNOWN**: Exact game runtime behavior requires testing
