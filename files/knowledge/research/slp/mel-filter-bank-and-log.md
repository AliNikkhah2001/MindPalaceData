---
title: "Mel Filter Bank and Log"
summary: "§I Large Language Models › Phonetics and Speech Feature Extra: 14.5 • FEATURE EXTRACTION FOR SPEECH RECOGNITION: LOG MEL SPECTRUM The next step is to extract spectral information for our windowed signal; we need to know how much energy the signal contains at different frequency b"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "341-341"
---

# Mel Filter Bank and Log

§I Large Language Models › Phonetics and Speech Feature Extraction › Feature Extraction for Speech Recognition: Log Mel Spectrum › Mel Filter Bank and Log · pp. 341–341 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
14.5 • FEATURE EXTRACTION FOR SPEECH RECOGNITION: LOG MEL SPECTRUM The next step is to extract spectral information for our windowed signal; we need to know how much energy the signal contains at different frequency bands. The tool for extracting spectral information for discrete frequency bands for a discrete-time (sampled) signal is the discrete Fourier transform or DFT. Discrete Fourier transform DFT The input to the DFT is a windowed signal x[n]...x[m], and the output, for each of N discrete frequency bands, is a complex number X[k] representing the magnitude and phase of that frequency component in the original signal. If we plot the magnitude against the frequency, we can visualize the spectrum (see Chapter 14 for more on spectra). For example, Fig. 14.28 shows a 25 ms Hamming-windowed portion of a signal and its spectrum as computed by a DFT (with some additional smoothing). Time (s) 0.0141752 0.039295 -0.04121 0.04414 Frequency (Hz) Sound pressure level (dB/Hz) -20 (a) (b) Figure 14.28 (a) A 25 ms Hamming-windowed portion of a signal from the vowel [iy] and (b) its spectrum computed by a DFT. We do not introduce the mathematical details of the DFT here, except to note that …

## Key terms
- **frequency** — 10 mentions
- **signal** — 8 mentions
- **band** — 6 mentions
- **fourier** — 5 mentions
- **recognition** — 4 mentions
- **spectrum** — 4 mentions
- **information** — 4 mentions
- **discrete** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=341|Speech and Language Processing.pdf p. 341]]

## Liens
- Up: [[research/slp/feature-extraction-for-speech-recognition-log-mel-spectrum]]
- ← Prev: [[research/slp/discrete-fourier-transform]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
