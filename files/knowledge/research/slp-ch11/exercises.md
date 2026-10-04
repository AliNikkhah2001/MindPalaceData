---
title: "Exercises"
summary: "§Retrieval-based Models › Exercises: CHAPTER 11 • RETRIEVAL-BASED MODELS swering directly from the LM with no retrieval component at all is the closed book closed book QA task.5 Thus datasets like Natural Questions can be treated as open book if the solver uses each question’s at"
level: "research"
series: "SLP Chapter 11 (Standalone Chapter)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, chapter, study-slice, section]
pages: "20-25"
---

# Exercises

§Retrieval-based Models › Exercises · pp. 20–25 · SLP Chapter 11 (Standalone Chapter)

## Extrait
CHAPTER 11 • RETRIEVAL-BASED MODELS swering directly from the LM with no retrieval component at all is the closed book closed book QA task.5 Thus datasets like Natural Questions can be treated as open book if the solver uses each question’s attached document, or closed book if the documents are not used, while datasets like MMLU are solely closed book. Another dimension of variation is the format of the answer: multiple-choice versus freeform. And of course there are variations in prompting, like whether the model is just the question (zero-shot) or also given demonstrations of answers to similar questions (few-shot). MMLU offers both zero-shot and few-shot prompt options. Two techniques are commonly employed to evaluate question-answering systems, with the choice depending on the type of question and QA situation. For multiple choice questions like in MMLU, we report exact match: Exact match: The % of predicted answers that match the gold answer exactly. For questions with free text answers, like Natural Questions, we commonly evaluated with token F1 score to roughly measure the partial string overlap between the answer and the reference answer: F1 score: The average token overlap between predicted and gold answers.

## Key terms
- **question** — 35 mentions
- **answer** — 21 mentions
- **retrieval** — 18 mentions
- **system** — 18 mentions
- **document** — 13 mentions
- **answering** — 10 mentions
- **model** — 9 mentions
- **task** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing Chapter 11.pdf#page=20|Speech and Language Processing Chapter 11.pdf p. 20]]

## Liens
- Up: [[research/slp-ch11/retrieval-based-models]]
- ← Prev: [[research/slp-ch11/historical-notes]]
- Document: [[research/slp-chapter-11]]

#nlp #chapter #study-slice #research #section
