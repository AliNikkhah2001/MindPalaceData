---
title: "Part 8 (pp. 57–64)"
summary: "§Part 8 (pp. 57–64): You are a helpful financial analyst and an expert in extracting financial information from documents. Your goal is to give a response to the user query, based on the relevant context."
level: "research"
series: "RAG in Production with Haystack (Technical Guide)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [rag, retrieval, production, haystack, section]
pages: "57-64"
---

# Part 8 (pp. 57–64)

§Part 8 (pp. 57–64) · pp. 57–64 · RAG in Production with Haystack (Technical Guide)

## Extrait
You are a helpful financial analyst and an expert in extracting financial information from documents. Your goal is to give a response to the user query, based on the relevant context. If no context is provided, respond with "Sorry I cannot answer that." Make sure to follow the following instructions in addition: Do not provide any general information. Do not respond with profanity. Providing examples of inputs and outputs is a good practice, espe‐ cially if outputs are expected to be in a certain format, such as JSON. Few-shot prompting is a way to ensure that outputs adhere to these specific requirements. You can add to the previous prompt as follows (make sure to use delimiters like ``` or ## where it makes sense, to make the instructions clear): template = """You are a helpful financial analyst, and an expert in extracting financial information from documents. Your goal is to give a response to the user query, based on the relevant context. Your output should be JSON formatted, with the JSON key being the user query and the value being the numerical dollar amount, like {query: value}. Here is an example: ``` ## Example Input: -------- Context: "effective for all periods presente…

## Key terms
- **model** — 32 mentions
- **application** — 21 mentions
- **llms** — 17 mentions
- **data** — 13 mentions
- **production** — 12 mentions
- **user** — 11 mentions
- **context** — 11 mentions
- **need** — 11 mentions

## Practice — open in app
- [[pdf:Retrieval-Augmented.pdf#page=57|Retrieval-Augmented.pdf p. 57]]

## Liens
- ← Prev: [[research/rag-haystack/part-7-pp-49-56]]
- Next: [[research/rag-haystack/part-9-pp-65-72]] →
- Document: [[research/rag-haystack-guide]]

#rag #retrieval #production #haystack #research #section
