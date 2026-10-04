---
title: "Part 7 (pp. 49–56)"
summary: "§Part 7 (pp. 49–56): component in the pipeline that assigns scores. This mode doesn’t influence document scores. merge Merges lists of documents and sorts them by score."
level: "research"
series: "RAG in Production with Haystack (Technical Guide)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [rag, retrieval, production, haystack, section]
pages: "49-56"
---

# Part 7 (pp. 49–56)

§Part 7 (pp. 49–56) · pp. 49–56 · RAG in Production with Haystack (Technical Guide)

## Extrait
component in the pipeline that assigns scores. This mode doesn’t influence document scores. merge Merges lists of documents and sorts them by score. For dupli‐ cate documents, you can also assign a weight to the scores to influence how they’re merged. reciprocal_rank_fusion Combines documents based on their ranking received from multiple components. If the same document appears in more than one list (was returned by multiple components), it gets a higher score. distribution_based_rank_fusion Combines rankings from multiple sources into a single, unified ranking. It analyzes how scores are spread out and normalizes them, ensuring that each component’s scoring method is taken into account. This normalization helps to balance the influence of each component, resulting in a more robust and fair com‐ bined ranking. If a document appears in multiple lists, its final score is adjusted based on the distribution of scores from all lists. Let’s look at how to use Haystack pipelines to create a hybrid retriever and a reranker to rank the documents for relevancy using the results from both the embedding and keyword retrievers. Let’s keep using the same NVIDIA 10-Q document we have dis‐ cussed in the basic pipeline for document QA.

## Key terms
- **document** — 70 mentions
- **retrieval** — 31 mentions
- **component** — 30 mentions
- **pipeline** — 29 mentions
- **hybrid** — 22 mentions
- **embedding** — 21 mentions
- **query** — 17 mentions
- **builder** — 15 mentions

## Practice — open in app
- [[pdf:Retrieval-Augmented.pdf#page=49|Retrieval-Augmented.pdf p. 49]]

## Liens
- ← Prev: [[research/rag-haystack/part-6-pp-41-48]]
- Next: [[research/rag-haystack/part-8-pp-57-64]] →
- Document: [[research/rag-haystack-guide]]

#rag #retrieval #production #haystack #research #section
