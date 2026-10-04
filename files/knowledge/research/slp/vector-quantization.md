---
title: "Vector Quantization"
summary: "§I Large Language Models › Text-to-Speech › Using a codec to : 16.2 • USING A CODEC TO LEARN DISCRETE AUDIO TOKENS vectors, each of dimensionality D. For the purposes of this explanation, we’ll use D = 256."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "377-377"
---

# Vector Quantization

§I Large Language Models › Text-to-Speech › Using a codec to learn discrete audio tokens › Vector Quantization · pp. 377–377 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
16.2 • USING A CODEC TO LEARN DISCRETE AUDIO TOKENS vectors, each of dimensionality D. For the purposes of this explanation, we’ll use D = 256. This downsampling is accomplished by having a series of encoder blocks that are made up of convolutional layers with strides larger than 1 that iteratively downsample the audio, as we discussed at the end of Section 15.2. The convolution blocks are sketched in Fig. 16.3, and include a long series of convolutions as well as residual units that add a convolution to the prior input. The output of the encoder is an embedding zt at time t, 75 of which are produced per second. This embedding is then quantized (as discussed in the next section), turning each embedding zt into a series of Nc discrete symbols qt = qt,1,qt,2,...,qt,Nc, and also turning the series of symbols into a new quantizer output vector zqt. Finally, the decoder takes the output embedding from the quantizer zqt and generates a waveform via a symmetric set of convnets that upsample the audio. In summary, a 24kHz waveform comes through, we encode/downsample it into a vector zt of dimensionality D = 256, quantize it into discrete symbols qt, turn it back into a vector zqt of dimensionality D = 256, and then decode/upsample that vector back into a waveform at 24kHz.

## Key terms
- **vector** — 24 mentions
- **algorithm** — 8 mentions
- **discrete** — 7 mentions
- **quantization** — 7 mentions
- **series** — 6 mentions
- **cluster** — 6 mentions
- **symbols** — 5 mentions
- **speech** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=377|Speech and Language Processing.pdf p. 377]]

## Liens
- Up: [[research/slp/using-a-codec-to-learn-discrete-audio-tokens]]
- ← Prev: [[research/slp/the-encoder-and-decoder-for-the-encodec-model]]
- Next: [[research/slp/residual-vector-quantization]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
