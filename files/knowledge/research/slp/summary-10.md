---
title: "Summary"
summary: "§I Large Language Models › Retrieval-based Models › Summary: CHAPTER 11 • RETRIEVAL-BASED MODELS document. We sometimes call the task of question answering given one or more documents (for example via RAG), the open book QA task, while the task of anopen book swering directly fro"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "262-262"
---

# Summary

§I Large Language Models › Retrieval-based Models › Summary · pp. 262–262 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 11 • RETRIEVAL-BASED MODELS document. We sometimes call the task of question answering given one or more documents (for example via RAG), the open book QA task, while the task of anopen book swering directly from the LM with no retrieval component at all is the closed book closed book QA task.5 Thus datasets like Natural Questions can be treated as open book if the solver uses each question’s attached document, or closed book if the documents are not used, while datasets like MMLU are solely closed book. Another dimension of variation is the format of the answer: multiple-choice versus freeform. And of course there are variations in prompting, like whether the model is just the question (zero-shot) or also given demonstrations of answers to similar questions (few-shot). MMLU offers both zero-shot and few-shot prompt options. Two techniques are commonly employed to evaluate question-answering systems, with the choice depending on the type of question and QA situation. For multiple choice questions like in MMLU, we report exact match: Exact match: The % of predicted answers that match the gold answer exactly. For questions with free text answers, like Natural Questions, we commonly evaluated with token F1 score to roughly measure the partial string overlap between the answer and the reference answer: F1 score: The average token overlap between predicted and gold answers.

## Key terms
- **question** — 13 mentions
- **document** — 9 mentions
- **retrieval** — 9 mentions
- **book** — 8 mentions
- **answer** — 8 mentions
- **task** — 7 mentions
- **information** — 6 mentions
- **closed** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=262|Speech and Language Processing.pdf p. 262]]

## Liens
- Up: [[research/slp/retrieval-based-models]]
- ← Prev: [[research/slp/evaluating-question-answering]]
- Next: [[research/slp/historical-notes-10]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
