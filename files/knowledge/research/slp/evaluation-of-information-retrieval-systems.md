---
title: "Evaluation of Information-Retrieval Systems"
summary: "§I Large Language Models › Retrieval-based Models › Evaluatio: CHAPTER 11 • RETRIEVAL-BASED MODELS Given a list of terms in query, we can very efficiently get lists of all candidate documents, together with the information necessary to compute the tf-idf scores we need."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "252-254"
---

# Evaluation of Information-Retrieval Systems

§I Large Language Models › Retrieval-based Models › Evaluation of Information-Retrieval Systems · pp. 252–254 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 11 • RETRIEVAL-BASED MODELS Given a list of terms in query, we can very efficiently get lists of all candidate documents, together with the information necessary to compute the tf-idf scores we need. We measure the performance of ranked retrieval systems using the same precision and recall metrics we have been using. We make the assumption that each document returned by the IR system is either relevant to our purposes or not relevant. Precision is the fraction of the returned documents that are relevant, and recall is the fraction of all relevant documents that are returned. More formally, let’s assume a system returns T ranked documents in response to an information request, a subset R of these are relevant, a disjoint subset, N, are the remaining irrelevant documents, and U documents in the collection as a whole are relevant to this request. Precision and recall are then defined as: Precision = |R| |T| Recall = |R| |U| (11.13) Unfortunately, these metrics don’t adequately measure the performance of a system that ranks the documents it returns. If we are comparing the performance of two ranked retrieval systems, we need a metric that prefers the one that ranks the relevant documents higher.

## Key terms
- **precision** — 34 mentions
- **recall** — 29 mentions
- **document** — 21 mentions
- **relevant** — 16 mentions
- **system** — 14 mentions
- **value** — 11 mentions
- **curve** — 9 mentions
- **query** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=252|Speech and Language Processing.pdf p. 252]]

## Liens
- Up: [[research/slp/retrieval-based-models]]
- ← Prev: [[research/slp/information-retrieval]]
- Next: [[research/slp/information-retrieval-with-dense-vectors]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
