---
title: "Datasets"
summary: "§I Large Language Models › Retrieval-based Models › Datasets: CHAPTER 11 • RETRIEVAL-BASED MODELS trained, or if it was, it was likely trained for simple IR or factoid question-answering tasks, not for the RAG scenario where the retrieved passages are specifically to be used by a"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "260-261"
---

# Datasets

§I Large Language Models › Retrieval-based Models › Datasets · pp. 260–261 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 11 • RETRIEVAL-BASED MODELS trained, or if it was, it was likely trained for simple IR or factoid question-answering tasks, not for the RAG scenario where the retrieved passages are specifically to be used by another LLM for generating texts. We can address this mismatch for trainable IR algorithms by doing end-to-end training of the entire architecture on some set of questions and answers, training the parameters of the IR model as well as the LLM. Finally, it is generally useful for LLMs to give the user evidence for any factual statement. This can be in the form of knowledge citations, such as URLs of a knowledge citations trusted source or citation references to particular literature. For example a question answering system might generate numbered pointers to URLs as follows: Q: Which films have Gong Li as a member of their cast? A: The Story of Qiu Ju [1], Farewell My Concubine [2], The Monkey King 2 [3], Mulan [3], Saturday Fiction [3] ... The simplest way for generating knowledge citations is to specify it as part of the prompt. For example Gao et al. (2023) employ a prompt with text like: ‘‘Write an answer for the given question using only the provided search results (some of which might be irrelevant) and cite them properly...

## Key terms
- **question** — 22 mentions
- **answer** — 16 mentions
- **dataset** — 13 mentions
- **atom** — 8 mentions
- **human** — 7 mentions
- **natural** — 6 mentions
- **passage** — 6 mentions
- **knowledge** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=260|Speech and Language Processing.pdf p. 260]]

## Liens
- Up: [[research/slp/retrieval-based-models]]
- ← Prev: [[research/slp/retrieval-augmented-generation-rag]]
- Next: [[research/slp/evaluating-question-answering]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
