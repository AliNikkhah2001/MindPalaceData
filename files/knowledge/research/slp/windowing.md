---
title: "Windowing"
summary: "§I Large Language Models › Phonetics and Speech Feature Extra: 14.5 • FEATURE EXTRACTION FOR SPEECH RECOGNITION: LOG MEL SPECTRUM sampling rate is sufficient for telephone-bandwidth speech like the Switchboard corpus, while 16,000 Hz sampling is often used for microphone speech."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "339-339"
---

# Windowing

§I Large Language Models › Phonetics and Speech Feature Extraction › Feature Extraction for Speech Recognition: Log Mel Spectrum › Windowing · pp. 339–339 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
14.5 • FEATURE EXTRACTION FOR SPEECH RECOGNITION: LOG MEL SPECTRUM sampling rate is sufficient for telephone-bandwidth speech like the Switchboard corpus, while 16,000 Hz sampling is often used for microphone speech. Although using higher sampling rates produces higher ASR accuracy, we can’t combine different sampling rates for training and testing ASR systems. Thus if we are testing on a telephone corpus like Switchboard (8 KHz sampling), we must downsample our training corpus to 8 KHz. Similarly, if we are training on multiple corpora and one of them includes telephone speech, we downsample all the wideband corpora to 8KHz. Amplitude measurements are stored as integers, either 8 bit (values from -128127) or 16 bit (values from -32768-32767). This process of representing real-valued numbers as integers is called quantization; all values that are closer together than quantization the minimum granularity (the quantum size) are represented identically. We refer to each sample at time index n in the digitized, quantized waveform as x[n]. Once data is quantized, it is stored in various formats. One parameter of these formats is the sample rate and sample size discussed above; telephone speech is often sampled at 8 kHz and stored as 8-bit samples, and microphone data is often sampled at 16 kHz and stored as 16-bit samples.

## Key terms
- **speech** — 11 mentions
- **value** — 10 mentions
- **window** — 10 mentions
- **sample** — 7 mentions
- **sampling** — 5 mentions
- **signal** — 5 mentions
- **rate** — 4 mentions
- **telephone** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=339|Speech and Language Processing.pdf p. 339]]

## Liens
- Up: [[research/slp/feature-extraction-for-speech-recognition-log-mel-spectrum]]
- ← Prev: [[research/slp/sampling-and-quantization]]
- Next: [[research/slp/discrete-fourier-transform]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
