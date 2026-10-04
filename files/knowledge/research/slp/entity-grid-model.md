---
title: "Entity Grid model"
summary: "§II Annotating Linguistic Structure › Discourse Coherence › C: CHAPTER 24 • DISCOURSE COHERENCE entity. In a RETAIN relation, the speaker intends to SHIFT to a new entity in a future utterance and meanwhile places the current entity in a lower rank Cf ."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "570-571"
---

# Entity Grid model

§II Annotating Linguistic Structure › Discourse Coherence › Centering and Entity-Based Coherence › Entity Grid model · pp. 570–571 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 24 • DISCOURSE COHERENCE entity. In a RETAIN relation, the speaker intends to SHIFT to a new entity in a future utterance and meanwhile places the current entity in a lower rank Cf . In a SHIFT relation, the speaker is shifting to a new salient entity. Let’s walk though the start of (24.28) again, repeated as (24.30), showing the representations after each utterance is processed. (24.30) John went to his favorite music store to buy a piano. (U1) He was excited that he could finally buy a piano. (U2) He arrived just as the store was closing for the day. (U3) It was closing just as John arrived (U4) Using the grammatical role hierarchy to order the Cf , for sentence U1 we get: Cf (U1): {John, music store, piano} Cp(U1): John Cb(U1): undefined and then for sentence U2: Cf (U2): {John, piano} Cp(U2): John Cb(U2): John Result: Continue (Cp(U2)=Cb(U2); Cb(U1) undefined) The transition from U1 to U2 is thus a CONTINUE. Completing this example is left as exercise (1) for the reader Centering embodies a particular theory of how entity mentioning leads to coherence: that salient entities appear in subject position or are pronominalized, and that discourses are salient by means of continuing to mention the same entity in such ways.

## Key terms
- **entity** — 21 mentions
- **sentence** — 14 mentions
- **grid** — 10 mentions
- **transition** — 9 mentions
- **entities** — 9 mentions
- **appear** — 8 mentions
- **model** — 8 mentions
- **column** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=570|Speech and Language Processing.pdf p. 570]]

## Liens
- Up: [[research/slp/centering-and-entity-based-coherence]]
- ← Prev: [[research/slp/centering]]
- Next: [[research/slp/evaluating-neural-and-entity-based-coherence]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
