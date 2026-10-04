---
title: "Named Entities"
summary: "§I Large Language Models › Masked Language Models › Fine-Tuni: 9.5 • FINE-TUNING FOR SEQUENCE LABELING: NAMED ENTITY RECOGNITION describe a relationship between the meaning of the first sentence (the premise) and the meaning of the second sentence (the hypothesis)."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "221-221"
---

# Named Entities

§I Large Language Models › Masked Language Models › Fine-Tuning for Sequence Labeling: Named Entity Recognition › Named Entities · pp. 221–221 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
9.5 • FINE-TUNING FOR SEQUENCE LABELING: NAMED ENTITY RECOGNITION describe a relationship between the meaning of the first sentence (the premise) and the meaning of the second sentence (the hypothesis). Here are representative examples of each class from the corpus: • Neutral a: Jon walked back to the town to the smithy. b: Jon traveled back to his hometown. • Contradicts a: Tourist Information offices can be very helpful. b: Tourist Information offices are never of any help. • Entails a: I’m confused. b: Not all of it is very clear to me. A relationship of contradicts means that the premise contradicts the hypothesis; entails means that the premise entails the hypothesis; neutral means that neither is necessarily true. The meaning of these labels is looser than strict logical entailment or contradiction indicating that a typical human reading the sentences would most likely interpret the meanings in this way. To finetune a classifier for the MultiNLI task, we pass the premise/hypothesis pairs through a bidirectional encoder as described above and use the output vector for the [CLS] token as the input to the classification head. As with ordinary sequence classification, this head provides the input to a three-way classifier that can be trained on the MultiNLI training corpus.

## Key terms
- **entity** — 11 mentions
- **named** — 8 mentions
- **sequence** — 6 mentions
- **recognition** — 5 mentions
- **labeling** — 4 mentions
- **meaning** — 4 mentions
- **premise** — 4 mentions
- **hypothesis** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=221|Speech and Language Processing.pdf p. 221]]

## Liens
- Up: [[research/slp/fine-tuning-for-sequence-labeling-named-entity-recognition]]
- Next: [[research/slp/bio-tagging]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
