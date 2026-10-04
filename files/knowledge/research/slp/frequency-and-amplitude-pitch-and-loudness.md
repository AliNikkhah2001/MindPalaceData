---
title: "Frequency and Amplitude; Pitch and Loudness"
summary: "§I Large Language Models › Phonetics and Speech Feature Extra: 14.4 • ACOUSTIC PHONETICS AND SIGNALS frequencies less than 4,000 Hz are transmitted by telephones. Thus, an 8,000 Hz sampling rate is sufficient for telephone-bandwidth speech like the Switchboard corpus, while 16,00"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "329-331"
---

# Frequency and Amplitude; Pitch and Loudness

§I Large Language Models › Phonetics and Speech Feature Extraction › Acoustic Phonetics and Signals › Frequency and Amplitude; Pitch and Loudness · pp. 329–331 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
14.4 • ACOUSTIC PHONETICS AND SIGNALS frequencies less than 4,000 Hz are transmitted by telephones. Thus, an 8,000 Hz sampling rate is sufficient for telephone-bandwidth speech like the Switchboard corpus, while 16,000 Hz sampling is often used for microphone speech. Even an 8,000 Hz sampling rate requires 8000 amplitude measurements for each second of speech, so it is important to store amplitude measurements efficiently. They are usually stored as integers, either 8 bit (values from -128-127) or 16 bit (values from -32768-32767). This process of representing real-valued numbers as integers is called quantization because the difference between two integers acts as quantization a minimum granularity (a quantum size) and all values that are closer together than this quantum size are represented identically. Once data is quantized, it is stored in various formats. One parameter of these formats is the sample rate and sample size discussed above; telephone speech is often sampled at 8 kHz and stored as 8-bit samples, and microphone data is often sampled at 16 kHz and stored as 16-bit samples. Another parameter is the number of channels. For stereo data or for two-party conversations, we can store both channels channel in the same file or we can store them in separate files.

## Key terms
- **pitch** — 16 mentions
- **value** — 14 mentions
- **frequency** — 14 mentions
- **amplitude** — 10 mentions
- **format** — 9 mentions
- **wave** — 9 mentions
- **pressure** — 9 mentions
- **sound** — 8 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=329|Speech and Language Processing.pdf p. 329]]

## Liens
- Up: [[research/slp/acoustic-phonetics-and-signals]]
- ← Prev: [[research/slp/speech-sound-waves]]
- Next: [[research/slp/interpretation-of-phones-from-a-waveform]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
