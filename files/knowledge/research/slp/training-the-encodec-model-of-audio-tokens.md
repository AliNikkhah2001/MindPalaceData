---
title: "Training the EnCodec model of audio tokens"
summary: "§I Large Language Models › Text-to-Speech › Using a codec to : 16.2 • USING A CODEC TO LEARN DISCRETE AUDIO TOKENS In practice, simple VQ doesn’t produce good enough reconstructions, at least not with codebook sizes of 1024."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "379-380"
---

# Training the EnCodec model of audio tokens

§I Large Language Models › Text-to-Speech › Using a codec to learn discrete audio tokens › Training the EnCodec model of audio tokens · pp. 379–380 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
16.2 • USING A CODEC TO LEARN DISCRETE AUDIO TOKENS In practice, simple VQ doesn’t produce good enough reconstructions, at least not with codebook sizes of 1024. 1024 codeword vectors just isn’t enough to represent the wide variety of embeddings we get from encoding all possible speech waveforms. So what the ENCODEC model (and many other audio tokenization methods) use instead is a more sophisticated variant called residual vector quantization, or residual vector quantization RVQ. In residual vector quantization, we use multiple codebooks arranged in a kind RVQ of hierarchy. Figure 16.5 Residual VQ (figure from Chen et al. (2025)). We run VQ on the encoder output embedding to produce a discrete symbol and the corresponding codeword. We then look at the residual, the difference between the encoder output embedding zt and the codeword chosen by VQ. We then take a second codebook and run VQ on this residual. We repeat the process until we have 8 tokens. The idea is very simple. We run standard VQ with a codebook just as in Fig. 16.4 in the prior section. Then for an input embedding zt we take the codeword vector that is produced, let’s call it zq1t for the zt as quantified by codebook 1, and take the difference between the two: residual = zt −z(1) q t.

## Key terms
- **residual** — 14 mentions
- **vector** — 13 mentions
- **loss** — 11 mentions
- **codeword** — 10 mentions
- **audio** — 9 mentions
- **model** — 7 mentions
- **waveform** — 7 mentions
- **speech** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=379|Speech and Language Processing.pdf p. 379]]

## Liens
- Up: [[research/slp/using-a-codec-to-learn-discrete-audio-tokens]]
- ← Prev: [[research/slp/residual-vector-quantization]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
