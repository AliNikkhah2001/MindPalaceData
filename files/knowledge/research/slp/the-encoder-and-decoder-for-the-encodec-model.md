---
title: "The Encoder and Decoder for the EnCodec model"
summary: "§I Large Language Models › Text-to-Speech › Using a codec to : CHAPTER 16 • TEXT-TO-SPEECH trained to recreate the same audio waveform out, via an intermediate representation consisting of discrete tokens created by vector quantization."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "376-376"
---

# The Encoder and Decoder for the EnCodec model

§I Large Language Models › Text-to-Speech › Using a codec to learn discrete audio tokens › The Encoder and Decoder for the EnCodec model · pp. 376–376 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 16 • TEXT-TO-SPEECH trained to recreate the same audio waveform out, via an intermediate representation consisting of discrete tokens created by vector quantization. Audio tokenizers have three stages: 1. an encoder maps the acoustic waveform, a series of T values x = x1,x2,...,xT, to a sequence of τ embeddings z = z1,z2,...,zτ. τ is typically 100-1000 times smaller than T. 2. a vector quantizer that takes each embedding zt corresponding to part of the waveform, and represents it by a sequence of discrete tokens each taken from one of the Nc codebooks, qt = qt,1,qt,2,...,qt,Nc. The vector quantizer also sums the vector codewords from each codebook to create a quantizer output vector zqt. 3. a decoder that generates a lossy reconstructed waveform span ˆx from the quantizer output vector zqt. Audio tokenizers are generally learned end-to-end, using loss functions that reward a tokenization that allows the system to reconstruct the input waveform. In the following subsections we’ll go through the components of one particular tokenizer, the ENCODEC tokenizer of D´efossez et al. (2023). Conv1D (k=7, n=C) Encoder EncoderBlock (N=16C, S=8) EncoderBlock (N=8C, S=5) EncoderBlock (N=…

## Key terms
- **waveform** — 10 mentions
- **embedding** — 9 mentions
- **encoder** — 7 mentions
- **vector** — 6 mentions
- **decoder** — 6 mentions
- **conv1d** — 6 mentions
- **encoderblock** — 5 mentions
- **decoderblock** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=376|Speech and Language Processing.pdf p. 376]]

## Liens
- Up: [[research/slp/using-a-codec-to-learn-discrete-audio-tokens]]
- Next: [[research/slp/vector-quantization]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
