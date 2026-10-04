---
title: "Part 6 (pp. 41–48)"
summary: "§Part 6 (pp. 41–48): import os from haystack import Pipeline from haystack.components.builders import ( AnswerBuilder, ChatPromptBuilder ) from haystack.components.converters import PyPDFToDocument from haystack.components.embedders import ( SentenceTransformersTextEmbedder, Sent"
level: "research"
series: "RAG in Production with Haystack (Technical Guide)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [rag, retrieval, production, haystack, section]
pages: "41-48"
---

# Part 6 (pp. 41–48)

§Part 6 (pp. 41–48) · pp. 41–48 · RAG in Production with Haystack (Technical Guide)

## Extrait
import os from haystack import Pipeline from haystack.components.builders import ( AnswerBuilder, ChatPromptBuilder ) from haystack.components.converters import PyPDFToDocument from haystack.components.embedders import ( SentenceTransformersTextEmbedder, SentenceTransformersDocumentEmbedder ) from haystack.components.generators.\ chat import OpenAIChatGenerator from haystack.components.preprocessors import ( DocumentCleaner, DocumentSplitter ) from haystack.components.\ retrievers import InMemoryEmbeddingRetriever from haystack.components.writers import DocumentWriter from haystack.dataclasses import ChatMessage from haystack.document_stores.\ in_memory import InMemoryDocumentStore os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY" Next, instantiate the document store and document writer: document_store = InMemoryDocumentStore() document_writer = DocumentWriter(document_store) Now add the relevant components to convert PDF documents and clean, split, embed, and write the data to the in-memory database. These are the converter, cleaner, splitter, embedder, and writer com‐ ponents respectively: splitter = DocumentSplitter("sentence", 5) document_embedder = SentenceTransformersDocum…

## Key terms
- **document** — 39 mentions
- **pipeline** — 38 mentions
- **answer** — 36 mentions
- **component** — 25 mentions
- **context** — 22 mentions
- **basic** — 19 mentions
- **result** — 18 mentions
- **haystack** — 17 mentions

## Practice — open in app
- [[pdf:Retrieval-Augmented.pdf#page=41|Retrieval-Augmented.pdf p. 41]]

## Liens
- ← Prev: [[research/rag-haystack/part-5-pp-33-40]]
- Next: [[research/rag-haystack/part-7-pp-49-56]] →
- Document: [[research/rag-haystack-guide]]

#rag #retrieval #production #haystack #research #section
