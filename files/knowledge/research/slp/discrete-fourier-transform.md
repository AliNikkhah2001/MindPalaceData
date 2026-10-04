---
title: "Discrete Fourier Transform"
summary: "§I Large Language Models › Phonetics and Speech Feature Extra: CHAPTER 14 • PHONETICS AND SPEECH FEATURE EXTRACTION Shift ms Window 25 ms Shift ms Window 25 ms Window 25 ms Figure 14.26 Windowing, showing a 25 ms rectangular window with a 10ms stride."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "340-340"
---

# Discrete Fourier Transform

§I Large Language Models › Phonetics and Speech Feature Extraction › Feature Extraction for Speech Recognition: Log Mel Spectrum › Discrete Fourier Transform · pp. 340–340 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 14 • PHONETICS AND SPEECH FEATURE EXTRACTION Shift ms Window 25 ms Shift ms Window 25 ms Window 25 ms Figure 14.26 Windowing, showing a 25 ms rectangular window with a 10ms stride. tracted windowed signal looks just like the original signal. The rectangular window, however, abruptly cuts off the signal at its boundaries, which creates problems when we do Fourier analysis. For this reason, for acoustic feature creation we more commonly use the Hamming window, which shrinks the values of the signal toward Hamming zero at the window boundaries, avoiding discontinuities. Figure 14.27 shows both; the equations are as follows (assuming a window that is L frames long): rectangular w[n] =  1 0 ≤n ≤L−1 otherwise (14.12) Hamming w[n] =  0.54−0.46cos( 2πn L ) 0 ≤n ≤L−1 otherwise (14.13) Time (s) 0.0475896 -0.5 0.4999 Rectangular window Hamming window Time (s) 0.00455938 0.0256563 -0.4826 0.4999 Time (s) 0.00455938 0.0256563 -0.5 0.4999 Figure 14.27 Windowing a sine wave with the rectangular or Hamming windows.

## Key terms
- **window** — 11 mentions
- **rectangular** — 5 mentions
- **hamming** — 5 mentions
- **signal** — 4 mentions
- **time** — 3 mentions
- **feature** — 2 mentions
- **shift** — 2 mentions
- **windowing** — 2 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=340|Speech and Language Processing.pdf p. 340]]

## Liens
- Up: [[research/slp/feature-extraction-for-speech-recognition-log-mel-spectrum]]
- ← Prev: [[research/slp/windowing]]
- Next: [[research/slp/mel-filter-bank-and-log]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
