# SM-13 — Jeanette Introduction (Asylum)

**Date**: 2026-11-09
**Source**: `jeanette.dlg`
**NPC**: Jeanette Voerman (Asylum)
**Status**: Partial documentation


> Расширенный разбор диалогов: [[SM-13_Asylum_08_Jeanette_Dialogue]].
---

## Overview

Jeanette is the first NPC encountered in The Asylum, providing initial lore introduction to the club and its occult atmosphere. Her dialogue establishes the nightclub setting and introduces the player to Jeanette/Therese dual personality dynamic (Malkavian).

---

## VERIFIED Findings

### Record 1 - Initial Encounter

**Source**: `jeanette.dlg:1`

**Field Mapping**:
- ID: "1"
- Response_1: "Oooh, what do we have here? Another scrumptious young plaything... you smell new, little boy..."
- Response_2: "What do we have here? Another scrumptious young plaything... you smell new, little girl..."
- Next ID: "#"
- Conditions: (Empty)
- Scripts: "G.Jeanette_Know = 1"
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Initial greeting when player enters Asylum
- Sets global flag `G.Jeanette_Know = 1` (Jeanette knows player)
- Response_2 addresses "little girl" (female player variant), Response_1 addresses "little boy" (male player variant)

---

### Record 2 - Player Asks "Who are you?"

**Source**: `jeanette.dlg:2`

**Field Mapping**:
- ID: "2"
- Response_1: "Who are you?"
- Response_2: (Female player variant)
- Next ID: "11"
- Conditions: "not IsClan(pc,"Malkavian")"
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Malkavian players get different response (record 11)
- Non-Malkavians hear "Who are you?" response
- Female player variant for Response_2

---

### Record 3 - Player Responds "Frightening isn't the word"

**Source**: `jeanette.dlg:3`

**Field Mapping**:
- ID: "3"
- Response_1: "Frightening isn't the word I'd use... exciting is more like it."
- Response_2: (Female player variant)
- Next ID: "21"
- Conditions: "Seduction 2 & not IsClan(pc,"Malkavian")"
- Scripts: "G.Jeanette_Seduce = G.Jeanette_Seduce + 1"
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Requires Seduction 2 skill
- Increments `G.Jeanette_Seduce` counter
- Leads to record 21
- Female player variant for Response_2

---

### Record 4 - Player Asks "What the hell's your problem?"

**Source**: `jeanette.dlg:4`

**Field Mapping**:
- ID: "4"
- Response_1: "What the hell's your problem?"
- Response_2: (Female player variant)
- Next ID: "41"
- Conditions: "not IsClan(pc,"Malkavian")"
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Non-Malkavian players get this response
- Leads to record 41
- Female player variant for Response_2

---

### Record 5 - Player Says "Leave me alone"

**Source**: `jeanette.dlg:5`

**Field Mapping**:
- ID: "5"
- Response_1: "Leave me alone."
- Response_2: (Female player variant)
- Next ID: "51"
- Conditions: "not IsClan(pc,"Malkavian")"
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Non-Malkavian players get this response
- Leads to record 51
- Female player variant for Response_2

---

### Record 11 - Malkavian-Specific "Who is that girl?"

**Source**: `jeanette.dlg:11`

**Field Mapping**:
- ID: "11"
- Response_1: "I'm the finger down your spine when all the lights are out..."
- Response_2: (Female player variant)
- Next ID: "#"
- Conditions: (Empty)
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Malkavian-specific poetic introduction
- Establishes mystical/occult tone
- Likely leads to Therese personality
- Female player variant for Response_2

---

### Record 21 - "Fire hoses" Metaphor

**Source**: `jeanette.dlg:21`

**Field Mapping**:
- ID: "21"
- Response_1: "[Giggles]I can tell you and I are going to get along just like fire hoses."
- Response_2: (Female player variant)
- Next ID: "#"
- Conditions: (Empty)
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Sets disposition to "Flirt"
- Metaphorical dialogue about passion/intensity
- Female player variant for Response_2

---

### Record 31 - "When we get turned on, there's bound to be flames"

**Source**: `jeanette.dlg:31`

**Field Mapping**:
- ID: "31"
- Response_1: "When we get turned on, there's bound to be flames."
- Response_2: (Female player variant)
- Next ID: "#"
- Conditions: (Empty)
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Continues flame metaphor
- Suggests passion/intensity theme
- Female player variant for Response_2

---

### Record 33 - "Tell me your name"

**Source**: `jeanette.dlg:33`

**Field Mapping**:
- ID: "33"
- Response_1: "That's what I was thinking. What's your name?"
- Response_2: (Female player variant)
- Next ID: "11"
- Conditions: (Empty)
- Scripts: "G.Jeanette_Seduce = G.Jeanette_Seduce + 1"
- Brujah Response: "Burn, baby, burn. Give me the pleasure of your label."
- Malkavian Response: (Empty)

**Meaning**:
- Increments `G.Jeanette_Seduce` counter
- Leads to Malkavian-specific record 11
- Brujah response differs from Malkavian
- Female player variant for Response_2

---

### Record 41 - "Delicious little pancake"

**Source**: `jeanette.dlg:41`

**Field Mapping**:
- ID: "41"
- Response_1: "Oh, I was just thinking about this delicious little pancake who came into my club..."
- Response_2: (Female player variant)
- Next ID: "#"
- Conditions: (Empty)
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Metaphor about player (burnt pancake metaphor)
- Suggests player is "cooked" or "burnt"
- Female player variant for Response_2

---

### Record 43 - "You're insane, you know that?"

