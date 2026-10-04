---
title: "CTC Inference"
summary: "§I Large Language Models › Automatic Speech Recognition › CTC: CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION X (input) A (alignment) Y (output) d x1 i x2 i x3 n x4 n x5 n x6 n x7 e x8 r x9 r x10 r x11 r x12 r x13 r x14 d i n e r wavefile Figure 15.12 A naive algorithm for collapsing "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "364-365"
---

# CTC Inference

§I Large Language Models › Automatic Speech Recognition › CTC › CTC Inference · pp. 364–365 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION X (input) A (alignment) Y (output) d x1 i x2 i x3 n x4 n x5 n x6 n x7 e x8 r x9 r x10 r x11 r x12 r x13 r x14 d i n e r wavefile Figure 15.12 A naive algorithm for collapsing an alignment between input and letters. X (input) A (alignment) remove blanks d x1 i x2 x3 n x4 n x5 x6 n x7 e x8 r x9 r x10 r x11 r x12 x13 x14 d i n e r n merge duplicates d i n e r n Y (output) d i n e r n ␣ ␣ ␣ ␣ ␣ ␣␣ Figure 15.13 The CTC collapsing function B, showing the space blank character ; repeated (consecutive) characters in an alignment A are removed to form the output Y. The CTC collapsing function is many-to-one; lots of different alignments map to the same output string. For example, the alignment shown in Fig. 15.13 is not the only alignment that results in the string dinner. Fig. 15.14 shows some other alignments that would produce the same output. d i n n n e e e r r r ␣ ␣ d d i n n n e r r ␣ ␣␣ d d d i n n n e r r ␣ i ␣ ␣ ␣␣␣ Figure 15.14 Three other legitimate alignments producing the transcript dinner. It’s useful to think of the set of all alignments that might produce the same output Y. We’ll use the inverse of our B function, called B−1, and represent that set as B−1(Y).

## Key terms
- **alignment** — 25 mentions
- **output** — 18 mentions
- **input** — 7 mentions
- **string** — 7 mentions
- **time** — 6 mentions
- **sequence** — 5 mentions
- **probable** — 5 mentions
- **collapsing** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=364|Speech and Language Processing.pdf p. 364]]

## Liens
- Up: [[research/slp/ctc]]
- Next: [[research/slp/ctc-training]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
