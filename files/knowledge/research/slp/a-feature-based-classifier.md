---
title: "A feature-based classifier"
summary: "§II Annotating Linguistic Structure › Dependency Parsing › Tr: 19.2 • TRANSITION-BASED DEPENDENCY PARSING possible action. The same conditions hold in the next two steps. In step 3, LEFTARC is selected to link the to its head."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "449-449"
---

# A feature-based classifier

§II Annotating Linguistic Structure › Dependency Parsing › Transition-Based Dependency Parsing › A feature-based classifier · pp. 449–449 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
19.2 • TRANSITION-BASED DEPENDENCY PARSING possible action. The same conditions hold in the next two steps. In step 3, LEFTARC is selected to link the to its head. Now consider the situation in Step 4. Stack Word buffer Relations [root, book, flight] [through, Houston] (the ←flight) Here, we might be tempted to add a dependency relation between book and flight, which is present in the reference parse. But doing so now would prevent the later attachment of Houston since flight would have been removed from the stack. Fortunately, the precondition on choosing RIGHTARC prevents this choice and we’re again left with SHIFT as the only viable option. The remaining choices complete the set of operators needed for this example. To recap, we derive appropriate training instances consisting of configurationtransition pairs from a treebank by simulating the operation of a parser in the context of a reference dependency tree. We can deterministically record correct parser actions at each step as we progress through each training example, thereby creating the training set we require. We’ll now introduce two classifiers for choosing transitions, here a classic featurebased algorithm and in the next section a neural classifier using embedding features.

## Key terms
- **feature** — 14 mentions
- **word** — 9 mentions
- **stack** — 8 mentions
- **flight** — 7 mentions
- **buffer** — 6 mentions
- **relation** — 6 mentions
- **training** — 6 mentions
- **dependency** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=449|Speech and Language Processing.pdf p. 449]]

## Liens
- Up: [[research/slp/transition-based-dependency-parsing]]
- ← Prev: [[research/slp/creating-an-oracle]]
- Next: [[research/slp/a-neural-classifier]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
