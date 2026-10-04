---
title: "RAG in Production with Haystack (Technical Guide)"
summary: "The engineering counterpart to the theory: building trustworthy, scalable RAG systems with Haystack — chunking, retrieval, eval, and production concerns. Pair with the slide deck for the paradigms, keep this for how to actually ship."
level: "research"
series: "D:\\Research"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [rag, retrieval, production, haystack]
---

# RAG in Production with Haystack (Technical Guide)

## Pourquoi ce nœud — explication
The engineering counterpart to the theory: building trustworthy, scalable RAG systems with Haystack — chunking, retrieval, eval, and production concerns. Pair with the slide deck for the paradigms, keep this for how to actually ship.

Source file: `Retrieval-Augmented.pdf` · [[index-research]]

```mermaid
graph LR
    Chunk --> Retrieve
    Retrieve --> Rerank
    Rerank --> Generate
    Generate --> Evaluate
```

En bref: $$P(y \mid x) = \sum_{z} P(z \mid x)\,P(y \mid x, z)$$

## Contents (17 sections — every entry links somewhere)
- [[research/rag-haystack/part-1-pp-1-8|part 1 pp 1 8]]
- [[research/rag-haystack/part-10-pp-73-80|part 10 pp 73 80]]
- [[research/rag-haystack/part-11-pp-81-88|part 11 pp 81 88]]
- [[research/rag-haystack/part-12-pp-89-96|part 12 pp 89 96]]
- [[research/rag-haystack/part-13-pp-97-104|part 13 pp 97 104]]
- [[research/rag-haystack/part-14-pp-105-112|part 14 pp 105 112]]
- [[research/rag-haystack/part-15-pp-113-120|part 15 pp 113 120]]
- [[research/rag-haystack/part-16-pp-121-128|part 16 pp 121 128]]
- [[research/rag-haystack/part-17-pp-129-132|part 17 pp 129 132]]
- [[research/rag-haystack/part-2-pp-9-16|part 2 pp 9 16]]
- [[research/rag-haystack/part-3-pp-17-24|part 3 pp 17 24]]
- [[research/rag-haystack/part-4-pp-25-32|part 4 pp 25 32]]
- [[research/rag-haystack/part-5-pp-33-40|part 5 pp 33 40]]
- [[research/rag-haystack/part-6-pp-41-48|part 6 pp 41 48]]
- [[research/rag-haystack/part-7-pp-49-56|part 7 pp 49 56]]
- [[research/rag-haystack/part-8-pp-57-64|part 8 pp 57 64]]
- [[research/rag-haystack/part-9-pp-65-72|part 9 pp 65 72]]

## Practice — open in app
- [[pdf:Retrieval-Augmented.pdf|Open Retrieval-Augmented.pdf]]
- [[quiz:3|ML starter quiz]]

## Liens
- [[rag-slides]]
- [[slp-book]]
- [[index-research]]

#rag #retrieval #production #haystack #research #lecture
