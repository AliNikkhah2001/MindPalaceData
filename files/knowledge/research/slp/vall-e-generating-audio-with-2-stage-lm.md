---
title: "VALL-E: Generating audio with 2-stage LM"
summary: "§I Large Language Models › Text-to-Speech › VALL-E: Generatin: 16.3 • VALL-E: GENERATING AUDIO WITH 2-STAGE LM output vector zt and the reconstructed vector after the quantization zqt, i.e."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "381-382"
---

# VALL-E: Generating audio with 2-stage LM

§I Large Language Models › Text-to-Speech › VALL-E: Generating audio with 2-stage LM · pp. 381–382 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
16.3 • VALL-E: GENERATING AUDIO WITH 2-STAGE LM output vector zt and the reconstructed vector after the quantization zqt, i.e. the codeword, summed over all the Nc codebooks and residuals. LVQ(x, ˆx) = T X t=1 Nc X c=1 ||z(c)t −z(c) q t|| (16.3) The total loss function can then just be a weighted sum of these losses: L(x, ˆx) = λ1Lreconstruction(x, ˆx)+λ2LGAN(x, ˆx)+λ3LVQ(x, ˆx) (16.4) As we summarized in the introduction, the structure of TTS systems like VALL-E is to take as input a text to be synthesized and a sample of the voice to be used, and tokenize both, using BPE for the text and an audio codec for the speech. We then use a language model to conditionally generate discrete audio tokens corresponding to the text prompt, in the voice of the speech sample. Autoregressive (AR) Transformer Text Audio Prompt CT’+1,1 CT’+2,1 CT,1 CT’+1,2 CT’+1,3 CT’+2,2 CT,2 CT’+2,3 x C CT,3 CT’+1,1 CT’+2,1 CT,1 x C x C x C CT’+1,1 CT’+1,2 … … … CT,1 CT’+2,1 CT’+2,2 CT,2 … Non-Autoregressive Non-Autoregressive Non-Autoregressive Output code sequence … Figure 16.7 The 2-stage language modelling approach for VALL-E, showing the inference stage for the autoregressive transformer and the first 3 of the 7 non-autoregressive transformers.

## Key terms
- **code** — 20 mentions
- **audio** — 10 mentions
- **text** — 9 mentions
- **quantizer** — 9 mentions
- **output** — 8 mentions
- **generate** — 8 mentions
- **autoregressive** — 8 mentions
- **non-autoregressive** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=381|Speech and Language Processing.pdf p. 381]]

## Liens
- Up: [[research/slp/text-to-speech]]
- ← Prev: [[research/slp/using-a-codec-to-learn-discrete-audio-tokens]]
- Next: [[research/slp/tts-evaluation]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
