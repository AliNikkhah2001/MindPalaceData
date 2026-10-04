---
title: "The Automatic Speech Recognition Task"
summary: "§I Large Language Models › Automatic Speech Recognition › The: CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION We’ll then introduce two families of methods for ASR. The first is the encoderdecoder paradigm, and we’ll introduce the baseline attention-based encoder decoder algorithm, som"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "348-349"
---

# The Automatic Speech Recognition Task

§I Large Language Models › Automatic Speech Recognition › The Automatic Speech Recognition Task · pp. 348–349 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION We’ll then introduce two families of methods for ASR. The first is the encoderdecoder paradigm, and we’ll introduce the baseline attention-based encoder decoder algorithm, sometimes called Listen Attend and Spell after an early implementation. We’ll also introduce a more advanced encoder-decoder system, OpenAI’s Whisper system (Radford et al., 2023) as well an open system based on the same architecture, OWSM (the Open Whisper-style Speech Model) (Peng et al., 2023). (These models have additional capabilities including translation, as we’ll discuss later). The second is the use of self-supervised speech models (sometimes called SSL for selfsupervised learning) like Wav2Vec2.0 or HuBERT, which are encoders that learn abstract representations of speech that can be used for ASR by pairing them with the CTC loss function for decoding. We’ll conclude with the standard word error rate metric used to evaluate ASR. Before describing algorithms for ASR, let’s talk about how the ASR task itself varies. One dimension of variation is vocabulary size. Some ASR tasks have long been solved with extremely high accuracy, like those with a 2-word vocabulary (yes versus no) or an 11 word vocabulary like digit recognition (recognizing sequences digit recognition of digits including zero to nine plus oh).

## Key terms
- **speech** — 28 mentions
- **speaker** — 15 mentions
- **read** — 10 mentions
- **human** — 9 mentions
- **corpus** — 9 mentions
- **word** — 8 mentions
- **system** — 7 mentions
- **task** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=348|Speech and Language Processing.pdf p. 348]]

## Liens
- Up: [[research/slp/automatic-speech-recognition]]
- Next: [[research/slp/convolutional-neural-networks]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
