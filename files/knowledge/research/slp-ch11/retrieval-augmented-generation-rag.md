---
title: "Retrieval-Augmented Generation (RAG)"
summary: "§Retrieval-based Models › Retrieval-Augmented Generation (RAG: 11.3 • INFORMATION RETRIEVAL WITH DENSE VECTORS Query Document … … … … … … s(q,d) MaxSim MaxSim MaxSim ∑ norm norm norm norm norm norm Figure 11.12 A sketch of the ColBERT algorithm at inference time."
level: "research"
series: "SLP Chapter 11 (Standalone Chapter)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, chapter, study-slice, section]
pages: "15-17"
---

# Retrieval-Augmented Generation (RAG)

§Retrieval-based Models › Retrieval-Augmented Generation (RAG) · pp. 15–17 · SLP Chapter 11 (Standalone Chapter)

## Extrait
11.3 • INFORMATION RETRIEVAL WITH DENSE VECTORS Query Document … … … … … … s(q,d) MaxSim MaxSim MaxSim ∑ norm norm norm norm norm norm Figure 11.12 A sketch of the ColBERT algorithm at inference time. The query and document are first passed through separate BERT encoders. Similarity between query and document is computed by summing a soft alignment between the contextual representations of tokens in the query and the document. Training is end-to-end. (Various details aren’t depicted; for example the query is prepended by a [CLS] and [Q:] tokens, and the document by [CLS] and [D:] tokens). Figure adapted from Khattab and Zaharia (2020). chitecture still needs to be trained end-to-end to fine-tune the BERT encoders and train the linear layers (and the special [Q] and [D] embeddings) from scratch. It is trained on triples ⟨q,d+,d−⟩of query q, positive document d+ and negative document d−to produce a score for each document using Eq. 11.19, optimizing model parameters using a cross-entropy loss. All the supervised algorithms (like ColBERT or the full-interaction version of the BERT algorithm applied for reranking) need training data in the form of queries together with relevant and irrelevant passages or documents (positive and negative examples).

## Key terms
- **document** — 23 mentions
- **passage** — 20 mentions
- **prompt** — 13 mentions
- **question** — 13 mentions
- **query** — 12 mentions
- **model** — 12 mentions
- **answer** — 12 mentions
- **generation** — 10 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing Chapter 11.pdf#page=15|Speech and Language Processing Chapter 11.pdf p. 15]]

## Liens
- Up: [[research/slp-ch11/retrieval-based-models]]
- ← Prev: [[research/slp-ch11/information-retrieval-with-dense-vectors]]
- Next: [[research/slp-ch11/datasets]] →
- Document: [[research/slp-chapter-11]]

#nlp #chapter #study-slice #research #section
