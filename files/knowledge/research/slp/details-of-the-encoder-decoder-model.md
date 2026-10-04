---
title: "Details of the Encoder-Decoder Model"
summary: "§I Large Language Models › Machine Translation › Details of t: 12.3 • DETAILS OF THE ENCODER-DECODER MODEL that are too similar, suggesting that they were copies rather than translations)."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "275-276"
---

# Details of the Encoder-Decoder Model

§I Large Language Models › Machine Translation › Details of the Encoder-Decoder Model · pp. 275–276 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
12.3 • DETAILS OF THE ENCODER-DECODER MODEL that are too similar, suggesting that they were copies rather than translations). Or pairs can be ranked by their multilingual embedding cosine score and low-scoring pairs discarded. Encoder The green llegó witch arrived <s> llegó la la bruja bruja verde verde </s> Decoder cross-attention transformer blocks Figure 12.5 The encoder-decoder transformer architecture for machine translation. The encoder uses the transformer blocks we saw in Chapter 8, while the decoder uses a more powerful block with an extra crossattention layer that can attend to all the encoder words. We’ll see this in more detail in the next section. The standard architecture for MT is the encoder-decoder transformer. Fig. 12.5 shows the intuition of the architecture at a high level. You’ll see that the encoderdecoder architecture is made up of two transformers: an encoder, which is the same as the basic transformers from Chapter 8, and a decoder, which is augmented with a special new layer called the cross-attention layer. The encoder takes the source language input word tokens X = x1,...,xn and maps them to an output representation Henc = h1,...,hn; via a stack of encoder blocks.

## Key terms
- **layer** — 25 mentions
- **encoder** — 18 mentions
- **block** — 17 mentions
- **decoder** — 16 mentions
- **attention** — 14 mentions
- **transformer** — 13 mentions
- **cross-attention** — 10 mentions
- **language** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=275|Speech and Language Processing.pdf p. 275]]

## Liens
- Up: [[research/slp/machine-translation]]
- ← Prev: [[research/slp/machine-translation-using-encoder-decoder]]
- Next: [[research/slp/decoding-in-mt-beam-search]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
