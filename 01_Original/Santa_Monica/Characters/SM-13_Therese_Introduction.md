# SM-13 — Therese Introduction (Asylum)

**Date**: 2026-11-09
**Source**: `therese.dlg`
**NPC**: Therese Voerman (Asylum)
**Status**: Partial documentation


> Расширенный разбор диалогов: [[SM-13_Asylum_07_Therese_Dialogue]].
---

## Overview

Therese is the composed, serious personality of the Voerman sisters in The Asylum. She provides the "serious" side of the Malkavian split personality dynamic, contrasting with Jeanette's flamboyant behavior.

---

## VERIFIED Findings

### Record 1 - Therese Enters (Initial)

**Source**: `therese.dlg:1`

**Field Mapping**:
- ID: "1"
- Response_1: "Please, come in. I do apologize for my sister's crassness..."
- Response_2: (Male player variant)
- Next ID: "#"
- Conditions: "npc.SetDisposition("Neutral",1)"
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Sets disposition to "Neutral" when Therese appears
- Apologizes for Jeanette's behavior
- Establishes serious, composed tone
- Male player variant for Response_2

---

### Record 2 - "Are you Therese?"

**Source**: `therese.dlg:2`

**Field Mapping**:
- ID: "2"
- Response_1: "If you say so. I guess that means you're Therese?"
- Response_2: (Male player variant)
- Next ID: "61"
- Conditions: (Empty)
- Scripts: (Empty)
- Brujah Response: "Are you Therese? The dark daughter of Janus?"
- Malkavian Response: (Empty)

**Meaning**:
- Confirms Therese identity
- Leads to record 61
- Male player variant for Response_2

---

### Record 3 - "I'm just glad she's gone"

**Source**: `therese.dlg:3`

**Field Mapping**:
- ID: "3"
- Response_1: "I'm just glad she's gone. You are Therese?"
- Response_2: (Identical to Response_1)
- Next ID: "61"
- Conditions: (Empty)
- Scripts: "G.Therese_Seduce = G.Therese_Seduce + 1"
- Brujah Response: "I could stomach her oozings no longer. You are Therese, the dark daughter?"
- Malkavian Response: (Empty)

**Meaning**:
- Increments `G.Therese_Seduce` counter
- Expresses relief that Jeanette is gone
- Leads to record 61

---

### Record 4 - "Jeanette? She was no trouble"

**Source**: `therese.dlg:4`

**Field Mapping**:
- ID: "4"
- Response_1: "Jeanette? She was no trouble."
- Response_2: (Identical to Response_1)
- Next ID: "11"
- Conditions: (Empty)
- Scripts: (Empty)
- Brujah Response: "Her whiteness was no terrible weight."
- Malkavian Response: (Empty)

**Meaning**:
- Refers to Jeanette by name
- Suggests Jeanette wasn't a major issue
- Leads to Malkavian-specific record 11

---

### Record 5 - "Where is she?"

**Source**: `therese.dlg:5`

**Field Mapping**:
- ID: "5"
- Response_1: "Where is she?"
- Response_2: (Identical to Response_1)
- Next ID: "21"
- Conditions: (Empty)
- Scripts: (Empty)
- Brujah Response: "Where is the ivory princess?"
- Malkavian Response: (Empty)

**Meaning**:
- Asks about Jeanette's whereabouts
- Leads to record 21

---

### Record 11 - Malkavian-Specific "Her whiteness was no terrible weight"

**Source**: `therese.dlg:11`

**Field Mapping**:
- ID: "11"
- Response_1: (Implied)
- Response_2: (Identical to Response_1)
- Next ID: "#"
- Conditions: (Empty)
- Scripts: (Empty)
- Brujah Response: "Her whiteness was no terrible weight."
- Malkavian Response: (Empty)

**Meaning**:
- Malkavian-specific response
- Poetic reference to Jeanette
- Likely part of deeper lore

---

### Record 21 - "Where is the ivory princess?"

**Source**: `therese.dlg:21`

**Field Mapping**:
- ID: "21"
- Response_1: (Implied)
- Response_2: (Identical to Response_1)
- Next ID: "#"
- Conditions: (Empty)
- Scripts: (Empty)
- Brujah Response: "Where is the ivory princess?"
- Malkavian Response: (Empty)

**Meaning**:
- Poetic question about Jeanette
- "Ivory princess" metaphor
- Further lore about sisters

---

## INFERRED Findings

### Seduction Mechanics

**Interpretation**:
- `G.Therese_Seduce` tracks player interaction success with Therese
- Similar to `G.Jeanette_Seduce` but for Therese personality
- May affect quest progression or relationship

**Evidence**:
- Record 3 increments `G.Therese_Seduce`

---

### Personality Contrast

**Interpretation**:
- Therese represents the composed, serious side
- Jeanette represents the chaotic, flamboyant side
- Player's interaction style affects both personalities

**Evidence**:
- Therese disposition is "Neutral"
- Jeanette disposition is "Flirt" or varies
- Separate dialogue trees for each personality

---

### Janus Reference

**Interpretation**:
- Janus is the Roman two-faced god
- Fits Malkavian theme of duality
- May relate to Jeanette/Therese split personality

**Evidence**:
- Therese.dlg record 2 mentions "dark daughter of Janus"
- Record 11 and 21 have poetic Malkavian-specific responses

---

## Unknowns

### What are records 61, 71, 81?

- Not yet examined
- Likely contain deeper dialogue or quest progression
- May lead to main Asylum quest

### How do `G.Jeanette_Seduce` and `G.Therese_Seduce` interact?

- Separate counters for each personality
- May combine for overall relationship score
- May affect Therese personality unlock

### What is the "dark daughter of Janus"?

- Janus = two-faced god
- May relate to sister duality
- May be part of quest lore

### What is the connection to Asylum quests?

- Explosive Beginning, Slashterpiece, Sibling Rivalry
- Need to verify exact NPC/diologue connections
- May involve Jeanette/Therese personality unlock

---

## Research Priorities

1. **P0**: Examine records 61, 71, 81 (Therese/Quest progression)
2. **P0**: Document full Therese dialogue tree
3. **P1**: Determine connection to `G.Jeanette_Seduce` and `G.Therese_Seduce`
4. **P1**: Map Therese to Asylum quest progression
5. **P2**: Verify Therese/Quest connection to Asylum quest markers
6. **P2**: Investigate "Janus" reference and lore implications

---

## Related Files

- `jeanette.dlg` — Jeanette personality dialogue
- `tourette.dlg` — Tourette entity in Asylum
- `danielle.dlg` — Danielle NPC in Asylum
- `santamonica.py` — Global script logic
- `sm_asylum_1.vmf` — Level geometry and triggers
- [[SM-13_Jeanette_Introduction|Jeanette Introduction]]
