---
title: "Evaluation of Instruction-Tuned Models"
summary: "§I Large Language Models › Post-training: Instruction Tuning,: 10.1 • INSTRUCTION TUNING Sample Extended Instruction • Definition: This task involves creating answers to complex questions, from a given passage."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "231-231"
---

# Evaluation of Instruction-Tuned Models

§I Large Language Models › Post-training: Instruction Tuning, Alignment, and Test-Time Compute › Instruction Tuning › Evaluation of Instruction-Tuned Models · pp. 231–231 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
10.1 • INSTRUCTION TUNING Sample Extended Instruction • Definition: This task involves creating answers to complex questions, from a given passage. Answering these questions, typically involve understanding multiple sentences. Make sure that your answer has the same type as the ”answer type” mentioned in input. The provided ”answer type” can be of any of the following types: ”span”, ”date”, ”number”. A ”span” answer is a continuous phrase taken directly from the passage or question. You can directly copy-paste the text from the passage or the question for span type answers. If you find multiple spans, please add them all as a comma separated list. Please restrict each span to five words. A ”number” type answer can include a digit specifying an actual value. For ”date” type answers, use DD MM YYYY format e.g. 11 Jan 1992. If full date is not available in the passage you can write partial date such as 1992 or Jan 1992. • Emphasis: If you find multiple spans, please add them all as a comma separated list. Please restrict each span to five words. • Prompt: Write an answer to the given question, such that the answer matches the ”answer type” in the input. Passage: { passage} Question: {…

## Key terms
- **instruction** — 12 mentions
- **answer** — 12 mentions
- **question** — 10 mentions
- **task** — 9 mentions
- **type** — 8 mentions
- **dataset** — 8 mentions
- **model** — 8 mentions
- **span** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=231|Speech and Language Processing.pdf p. 231]]

## Liens
- Up: [[research/slp/instruction-tuning]]
- ← Prev: [[research/slp/instructions-as-training-data]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
