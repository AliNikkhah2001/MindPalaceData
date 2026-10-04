---
title: "K-means clustering"
summary: "§I Large Language Models › Automatic Speech Recognition › Sel: CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION … h4 h2 h1 … hn … Transformer Stack 7 CNN Layers (Frozen) h3 h5 A projection x4 x2 x1 xn x3 x5 A A A A i i i t h A t target letters Figure 15.11 The HuBERT finetuning pass aft"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "362-362"
---

# K-means clustering

§I Large Language Models › Automatic Speech Recognition › Self-supervised models: HuBERT › K-means clustering · pp. 362–362 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION … h4 h2 h1 … hn … Transformer Stack 7 CNN Layers (Frozen) h3 h5 A projection x4 x2 x1 xn x3 x5 A A A A i i i t h A t target letters Figure 15.11 The HuBERT finetuning pass after pretraining. The projection layer and cosine steps are removed, leaving only a randomly initialized projection/softmax layer. The CNN layers are frozen, and the rest of the model is finetuned on a dataset of audio with transcripts, trained with the CTC loss (Section 15.5) to produce letters as output. The parameters that are updated in finetuning are shown in red (the projection layer and the transformer stack). (corresponding to the 26 English letters and a few extra characters) for the ASR task. The CNNs are frozen and the rest of the model is finetuned for ASR using the CTC loss function to be described in Section 15.5. In this section we give the k-means clustering algorithm more formally. K-means k-means is a family of algorithms for grouping a set of vector data into k clusters. Clustering is useful whenever we want to treat a group of elements in the same way. In speech processing it is very commonly used whenever we need to convert a set of vectors over real values into a set of discrete symbols.

## Key terms
- **vector** — 9 mentions
- **algorithm** — 7 mentions
- **layer** — 5 mentions
- **step** — 5 mentions
- **cluster** — 5 mentions
- **projection** — 4 mentions
- **k-means** — 4 mentions
- **centroid** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=362|Speech and Language Processing.pdf p. 362]]

## Liens
- Up: [[research/slp/self-supervised-models-hubert]]
- ← Prev: [[research/slp/learning-for-hubert]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
