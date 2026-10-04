---
title: "ASR Evaluation: Word Error Rate"
summary: "§I Large Language Models › Automatic Speech Recognition › ASR: 15.6 • ASR EVALUATION: WORD ERROR RATE ENCODER … DECODER … H <s> i t ‘ s t i m x1 xn … … i t ’ s t i m e … CTC Loss Encoder-Decoder Loss Figure 15.16 Combining the CTC and encoder-decoder loss functions."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "367-369"
---

# ASR Evaluation: Word Error Rate

§I Large Language Models › Automatic Speech Recognition › ASR Evaluation: Word Error Rate · pp. 367–369 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
15.6 • ASR EVALUATION: WORD ERROR RATE ENCODER … DECODER … H <s> i t ‘ s t i m x1 xn … … i t ’ s t i m e … CTC Loss Encoder-Decoder Loss Figure 15.16 Combining the CTC and encoder-decoder loss functions. Because of the strong independence assumption in CTC (assuming that the output at time t is independent of the output at time t −1), recognizers based on CTC don’t achieve as high an accuracy as the attention-based encoder-decoder recognizers. CTC recognizers have the advantage, however, that they can be used for streaming. Streaming means recognizing words on-line rather than waiting until streaming the end of the sentence to recognize them. Streaming is crucial for many applications, from commands to dictation, where we want to start recognition while the user is still talking. Algorithms that use attention need to compute the hidden state sequence over the entire input first in order to provide the attention distribution context, before the decoder can start decoding. By contrast, a CTC algorithm can input letters from left to right immediately. If we want to do streaming, we need a way to improve CTC recognition to remove the conditional independent assumption, enabling it to know about output history.

## Key terms
- **error** — 30 mentions
- **word** — 28 mentions
- **rate** — 17 mentions
- **system** — 12 mentions
- **time** — 11 mentions
- **segment** — 10 mentions
- **output** — 9 mentions
- **number** — 9 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=367|Speech and Language Processing.pdf p. 367]]

## Liens
- Up: [[research/slp/automatic-speech-recognition]]
- ← Prev: [[research/slp/ctc]]
- Next: [[research/slp/summary-14]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
