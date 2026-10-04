---
title: "Document Scoring"
summary: "§Retrieval-based Models › Information Retrieval › Document Sc: 11.1 • INFORMATION RETRIEVAL Once we have represented each document and query as a weighted vector, we need to score each document."
level: "research"
series: "SLP Chapter 11 (Standalone Chapter)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, chapter, study-slice, section]
pages: "7-8"
---

# Document Scoring

§Retrieval-based Models › Information Retrieval › Document Scoring · pp. 7–8 · SLP Chapter 11 (Standalone Chapter)

## Extrait
11.1 • INFORMATION RETRIEVAL Once we have represented each document and query as a weighted vector, we need to score each document. Our goal is to measure the relevance of the document to the user’s information need, as expressed in their query. In the classic tf-idf model we estimate this relevance of a document by measuring its geometric similarity in vector space to the query. That is, we make the simplifying assumption that documents that have similar words to the query are more relevant to the user. We use the cosine similarity function introduced in Chapter 5, scoring document d by the cosine of its vector d with the query vector q: score(q,d) = cos(q,d) = q·d |q||d| (11.7) Another way to think of the cosine computation is as the dot product of unit vectors; we can first normalize both the query and document vector to unit vectors, by dividing by their lengths, and then take the dot product: score(q,d) = cos(q,d) = q |q| · d |d| (11.8) We can spell out Eq. 11.8, using the tf-idf values and spelling out the dot product as a sum of products: score(q,d) = X t∈q tf-idf(t,q) qP qi∈q tf-idf 2(qi,q) · tf-idf(t,d) qP di∈d tf-idf 2(di,d) (11.9) Now let’s use Eq. 11.9 to walk through an example of a tiny query against a collection of 4 nano documents, computing tf-idf values and seeing the rank of the documents.

## Key terms
- **document** — 28 mentions
- **tf-idf** — 24 mentions
- **query** — 19 mentions
- **vector** — 12 mentions
- **cosine** — 11 mentions
- **product** — 10 mentions
- **sweet** — 9 mentions
- **term** — 9 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing Chapter 11.pdf#page=7|Speech and Language Processing Chapter 11.pdf p. 7]]

## Liens
- Up: [[research/slp-ch11/information-retrieval]]
- ← Prev: [[research/slp-ch11/term-weighting-tf-idf-and-bm25]]
- Next: [[research/slp-ch11/efficiently-finding-documents-the-inverted-index]] →
- Document: [[research/slp-chapter-11]]

#nlp #chapter #study-slice #research #section
