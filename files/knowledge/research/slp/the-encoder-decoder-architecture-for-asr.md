---
title: "The Encoder-Decoder Architecture for ASR"
summary: "§I Large Language Models › Automatic Speech Recognition › The: CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION sequence z will be half the length of the input sequence x. Convolutional layers with strides greater than 1 are commonly used to shorten an input sequence."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "354-358"
---

# The Encoder-Decoder Architecture for ASR

§I Large Language Models › Automatic Speech Recognition › The Encoder-Decoder Architecture for ASR · pp. 354–358 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION sequence z will be half the length of the input sequence x. Convolutional layers with strides greater than 1 are commonly used to shorten an input sequence. This is useful partly because a shorter signal takes less memory and computational bandwidth, but also, as we’ll see in the next section, because it helps address the mismatch between the length of acoustic frame embeddings (10 ms) and letters or words, which cover much more of the signal. Finally, in practice a convolutional layer can be followed by an output nonlinearity, like a ReLU layer. The first ASR architecture we introduce is the encoder-decoder architecture, the same architecture introduced for MT in Chapter 12. Fig. 15.5 sketches this architecture, called attention-based encoder decoder or AED, or listen attend and spell AED listen attend and spell (LAS) after the two papers which first applied it to speech (Chorowski et al. 2014, Chan et al. 2016). The input to the architecture x is a sequence of t acoustic feature vectors X = x1,x2,...,xt, one vector per 10 ms frame. We often start from the log mel spectral features described in the previous section, although it’s also possible to start from a raw wavefile.

## Key terms
- **layer** — 30 mentions
- **encoder** — 23 mentions
- **attention** — 22 mentions
- **sequence** — 21 mentions
- **output** — 21 mentions
- **input** — 20 mentions
- **architecture** — 17 mentions
- **decoder** — 16 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=354|Speech and Language Processing.pdf p. 354]]

## Liens
- Up: [[research/slp/automatic-speech-recognition]]
- ← Prev: [[research/slp/convolutional-neural-networks]]
- Next: [[research/slp/self-supervised-models-hubert]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
