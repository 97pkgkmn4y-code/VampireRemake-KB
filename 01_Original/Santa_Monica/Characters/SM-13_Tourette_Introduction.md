# SM-13 — Tourette Introduction (Asylum)

**Date**: 2026-11-09
**Source**: `tourette.dlg`
**NPC**: Tourette (Asylum)
**Status**: Partial documentation


> Расширенный разбор диалогов и камер: [[SM-13_Asylum_09_Tourette_Dialogue]].
---

## Overview

Tourette is a Therese-voiced entity in The Asylum who appears after certain events (likely related to Jeanette's departure or "death"). The presence of `tourette.dlg` file does not prove existence of separate NPC. VMF note 4: "Nalichie v VMF ne oznachaet odnovremennogo poyavleniya". May have quest connection.

---

## VERIFIED Findings

### Record 1 - Tourette Appears (Therese-Voiced)

**Source**: `tourette.dlg:1`

**Field Mapping**:
- ID: "1"
- Response_1: "[Therese]You! I'm really sorry it had to end this way, I truly am..."
- Response_2: (Identical to Response_1)
- Next ID: "#"
- Conditions: "pc.SetCamera("Tourette") or npc.SetDisposition("apathy",1)"
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Therese-voiced NPC (suggests possession or split personality)
- Apologizes for "something ending" (likely Jeanette departure)
- Sets camera to Tourette
- Sets disposition to "apathy"

---

## INFERRED Findings

### Tourette Identity

**Interpretation**:
- Voiced by Therese, but acts as separate NPC
- Suggests possession or alternate personality
- May be related to Jeanette/Therese dynamic

**Evidence**:
- Speech in brackets: "[Therese]"
- Apologizes for "something ending" (Jeanette)

---

### "Something Ended" Reference

**Interpretation**:
- Likely refers to Jeanette's departure or apparent death
- May be connected to "Explosive Beginning" quest
- Could be part of Therese's guilt or manipulation

**Evidence**:
- Record 1 dialogue: "sorry it had to end this way... never double-crosses me again"

---

### Disposition "Apathy"

**Interpretation**:
- Sets player disposition to "apathy" (indifference)
- May affect player's reaction to Tourette
- Could be Therese's attempt to manipulate player

**Evidence**:
- Field 5: "npc.SetDisposition("apathy",1)"

---

## Unknowns

### What is Tourette's role in Asylum?

- Quest NPC?
- Side character?
- Related to Explosive Beginning or Slashterpiece?

### What happened to Jeanette?

- Did she "die" or leave permanently?
- Is this part of a quest?
- What is the "double-cross" reference?

### How does Tourette relate to Therese?

- Possessed by Therese?
- Separate entity?
- Alternate personality?

### What are subsequent Tourette dialogue records?

- Not yet examined
- Likely contain more context

---

## Research Priorities

1. **P1**: Examine more Tourette dialogue records
2. **P1**: Determine Tourette's role in Asylum quests
3. **P1**: Map Tourette connection to Explosive Beginning/Slashterpiece
4. **P2**: Investigate "double-cross" reference
5. **P2**: Verify Therese/Tourette relationship

---

## Related Files

- `jeanette.dlg` — Jeanette personality dialogue
- `therese.dlg` — Therese personality dialogue
- `danielle.dlg` — Danielle NPC in Asylum
- `santamonica.py` — Global script logic
- `sm_asylum_1.vmf` — Level geometry and triggers
