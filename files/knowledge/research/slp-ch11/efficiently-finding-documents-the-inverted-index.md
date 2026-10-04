---
title: "Efficiently finding documents: the Inverted Index"
summary: "§Retrieval-based Models › Information Retrieval › Efficiently: 11.1 • INFORMATION RETRIEVAL a query q is: X t∈q IDF z }| { log  N dft  weighted tf z }| { tft,d k  1−b+b  |d| |davg|  +tft,d (11.12) where |davg| is the length of the average document."
level: "research"
series: "SLP Chapter 11 (Standalone Chapter)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, chapter, study-slice, section]
pages: "9-9"
---

# Efficiently finding documents: the Inverted Index

§Retrieval-based Models › Information Retrieval › Efficiently finding documents: the Inverted Index · pp. 9–9 · SLP Chapter 11 (Standalone Chapter)

## Extrait
11.1 • INFORMATION RETRIEVAL a query q is: X t∈q IDF z }| { log  N dft  weighted tf z }| { tft,d k  1−b+b  |d| |davg|  +tft,d (11.12) where |davg| is the length of the average document. When k is 0, BM25 reverts to no use of term frequency, just a binary selection of terms in the query (plus idf). A large k results in raw term frequency (plus idf). b ranges from 1 (scaling by document length) to 0 (no length scaling). Manning et al. (2008) suggest reasonable values are k = [1.2,2] and b = 0.75. Kamphuis et al. (2020) is a useful summary of the many minor variants of BM25. Stop words In the past it was common to remove high-frequency words from both the query and document before representing them. The list of such high-frequency words to be removed is called a stop list. The intuition is that high-frequency terms stop list (often function words like the, a, to) carry little semantic weight and may not help with retrieval, and can also help shrink the inverted index files we describe below. The downside of using a stop list is that it makes it difficult to search for phrases that contain words in the stop list. For example, common stop lists would reduce the phrase to be or not to be to the phrase not.

## Key terms
- **document** — 16 mentions
- **term** — 16 mentions
- **list** — 13 mentions
- **word** — 9 mentions
- **stop** — 8 mentions
- **contain** — 7 mentions
- **query** — 6 mentions
- **frequency** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing Chapter 11.pdf#page=9|Speech and Language Processing Chapter 11.pdf p. 9]]

## Liens
- Up: [[research/slp-ch11/information-retrieval]]
- ← Prev: [[research/slp-ch11/document-scoring]]
- Document: [[research/slp-chapter-11]]

#nlp #chapter #study-slice #research #section
