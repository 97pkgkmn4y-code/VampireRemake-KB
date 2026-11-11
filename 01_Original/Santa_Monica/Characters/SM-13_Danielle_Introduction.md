# SM-13 — Danielle Introduction (Asylum)

**Date**: 2026-11-09
**Source**: `danielle.dlg`
**NPC**: Danielle (Asylum)
**Status**: Partial documentation


> В текущей структуре найдено только это частичное Introduction-исследование Danielle; см. [[Index]] и [[../Locations/asylum1/SM-13_Asylum_00_Index]].
---

## Overview

Danielle is a visitor in The Asylum, likely a customer or potential client. She provides early context about the club's atmosphere and may be involved in side interactions.

---

## VERIFIED Findings

### Record 1 - Initial Greeting

**Source**: `danielle.dlg:1`

**Field Mapping**:
- ID: "1"
- Response_1: "Sheesh, is this place always so dead?"
- Response_2: (Gender-neutral alternative)
- Next ID: "#"
- Conditions: "npc.SetDisposition("Neutral", 1)"
- Scripts: "G.Danielle_Know = 1"
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Sets disposition to "Neutral"
- Sets global flag `G.Danielle_Know = 1` (Danielle knows player)
- Asks about club atmosphere (suggests empty/negative vibe)

---

## Related Files

- `jeanette.dlg` — Jeanette personality dialogue
- `therese.dlg` — Therese personality dialogue
- `tourette.dlg` — Tourette NPC in Asylum
- `santamonica.py` — Global script logic
- `sm_asylum_1.vmf` — Level geometry and triggers


### Club Atmosphere

**Interpretation**:
- "This place always so dead?" suggests low patronage
- May indicate early-game state where Asylum isn't fully populated
- Could affect player perception of Asylum as a viable venue

**Evidence**:
- Record 1 dialogue reflects low activity

---

### Danielle Role

**Interpretation**:
- Likely a regular customer or potential client
- May have side quests or business interactions
- Could be related to "Explosive Beginning" quest

**Evidence**:
- First dialogue record suggests initial encounter
- Sets tracking flag for subsequent interactions

---

## Related Files

- `jeanette.dlg` — Jeanette personality dialogue
- `therese.dlg` — Therese personality dialogue
- `tourette.dlg` — Tourette NPC in Asylum
- `santamonica.py` — Global script logic
- `sm_asylum_1.vmf` — Level geometry and triggers
