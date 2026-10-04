---
title: "Input and Convolutional Layers"
summary: "§I Large Language Models › Automatic Speech Recognition › The: 15.3 • THE ENCODER-DECODER ARCHITECTURE FOR ASR ⋯ ⋯ 2 × Conv1D + GELU ⋮ cross attention Log-Mel Spectrogram ~ SOT EN TRANS- CRIBE 0.0 The quick Tokens in Multitask Training Format Transformer Encoder Blocks Transforme"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "355-355"
---

# Input and Convolutional Layers

§I Large Language Models › Automatic Speech Recognition › The Encoder-Decoder Architecture for ASR › Input and Convolutional Layers · pp. 355–355 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
15.3 • THE ENCODER-DECODER ARCHITECTURE FOR ASR ⋯ ⋯ 2 × Conv1D + GELU ⋮ cross attention Log-Mel Spectrogram ~ SOT EN TRANS- CRIBE 0.0 The quick Tokens in Multitask Training Format Transformer Encoder Blocks Transformer Decoder Blocks EN 0.0 The quick brown ⋮ ⋮ next-token prediction Sinusoidal Positional Encoding Learned Positional Encoding Sequence-to-sequence learning MLP self attention MLP self attention MLP self attention MLP cross attention self attention MLP cross attention self attention MLP cross attention self attention TRANS- CRIBE Figure 15.6 A sketch of the Whisper architecture from Radford et al. (2023). Because Whisper is a multitask system that also does translation, Whisper’s transcription format has a Start of Transcript (SOT) token, a language tag, and then an instruction token for whether to transcribe or translate. Speech Model (OWSM), which reproduces Whisper-style training but offers a fully open-source toolkit and publicly available data (Peng et al., 2023). The encoder-decoder architecture is particularly appropriate when input and output sequences have stark length differences, as they do for speech, with long acoustic feature sequences mapping to much shorter sequences of letters or words.

## Key terms
- **attention** — 10 mentions
- **self** — 6 mentions
- **sequence** — 6 mentions
- **token** — 5 mentions
- **speech** — 5 mentions
- **vector** — 5 mentions
- **architecture** — 4 mentions
- **cross** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=355|Speech and Language Processing.pdf p. 355]]

## Liens
- Up: [[research/slp/the-encoder-decoder-architecture-for-asr]]
- Next: [[research/slp/inference]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
