---
title: "Residual Vector Quantization"
summary: "§I Large Language Models › Text-to-Speech › Using a codec to : CHAPTER 16 • TEXT-TO-SPEECH 1.2 0.1 … 0.9 -55 -9 0.2 Encoder 256-d vector to be quantized Similarity Codebook 256-d codewords (vectors) Cluster # … … Vector Quantizer Output: discrete symbol Figure 16.4 The basic VQ a"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "378-378"
---

# Residual Vector Quantization

§I Large Language Models › Text-to-Speech › Using a codec to learn discrete audio tokens › Residual Vector Quantization · pp. 378–378 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 16 • TEXT-TO-SPEECH 1.2 0.1 … 0.9 -55 -9 0.2 Encoder 256-d vector to be quantized Similarity Codebook 256-d codewords (vectors) Cluster # … … Vector Quantizer Output: discrete symbol Figure 16.4 The basic VQ algorithm at inference time, after the codebook has been learned. The input is a span of speech encoded by the encoder into a vector of dimensionality D = 256. This vector is compared with each codeword (cluster centroid) in the codebook. The codeword for cluster 3 is most similar, so the VQ outputs 3 as the discrete representation of this vector. estimation step, the codeword for each cluster is recomputed by recalculating a new mean vector. The result is that the clusters and their centroids slowly adjust to the training space. We iterate back and forth between these two steps until the algorithm converges. VQ can also be used as part of end-to-end training, as we will discuss below, in which case instead of iterative k-means, we instead recompute the means during minibatch training via online algorithms like exponential moving averages. At the end of clustering, the cluster index can be used as a discrete symbol. Each cluster is also associated with a codeword, the vector which is the centroid of all codeword the vectors in the cluster.

## Key terms
- **vector** — 15 mentions
- **codeword** — 15 mentions
- **cluster** — 12 mentions
- **codebook** — 8 mentions
- **discrete** — 5 mentions
- **speech** — 5 mentions
- **symbol** — 4 mentions
- **input** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=378|Speech and Language Processing.pdf p. 378]]

## Liens
- Up: [[research/slp/using-a-codec-to-learn-discrete-audio-tokens]]
- ← Prev: [[research/slp/vector-quantization]]
- Next: [[research/slp/training-the-encodec-model-of-audio-tokens]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
