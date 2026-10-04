---
title: "Part 4 (pp. 25–32)"
summary: "§Part 4 (pp. 25–32): Sample Haystack RAG pipeline Build Your First RAG App Using Haystack Take a look at the following example query and its result."
level: "research"
series: "RAG in Production with Haystack (Technical Guide)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [rag, retrieval, production, haystack, section]
pages: "25-32"
---

# Part 4 (pp. 25–32)

§Part 4 (pp. 25–32) · pp. 25–32 · RAG in Production with Haystack (Technical Guide)

## Extrait
Figure 1-6. Sample Haystack RAG pipeline Build Your First RAG App Using Haystack Take a look at the following example query and its result. Here, the RAG pipeline is invoked to answer a particular question, including retrieving the relevant context corresponding to that question, and it appropriately builds the prompt based on the query and context: question = "What is Sonnet 12" results = rag_pipeline.run( { "retriever": {"query": question}, "prompt_builder": {"question": question} }, include_outputs_from = ["retriever"] ) print(results["llm"]['replies'][0]) Response: Sonnet 12 is a poem that discusses the passage of time and the inevitability of aging and death, using imagery such as a clock, nature, and beauty. Congratulations, you have successfully created (and visualized) your first RAG app! Custom Components Components that are connected form a pipeline. Haystack provides the flexibility to choose between using prebuilt components or cre‐ ating custom components. Prebuilt components perform multiple operations like preprocessing, retrieving, generating embeddings, and so forth. If the user would also like to have a custom compo‐ nent, we can define one using the `@component` decorator and implement a run method.

## Key terms
- **component** — 18 mentions
- **pipeline** — 15 mentions
- **application** — 15 mentions
- **haystack** — 11 mentions
- **query** — 11 mentions
- **text** — 10 mentions
- **question** — 9 mentions
- **data** — 9 mentions

## Practice — open in app
- [[pdf:Retrieval-Augmented.pdf#page=25|Retrieval-Augmented.pdf p. 25]]

## Liens
- ← Prev: [[research/rag-haystack/part-3-pp-17-24]]
- Next: [[research/rag-haystack/part-5-pp-33-40]] →
- Document: [[research/rag-haystack-guide]]

#rag #retrieval #production #haystack #research #section
