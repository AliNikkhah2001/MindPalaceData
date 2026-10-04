---
title: "Information Retrieval with Dense Vectors"
summary: "§I Large Language Models › Retrieval-based Models › Informati: 11.3 • INFORMATION RETRIEVAL WITH DENSE VECTORS The classic tf-idf or BM25 algorithms for IR have long been known to have a conceptual flaw: they work only if there is exact overlap of words between the query and docu"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "255-256"
---

# Information Retrieval with Dense Vectors

§I Large Language Models › Retrieval-based Models › Information Retrieval with Dense Vectors · pp. 255–256 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
11.3 • INFORMATION RETRIEVAL WITH DENSE VECTORS The classic tf-idf or BM25 algorithms for IR have long been known to have a conceptual flaw: they work only if there is exact overlap of words between the query and document. In other words, the user posing a query (or asking a question) needs to guess exactly what words the writer of the answer might have used, an issue called the vocabulary mismatch problem (Furnas et al., 1987). The solution to this problem is to use an approach that can handle synonymy: instead of (sparse) word-count vectors, using (dense) embeddings. This idea was first proposed for retrieval in the last century under the name of Latent Semantic Indexing approach (Deerwester et al., 1990), but is implemented in modern times via encoders like BERT. The most powerful approach is to present both the query and the document to a single encoder, allowing the transformer self-attention to see all the tokens of both the query and the document, and thus building a representation that is sensitive to the meanings of both query and document. Then a linear layer can be put on top of the [CLS] token to predict a similarity score for the query/document tuple: z = BERT(q;[SEP];d)[CLS] score(q,d) = softmax(U(z)) (11.17) This architecture is shown in Fig.

## Key terms
- **document** — 33 mentions
- **query** — 27 mentions
- **token** — 22 mentions
- **bert** — 10 mentions
- **encoder** — 10 mentions
- **vector** — 10 mentions
- **encode** — 9 mentions
- **score** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=255|Speech and Language Processing.pdf p. 255]]

## Liens
- Up: [[research/slp/retrieval-based-models]]
- ← Prev: [[research/slp/evaluation-of-information-retrieval-systems]]
- Next: [[research/slp/retrieval-augmented-generation-rag]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
