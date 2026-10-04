---
title: "Advanced Methods in Transition-Based Parsing"
summary: "§II Annotating Linguistic Structure › Dependency Parsing › Tr: 19.2 • TRANSITION-BASED DEPENDENCY PARSING The basic transition-based approach can be elaborated in a number of ways to improve performance by addressing some of the most obvious flaws in the approach."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "451-452"
---

# Advanced Methods in Transition-Based Parsing

§II Annotating Linguistic Structure › Dependency Parsing › Transition-Based Dependency Parsing › Advanced Methods in Transition-Based Parsing · pp. 451–452 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
19.2 • TRANSITION-BASED DEPENDENCY PARSING The basic transition-based approach can be elaborated in a number of ways to improve performance by addressing some of the most obvious flaws in the approach. Alternative Transition Systems The arc-standard transition system described above is only one of many possible systems. A frequently used alternative is the arc eager transition system. The arc eager arc eager approach gets its name from its ability to assert rightward relations much sooner than in the arc standard approach. To see this, let’s revisit the arc standard trace of Example 19.9, repeated here. Book the flight through Houston obj det nmod case root Consider the dependency relation between book and flight in this analysis. As is shown in Fig. 19.7, an arc-standard approach would assert this relation at Step 8, despite the fact that book and flight first come together on the stack much earlier at Step 4. The reason this relation can’t be captured at this point is due to the presence of the postnominal modifier through Houston. In an arc-standard approach, dependents are removed from the stack as soon as they are assigned their heads. If flight had been assigned book as its head in Step 4, it would no longer be available to serve as the head of Houston.

## Key terms
- **book** — 17 mentions
- **flight** — 17 mentions
- **houston** — 14 mentions
- **through** — 13 mentions
- **root** — 13 mentions
- **stack** — 13 mentions
- **word** — 12 mentions
- **beam** — 11 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=451|Speech and Language Processing.pdf p. 451]]

## Liens
- Up: [[research/slp/transition-based-dependency-parsing]]
- ← Prev: [[research/slp/a-neural-classifier]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
