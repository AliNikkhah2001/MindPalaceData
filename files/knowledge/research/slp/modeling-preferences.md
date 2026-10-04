---
title: "Modeling Preferences"
summary: "§I Large Language Models › Post-training: Instruction Tuning,: CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE Finally, an alternative to discrete preferences are scalar judgments over distinct dimensions, or aspects, of system outputs."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "234-234"
---

# Modeling Preferences

§I Large Language Models › Post-training: Instruction Tuning, Alignment, and Test-Time Compute › Learning from Preferences › Modeling Preferences · pp. 234–234 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE Finally, an alternative to discrete preferences are scalar judgments over distinct dimensions, or aspects, of system outputs. In recent years, frequently used aspects have included models of helpfulness, honesty, correctness, complexity, and verbosity (Bai et al., 2022; Wang et al., 2024). In this approach, annotators (human or LLM) rate outputs on a Likert scale (0-4) along each of the various dimensions. Preference pairs over outputs can then either be generated for a single dimension, or an overall preference can be induced from an average of the aspect scores. Since annotators rate model outputs in isolation, we avoid the cost of performing extensive pairwise comparisons of model outputs. Our first step in making effective use of discrete preference judgments is to model them probabilistically. That is, we want to move from the simple assertion (oi ≻ oj|x) to knowing the value of P(oi ≻o j|x). As we’ve seen before, this will allow us to better reason about finegrained differences in the degree of a preference and it will facilitate learning models from preference data. Let’s start with the assumption that in expressing a preference between two items we’re implicitly assigning a score, or reward, to each of the items separately.

## Key terms
- **preference** — 10 mentions
- **model** — 8 mentions
- **score** — 8 mentions
- **outputs** — 6 mentions
- **logistic** — 5 mentions
- **difference** — 5 mentions
- **approach** — 4 mentions
- **items** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=234|Speech and Language Processing.pdf p. 234]]

## Liens
- Up: [[research/slp/learning-from-preferences]]
- ← Prev: [[research/slp/llm-preference-data]]
- Next: [[research/slp/learning-to-score-preferences]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
