# Santa Monica - Arthur Dialogue Records

## Overview

This document collects dialogue records from arthur.dlg where Arthur discusses Santa Monica locations, operations, and related topics. These are dialogue records, not a separate quest.

## VERIFIED Findings

### Record 31
- ID: 31
- Response 1: I got to have a few other bondsmen to keep the place open 24 hours. Plus a bounty hunter. I pull the graveyard shift cuz that's when all the crazy stuff happens in Santa Monica.
- Next ID: "#"
- Conditions: "npc.SetDisposition(\"Neutral\",1)"
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

### Record 33
- ID: 33
- Response 1: Santa Monica doesn't sound like a good place to be living.
- Response 2: Santa Monica doesn't sound like a good place to be living.
- Next ID: "41"
- Conditions: "G.Arthur_BJ == 0 and not IsClan(pc,"Malkavian")"
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

### Record 41
- ID: 41
- Response_1: (Santa Monica discussion)
- Response_2: (Santa Monica discussion)
- Next ID: "#"
- Conditions: "npc.SetDisposition(\"Neutral\",1); G.Arthur_BJ = 1"
- Scripts: (Empty)
- Brujah Response: (Empty)
- Malkavian Response: (Empty)

### Record 42
- ID: 42
- Response_1: (Santa Monica discussion)
- Response_2: (Santa Monica discussion)
- Next ID: "61"
- Conditions: "G.Arthur_SM == 0"
- Scripts: (Empty)
- Brujah Response: "The lady's beauty has faded?"
- Malkavian Response: "The lady's beauty has faded?"

### Record 82
- ID: 82
- Response_1: (Santa Monica discussion)
- Response_2: (Santa Monica discussion)
- Next ID: "61"
- Conditions: "G.Arthur_BJ == 1 and G.Arthur_BH >= 1 and G.Arthur_SM == 0"
- Scripts: (Empty)
- Brujah Response: "The lady by the sea is drowning, is she not?"
- Malkavian Response: "The lady by the sea is drowning, is she not?"

### Record 441
- ID: 441
- Response 1: Most recently he was brought in as part of a big case on stolen auto parts. It's this big chop shop thing that's goin on in Santa Monica. Been in the paper.
- Condition: #

### Record 543
- ID: 543
- Response 1: How do you like Santa Monica?
- Condition: 41
- Variable: #

### Record 544
- ID: 544
- Response 1: Santa Monica looks like it's seen better times.
- Condition: 61
- Variable: #

### Record 571
- ID: 571
- Response 1: Huh? Oh! I see what you're yappin' about. Yeah...I guess you could call it that. Key master, huh? Might be worth tryin'...Arthur Kilpatrick: The Santa Monica Key Master! Ehh...I don't know. It kinda sounds like a bad horror movie...
- Condition: #

### Record 581
- ID: 581
- Response 1: You mean Santa Monica? You sure got a strange way a' sayin' things. This old burg has gone downhill in the past few years if you ask me. Lots of shady types movin' in. Which ain't bad for business, you know what I mean?
- Condition: #
- Variable: npc.SetDisposition("Neutral",1)

### Record 691
- ID: 691
- Response 1: Great! I suppose the first place you should look is his apartment at the Santa Monica Suites - apartment one, I think it is. Maybe you'll find something there to let you know where he's got himself to. Here's a key card that'll let you in.
- Condition: #
- Variable: npc.SetDisposition("Neutral",1)
- Field 7: G.Arthur_Knox = 2; pc.SetQuest("Arthur Knox", 1); pc.GiveItem("item_k_carson_apartment_key")

## INFERRED Findings

### Quest Variables
- G.Arthur_Knox = 2: dialogue global written at ID 691; its exact runtime meaning is UNVERIFIED.
- pc.SetQuest("Arthur Knox", 1): Quest "Arthur Knox" set to state 1 (in progress)
- pc.GiveItem("item_k_carson_apartment_key"): Key card for apartment
- G.Arthur_BJ is written in arthur.dlg IDs 41 and 741. The separate journal Bail Jumper starts at ID 331 with pc.SetQuest("Bail Jumper", 1).

### Quest Structure
1. Arthur mentions Santa Monica multiple times
2. Arthur reveals he knows about "The Santa Monica Key Master"
3. Arthur gives player key card for apartment
4. Quest "Arthur Knox" is triggered

## UNKNOWN Findings
- What is the "Santa Monica Key Master"?
- Who is the "he" in Record 441 (chop shop case)?
- What are the other quest branches not yet documented?