**Source**: `jeanette.dlg:43`

**Field Mapping**:
- ID: "43"
- Response_1: "You're insane, you know that?"
- Response_2: (Female player variant)
- Next ID: "61"
- Conditions: "not IsClan(pc,"Malkavian")"
- Scripts: "G.Jeanette_Seduce = G.Jeanette_Seduce - 1"
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Non-Malkavian players get this response
- Decreases `G.Jeanette_Seduce` (player insult)
- Leads to record 61
- Female player variant for Response_2

---

### Record 51 - "Aren't you just the teeniest bit curious?"

**Source**: `jeanette.dlg:51`

**Field Mapping**:
- ID: "51"
- Response_1: "Aren't you just the teeniest bit curious about me? Come on, don't be shy..."
- Response_2: (Female player variant)
- Next ID: "#"
- Conditions: (Empty)
- Scripts: "G.Jeanette_Curious = 1"
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

**Meaning**:
- Sets `G.Jeanette_Curious = 1` flag
- Encourages player to ask about identity
- May unlock Therese dialogue
- Female player variant for Response_2

---

### Record 53 - "Tell me your name" (Therese intro)

**Source**: `jeanette.dlg:53`

**Field Mapping**:
- ID: "53"
- Response_1: "Well, when you put it that way... by all means, tell me your name."
- Response_2: (Female player variant)
- Next ID: "71"
- Conditions: (Empty)
- Scripts: (Empty)
- Brujah Response: "Take the clothes off your name."
- Malkavian Response: (Empty)

**Meaning**:
- Transition to Therese personality
- Leads to record 71
- Female player variant for Response_2

---

### Record 54 - "Leave me alone" (Therese)

**Source**: `jeanette.dlg:54`

**Field Mapping**:
- ID: "54"
- Response_1: "Like I said, leave me alone, I couldn't care less about who you are."
- Response_2: (Female player variant)
- Next ID: "81"
- Conditions: (Empty)
- Scripts: "G.Jeanette_Seduce = G.Jeanette_Seduce - 1"
- Brujah Response: "Even the dead and desperate would pass on your well-used facilities."
- Malkavian Response: (Empty)

**Meaning**:
- Decreases `G.Jeanette_Seduce` counter
- Therese rejects player if seduction is low
- Leads to record 81
- Female player variant for Response_2

---

## INFERRED Findings

### Dual Personality System

**Interpretation**:
- Jeanette and Therese are two personalities of the same body
- Malkavian clan has access to both personalities
- Non-Malkavians see consistent Jeanette personality

**Evidence**:
- Records 2, 3, 4, 5, 42, 43, 44 all lead to Malkavian-specific branches
- Malkavian-specific responses in Jeanette and Therese

---

### Seduction Mechanics

**Interpretation**:
- `G.Jeanette_Seduce` and `G.Therese_Seduce` track player interaction success
- Higher seduction skill improves dialogue outcomes
- Decreases when player is rude or insults Jeanette/Therese

**Evidence**:
- Record 3 requires Seduction 2
- Record 33 increments `G.Jeanette_Seduce`
- Record 43 decreases `G.Jeanette_Seduce` (player insult)
- Record 54 decreases `G.Jeanette_Seduce` (Therese rejection)

---

### Curiosity Mechanic

**Interpretation**:
- `G.Jeanette_Curious = 1` flag tracks player's curiosity
- Set when player asks "Who are you?" (record 51)
- May unlock deeper dialogue or Therese personality

**Evidence**:
- Record 51 sets `G.Jeanette_Curious = 1`

---

### Gender-Neutral Responses

**Interpretation**:
- Jeanette uses gender-neutral language ("little boy/girl")
- Suggests transgender identity or gender-fluid personality
- May affect player perception and dialogue options

**Evidence**:
- Response 1 uses "little boy"
- Response 2 uses "little girl"

---

### "Janus" Reference

**Interpretation**:
- Janus is the Roman two-faced god
- Fits Malkavian theme of duality and split personality
- May be referenced in deeper lore or quest text

**Evidence**:
- Therese.dlg record 2 mentions "dark daughter of Janus"

---

## Unknowns

### What are records 61, 71, 81?

- Not yet examined
- Likely contain deeper dialogue or quest progression
- May lead to main Asylum quest

### What is the "Janus" reference?

- Janus = two-faced god
- May relate to Jeanette/Therese duality
- May be part of quest lore

### How do `G.Jeanette_Seduce` and `G.Therese_Seduce` interact?

- Separate counters for each personality
- May combine for overall relationship score
- May affect Therese personality unlock

### What is the "Explosive Beginning" quest connection?

- Asylum is linked to Explosive Beginning quest
- Need to verify exact connection
- May involve Danielle or other NPCs

---

## Research Priorities

1. **P0**: Examine records 61, 71, 81 (Therese/Quest progression)
2. **P0**: Document full Jeanette dialogue tree
3. **P0**: Determine Therese personality unlock conditions
4. **P1**: Map `G.Jeanette_Seduce` and `G.Therese_Seduce` to quest progression
5. **P1**: Verify connection to Explosive Beginning quest
6. **P2**: Investigate "Janus" reference and lore implications

---

## Related Files

- `therese.dlg` — Therese personality dialogue
- `tourette.dlg` — Tourette entity in Asylum
- `danielle.dlg` — Danielle NPC in Asylum
- `santamonica.py` — Global script logic
- `sm_asylum_1.vmf` — Level geometry and triggers
- [[SM-13_Therese_Introduction|Therese Introduction]]
- [[SM-13_Danielle_Introduction|Danielle Introduction]]
