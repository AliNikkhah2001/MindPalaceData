---
title: "Part 3 (pp. 17–24)"
summary: "§Part 3 (pp. 17–24): can find multiple good choices with at least 90% of the quality of the leading models but at a fraction of the size. Making the right choice is an important design consideration, as retrieval depends on which embedding model you choose."
level: "research"
series: "RAG in Production with Haystack (Technical Guide)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [rag, retrieval, production, haystack, section]
pages: "17-24"
---

# Part 3 (pp. 17–24)

§Part 3 (pp. 17–24) · pp. 17–24 · RAG in Production with Haystack (Technical Guide)

## Extrait
can find multiple good choices with at least 90% of the quality of the leading models but at a fraction of the size. Making the right choice is an important design consideration, as retrieval depends on which embedding model you choose. What this means is that if you decide to make the switch to another embedding model, say a year down the line, you will need to reindex the previously embedded data, which could be expensive and time-consuming. This remains an unsolved problem. Storing Data Storing document embeddings or documents in the right format is key to quality and latency. Typical SQL databases like PostgreSQL, MySQL, and so forth are good for handling text documents. While these can also store embeddings as strings, a new type of data‐ base, a vector database (DB), has emerged that is specifically built for indexing and storing vector embeddings. Vector DBs make fixed-dimension-related tasks like computing cosine similarity and clustering faster. This paradigm has become so popular that Post‐ greSQL, a traditional SQL database, now includes a vector exten‐ sion, called pgvector. Common vector DBs supported by Haystack include Elasticsearch and OpenSearch. Haystack supports multiple vector and non-vector document stores.

## Key terms
- **document** — 41 mentions
- **haystack** — 21 mentions
- **pipeline** — 20 mentions
- **data** — 19 mentions
- **component** — 18 mentions
- **prompt** — 15 mentions
- **application** — 14 mentions
- **retriever** — 13 mentions

## Practice — open in app
- [[pdf:Retrieval-Augmented.pdf#page=17|Retrieval-Augmented.pdf p. 17]]

## Liens
- ← Prev: [[research/rag-haystack/part-2-pp-9-16]]
- Next: [[research/rag-haystack/part-4-pp-25-32]] →
- Document: [[research/rag-haystack-guide]]

#rag #retrieval #production #haystack #research #section
