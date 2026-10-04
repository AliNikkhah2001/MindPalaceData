---
title: "Self-supervised models: HuBERT"
summary: "§I Large Language Models › Automatic Speech Recognition › Sel: 15.4 • SELF-SUPERVISED MODELS: HUBERT An alternative to the encoder-decoder architecture are the class of self-supervised self-supervised speech models."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "359-362"
---

# Self-supervised models: HuBERT

§I Large Language Models › Automatic Speech Recognition › Self-supervised models: HuBERT · pp. 359–362 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
15.4 • SELF-SUPERVISED MODELS: HUBERT An alternative to the encoder-decoder architecture are the class of self-supervised self-supervised speech models. These models don’t directly learn to map an acoustic input to a string of letters and tokens. Instead, they first bootstrap a set of discrete phonetic units from the acoustic input, learning to map from waveforms to these induced units. This pretraining phase doesn’t require transcripts; just unlabeled speech files. After they are pretrained, these models can then be finetuned to do ASR on a smaller set of labeled data, audio paired with transcripts. These models have the advantage that they can take advantage of large amounts of untranscribed audio for most of their training. Here we’ll introduce one self-supervised model called HuBERT (Hsu et al., HuBERT 2021). HuBERT and similar models like wav2vec 2.0 (Baevski et al., 2020) use the wav2vec 2.0 same intuition as the masked language models like BERT introduced in Chapter 9: we mask out some part of the input and train the model to guess what was hidden by the mask. … h4 h2 h1 … hn … Transformer Stack h3 h5 A cosine projection layer cosines w/each class x4 x2 x1 xn x3 x5 A cosine A cosine A cosine A cosine y1 y2 y3 y4 yn MSK MSK MSK A cosine y5 Figure 15.8 Schematic architecture for the HuBERT inference pass in training.

## Key terms
- **vector** — 21 mentions
- **training** — 20 mentions
- **model** — 20 mentions
- **layer** — 20 mentions
- **cosine** — 18 mentions
- **hubert** — 16 mentions
- **classes** — 12 mentions
- **cluster** — 12 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=359|Speech and Language Processing.pdf p. 359]]

## Liens
- Up: [[research/slp/automatic-speech-recognition]]
- ← Prev: [[research/slp/the-encoder-decoder-architecture-for-asr]]
- Next: [[research/slp/ctc]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
