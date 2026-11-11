# Arthur's Introduction Quest

**Status**: VERIFIED_STATIC for cited DLG fields. Runtime selection is UNVERIFIED.  
**Source**: UP+ 12.0 `Unofficial_Patch/dlg/santa monica/arthur.dlg` (SHA-256 `06d552f31c1f171dc46d1ab37061f7b0c8d33f3424603b11333a869e4ed62b2f`)  
**NPC**: Arthur Kilpatrick (Bail Bonds)  
**Location**: Santa Monica - Kilpatrick 24-Hour Bail Bonds

## Quest Overview

Arthur's Introduction documents the initial dialogue with Arthur Kilpatrick. The journal definitions in `Unofficial_Patch/vdata/system/quests_santamonica.txt:35–88,94–131` contain separate entries for `Arthur Knox` and `Bail Jumper`. An introduction entry is absent from that file.

## Evidence

### VERIFIED_STATIC: Record 11 - Initial Greeting

**Source**: `arthur.dlg:11`
**Field Mapping**:
- ID: "11"
- Response_1: "[with the panache of a hubcap salesman]Welcome to Kilpatrick 24-Hour Bail Bonds. My name's Arthur Kilpatrick. How can I help you?"
- Response_2: (Identical to Response_1)
- Next ID: "#"
- Conditions: "npc.SetDisposition(\"Joy\",1)"
- Scripts: "G.Arthur_Talked = 1"
- Brujah Response: (Empty)

**Analysis**:
- Contains `npc.SetDisposition("Joy",1)` in field 5, targeting the NPC
- Sets global variable `G.Arthur_Talked = 1` to track interaction (field 6)
- Identical response fields. Starting condition 1011 has literal target 11.

### VERIFIED_STATIC: Record 21 - Business Explanation

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
- Reveals Arthur's business model

### VERIFIED_STATIC: Record 31 - Employees and Location

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
- Explains Arthur's staff and operations
- Provides context about Santa Monica location

## Dialogue Structure

### Initial Branching (Records 11-35)

**Malkavian-Specific Paths**:
- Record 12: `not IsClan(pc,"Malkavian")`
- Record 13: `not IsClan(pc,"Malkavian") and G.Extra_Lines == 1`
- Record 14 → 711: `not IsClan(pc,"Malkavian")`
- Record 15 → 571: `IsClan(pc,"Malkavian")`
- Record 16: empty numbered row
- Record 20: literal target `0`, empty condition

**General Dialogue Paths**:
- Records 22→31 and 23→41 cover employees and business. ID 24→741 asks about work when `G.Arthur_Knox < 2`.
- Records 33-34: General conversation
- Record 35: `G.Arthur_BJ == 1 and G.Extra_Lines == 1`

## Global Variables and Entry Conditions

| Status | Direct evidence |
|---|---|
| VERIFIED_STATIC | ID 11 writes `G.Arthur_Talked = 1`, ID 21 writes `G.Arthur_Run = 1`. |
| VERIFIED_STATIC | `G.Arthur_BH` is checked at IDs 34, 43, 73 and 554. IDs 122, 602 and 702 are empty. See [[Bail_Hustler_Quest]]. |
| VERIFIED_STATIC | `G.Arthur_BJ` is checked at IDs 35 and 66, and written in 41 and 741. See [[Bail_Jumper_Quest]]. |
| VERIFIED_STATIC | `G.Arthur_Knox` is checked at IDs 34, 73 and 554. ID 691 writes `G.Arthur_Knox = 2` and separately calls `pc.SetQuest("Arthur Knox", 1)`. |
| INFERRED | `G.Arthur_Talked` tracks prior conversation, and `G.Arthur_Run` tracks discussion of Arthur's business. Default values and full runtime semantics are UNVERIFIED here. |

| Starting-condition ID | Literal target | Condition |
|---|---|---|
| 1009 | 361 | `G.Arthur_Muddy == 2` |
| 1010 | 231 | `G.Arthur_Talked > 0` |
| 1011 | 11 | `G.Arthur_Talked == 0 and G.Patch_Plus == 0` |
| 1012 | 2 | `G.Arthur_Talked == 0 and G.Patch_Plus == 1` |

These rows are VERIFIED_STATIC. Entry selection among concurrently eligible rows and the scope of `G.Arthur_SM`, `G.Know_Murder` and `G.Arthur_Killer` remain UNVERIFIED here. See [[Santa_Monica_Discovery]] for the related local investigation.

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

- **UNVERIFIED**: actual greeting selection, priority of overlapping start conditions, and runtime reachability of the inferred phases.

**Evidence**: direct dialogue fields and journal definitions.  
**INFERRED**: phase grouping based on dialogue topics.
