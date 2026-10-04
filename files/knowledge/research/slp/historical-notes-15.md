---
title: "Historical Notes"
summary: "§I Large Language Models › Text-to-Speech › Historical Notes: 16.7 • SUMMARY This chapter introduced the fundamental algorithms of text-to-speech (TTS). • A common modern algorithm for TTS is to use conditional generation with a language model over audio tokens learned by a codec"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "385-385"
---

# Historical Notes

§I Large Language Models › Text-to-Speech › Historical Notes · pp. 385–385 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
16.7 • SUMMARY This chapter introduced the fundamental algorithms of text-to-speech (TTS). • A common modern algorithm for TTS is to use conditional generation with a language model over audio tokens learned by a codec model. • A neural audio codec, short for coder/decoder, is a system that encodes analog speech signals into a digitized, discrete compressed representation for compression. • The discrete symbols that a codec produces as its compressed representation can be used as discrete codes for language modeling. • A codec includes an encoder that uses convnets to downsample speech into a downsampled embedding, a quantizer that converts the embedding into a series of discrete tokens, and a decoder that uses convnets to upsample the tokens/embedding back into a lossy reconstructed waveform. • Vector Quantization (VQ) is a method for turning a series of vectors into a series of discrete symbols. This can be done by using k-means clustering, and then creating a codebook in which each code is represented by a vector at the centroid of each cluster, called a codeword. Input vector can be assigned the nearest codeword cluster. • Residual Vector Quantization (RVQ) is a hierarchical ve…

## Key terms
- **vector** — 9 mentions
- **speech** — 7 mentions
- **discrete** — 6 mentions
- **model** — 5 mentions
- **codec** — 5 mentions
- **synthesis** — 5 mentions
- **formant** — 5 mentions
- **audio** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=385|Speech and Language Processing.pdf p. 385]]

## Liens
- Up: [[research/slp/text-to-speech]]
- ← Prev: [[research/slp/summary-15]]
- Next: [[research/slp/exercises-9]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
