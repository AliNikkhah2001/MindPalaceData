---
title: "Part 5 (pp. 33–40)"
summary: "§Part 5 (pp. 33–40): quality, but they also increase storage requirements and com‐ putational costs. Many embedding models offer a “quantized” option, allowing us to use a smaller model with minimal quality loss."
level: "research"
series: "RAG in Production with Haystack (Technical Guide)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [rag, retrieval, production, haystack, section]
pages: "33-40"
---

# Part 5 (pp. 33–40)

§Part 5 (pp. 33–40) · pp. 33–40 · RAG in Production with Haystack (Technical Guide)

## Extrait
quality, but they also increase storage requirements and com‐ putational costs. Many embedding models offer a “quantized” option, allowing us to use a smaller model with minimal quality loss. Step 4: Database Vector databases are specialized systems designed to store, index, and retrieve vector embeddings efficiently. These embed‐ dings are numerical representations of data that capture seman‐ tic meaning, allowing for similarity-based searches. These rely on approximate nearest neighbor (ANN) algorithms to locate the closest vectors, ensuring low latency in query responses. Examples include open-source options like Qdrant, Chroma, Milvus, Redis, Weaviate, and pgvector, as well as closed-source platforms like Pinecone and Databricks Vector Search. Step 5: Retrieval Recently, there have been multiple innovations in retrieval, including reranking, hybrid search, query rewriting, and more. We will discuss how these techniques allow us to make a cal‐ culated trade-off between execution time and quality of the retrieval results. Step 6: Generation Generation is crucial for RAG systems as this is the core of the system’s ability to process and produce human-like responses. The LLM serves as the foundation for understand‐ ing and interpreting the retrieved information, leveraging its vast knowledge to contextualize and synthesize the data.

## Key terms
- **document** — 25 mentions
- **model** — 18 mentions
- **score** — 17 mentions
- **chunk** — 17 mentions
- **ground-truth** — 15 mentions
- **response** — 15 mentions
- **chunking** — 14 mentions
- **embedding** — 13 mentions

## Practice — open in app
- [[pdf:Retrieval-Augmented.pdf#page=33|Retrieval-Augmented.pdf p. 33]]

## Liens
- ← Prev: [[research/rag-haystack/part-4-pp-25-32]]
- Next: [[research/rag-haystack/part-6-pp-41-48]] →
- Document: [[research/rag-haystack-guide]]

#rag #retrieval #production #haystack #research #section
