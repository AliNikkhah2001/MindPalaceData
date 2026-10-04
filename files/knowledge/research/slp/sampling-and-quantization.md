---
title: "Sampling and Quantization"
summary: "§I Large Language Models › Phonetics and Speech Feature Extra: CHAPTER 14 • PHONETICS AND SPEECH FEATURE EXTRACTION ture vectors, each vector representing the information in a small time window of feature vector the signal."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "338-338"
---

# Sampling and Quantization

§I Large Language Models › Phonetics and Speech Feature Extraction › Feature Extraction for Speech Recognition: Log Mel Spectrum › Sampling and Quantization · pp. 338–338 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 14 • PHONETICS AND SPEECH FEATURE EXTRACTION ture vectors, each vector representing the information in a small time window of feature vector the signal. Sometimes speech recognition or processing algorithms will start with the waveform, in which case that processing is done by the convolutional networks (convnets) that we will introduce in Chapter 15. Other systems begin instead at a higher level, with the log mel spectrum. So in this section we introduce this commonly used feature vector: sequences of log mel spectrum vectors. In the following section we’ll introduce an alternative vector, the MFCC representation. We’ll introduce these concepts at a relatively high level; a speech signal processing course is recommended for more details. We begin by repeating from Section 14.4.2 the process of digitizing and quantizing an analog speech waveform. The input to a speech recognizer is a complex series of changes in air pressure. These changes in air pressure obviously originate with the speaker and are caused by the specific way that air passes through the glottis and out the oral or nasal cavities. We represent sound waves by plotting the change in air pressure over time. One metaphor which sometimes helps in understanding these graphs is that of a vertical plate blocking the air pressure waves (perhaps in a microphone in front of a speaker’s mouth, or the eardrum in a hearer’s ear).

## Key terms
- **speech** — 8 mentions
- **wave** — 8 mentions
- **pressure** — 7 mentions
- **sample** — 7 mentions
- **vector** — 6 mentions
- **frequency** — 6 mentions
- **time** — 5 mentions
- **signal** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=338|Speech and Language Processing.pdf p. 338]]

## Liens
- Up: [[research/slp/feature-extraction-for-speech-recognition-log-mel-spectrum]]
- Next: [[research/slp/windowing]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
