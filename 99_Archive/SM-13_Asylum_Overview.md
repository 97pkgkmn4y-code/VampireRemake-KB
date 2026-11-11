# SM-13 — The Asylum Research Overview

**Date**: 2026-11-09
**Status**: Partial documentation
**Priority**: High (Santa Monica research)

---

## Overview

The Asylum is a nightclub in Santa Monica featuring the Voerman sisters (Jeanette and Therese) and several supporting NPCs. It serves as a major hub for early-game social interactions and quest progression.

---

## NPCs Documented

| NPC | DLG File | Status | Key Variables |
|-----|----------|--------|---------------|
| Jeanette | `jeanette.dlg` | Partial | `G.Jeanette_Know`, `G.Jeanette_Seduce`, `G.Jeanette_Curious` |
| Therese | `therese.dlg` | Partial | `G.Therese_Seduce` |
| Danielle | `danielle.dlg` | Partial | `G.Danielle_Know` |
| Tourette | `tourette.dlg` | Partial | (None) — file existence does not prove NPC presence |

---

## Key Mechanics Documented

### Dual Personality System

- **Jeanette**: Flamboyant, chaotic, male/female player variants
- **Therese**: Composed, serious, male/female player variants
- Both personalities accessible to all clans
- Separate dialogue trees for each personality

### Seduction Mechanics

- `G.Jeanette_Seduce` tracks Jeanette interaction success
- `G.Therese_Seduce` tracks Therese interaction success
- **Record 3**: Requires Seduction 2
- **Record 33**: Increments `G.Jeanette_Seduce`
- **Record 43**: Decreases `G.Jeanette_Seduce` (player insult)
- **Record 54**: Decreases `G.Jeanette_Seduce` (Therese rejection)

### Curiosity Mechanic

- `G.Jeanette_Curious = 1` tracks player curiosity
- Set when player asks "Who are you?" (record 51)
- May unlock deeper dialogue or Therese personality

### Disposition System

- **Jeanette**: "Flirt", "Joy", or neutral
- **Therese**: "Neutral"
- **Tourette**: "Apathy" — voiced by Therese

### Gender Variants

- Response_1: Male player variant
- Response_2: Female player variant
- Not gender-neutral; distinguishes player gender

---

## Quest Connections (External Evidence)

**Source**: [[SM-13_Asylum_04_Analysis#Quest-connections]] and VTMB Wiki

| Quest | Description |
|-------|-------------|
| Explosive Beginning | Asylum quest involving explosive materials |
| The Ghost Haunts at Midnight | Jeanette/Therese mysterious events |
| Spiritual Release | Quest about supernatural events |
| Slashterpiece | Quest involving violent events |
| Bad Blood | Quest about supernatural conflict |
| Sibling Rivalry | Jeanette/Therese sibling dynamic |
| Replanting a Lily | Quest about planting/maintenance |

**Note**: These connections are **external evidence**, not verified in DLG/VMF sources yet.

---

## Incomplete Dialogue Trees

### Jeanette.dlg
- **Record 61, 71, 81**: Not yet examined
- Likely contain deeper dialogue or quest progression

### Therese.dlg
- **Record 61, 71, 81**: Not yet examined
- May contain main Asylum quest dialogue

### Tourette.dlg
- **All records beyond 1**: Not yet examined
- Likely contain quest-related dialogue

### Danielle.dlg
- **All records beyond 1**: Not yet examined
- May contain side interactions

---

## Research Priorities

### P0 - Critical
1. **Examine records 61, 71, 81** in Jeanette.dlg and Therese.dlg
2. **Document full dialogue trees** for all NPCs
3. **Determine Therese personality unlock conditions**
4. **Verify quest connections** to Explosive Beginning, Sibling Rivalry, etc.

### P1 - High
5. **Map `G.Jeanette_Seduce` and `G.Therese_Seduce`** to quest progression
6. **Investigate "Janus" reference** and lore implications
7. **Determine Tourette's role** in Asylum quests
8. **Map `G.Danielle_Know`** to side interactions

### P2 - Medium
9. **Verify club atmosphere** (empty vs. populated)
10. **Investigate "double-cross" reference** in Tourette dialogue
11. **Verify Asylum population** in different game states
12. **Determine police response** when leaving club

---

## Related Files

- `jeanette.dlg` — Jeanette dialogue
- `therese.dlg` — Therese dialogue
- `tourette.dlg` — Tourette dialogue
- `danielle.dlg` — Danielle dialogue
- `santamonica.py` — Global script logic
- `sm_asylum_1.vmf` — Level geometry and triggers
- [[SM-13_Jeanette_Introduction|Jeanette Introduction]]
- [[SM-13_Therese_Introduction|Therese Introduction]]
- [[SM-13_Tourette_Introduction|Tourette Introduction]]
- [[SM-13_Danielle_Introduction|Danielle Introduction]]
- [[SM-13_Asylum_00_Index|Asylum Index]]
- [[SM-13_Asylum_04_Analysis|Asylum Analysis]]

---

## Next Steps

1. **Continue Jeanette.dlg** examination (records 61, 71, 81)
2. **Continue Therese.dlg** examination (records 61, 71, 81)
3. **Examine Tourette.dlg** beyond record 1
4. **Examine Danielle.dlg** beyond record 1
5. **Cross-reference** with `santamonica.py` for quest logic
6. **Verify quest markers** using VMF and DLG analysis

---

**Status**: Research in progress. Priority is to document complete dialogue trees for Asylum NPCs.
