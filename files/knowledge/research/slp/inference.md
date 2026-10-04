---
title: "Inference"
summary: "§I Large Language Models › Automatic Speech Recognition › The: CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION But the most common way of creating a shorter input sequence is to use the convolutional layers we introduced in the previous section."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "356-357"
---

# Inference

§I Large Language Models › Automatic Speech Recognition › The Encoder-Decoder Architecture for ASR › Inference · pp. 356–357 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 15 • AUTOMATIC SPEECH RECOGNITION But the most common way of creating a shorter input sequence is to use the convolutional layers we introduced in the previous section. When a convolutional layer has a stride greater than 1, the output sequence becomes shorter than the input sequence. Let’s see this in two commonly used ASR systems. The Whisper system (Radford et al., 2023) has an audio context window of 30 seconds. It extracts 128 channel log mel features for each frame, with a 25ms window and a stride of 10ms. These are then normalized to 0 mean and a range of -1 to 1. A stride of 10 ms (100 frames per second) means there are 3000 input frames in a 30 second context window. These 3000 frames are passed to two convolutional layers, each one followed by a nonlinearity (Whisper uses GELU (Gaussian Error Linear Unit), which is a smoother version of ReLU). The first convolutional layer has 128 input channels and uses a stride of 1, with number of output channels being the model dimensionality, and the window length is 3000. For the second convolutional layer the number of input and output channels is the model dimensionality, and there is a stride of 2. The stride of 2 in the second convolutional layer makes the output sequence half the length of the input sequence, bringing the output window length down to 1500 and producing an audio token every 20 ms.

## Key terms
- **layer** — 27 mentions
- **encoder** — 18 mentions
- **output** — 17 mentions
- **input** — 15 mentions
- **decoder** — 13 mentions
- **attention** — 12 mentions
- **block** — 11 mentions
- **transformer** — 9 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=356|Speech and Language Processing.pdf p. 356]]

## Liens
- Up: [[research/slp/the-encoder-decoder-architecture-for-asr]]
- ← Prev: [[research/slp/input-and-convolutional-layers]]
- Next: [[research/slp/learning]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
