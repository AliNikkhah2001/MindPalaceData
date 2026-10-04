---
title: "Exercises"
summary: "§I Large Language Models › Phonetics and Speech Feature Extra: CHAPTER 14 • PHONETICS AND SPEECH FEATURE EXTRACTION correct unit of a cepstrum is the sample. Examining this cepstrum, we see that there is indeed a large peak around 120, corresponding to the F0 and representing the"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "344-346"
---

# Exercises

§I Large Language Models › Phonetics and Speech Feature Extraction › Exercises · pp. 344–346 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 14 • PHONETICS AND SPEECH FEATURE EXTRACTION correct unit of a cepstrum is the sample. Examining this cepstrum, we see that there is indeed a large peak around 120, corresponding to the F0 and representing the glottal pulse. There are other various components at lower values on the x-axis. These represent the vocal tract filter (the position of the tongue and the other articulators). Thus, if we are interested in detecting phones, we can make use of just the lower cepstral values. If we are interested in detecting pitch, we can use the higher cepstral values. For the purposes of MFCC extraction, we generally just take the first 12 cepstral values. These 12 coefficients will represent information solely about the vocal tract filter, cleanly separated from information about the glottal source. It turns out that cepstral coefficients have the extremely useful property that the variance of the different coefficients tends to be uncorrelated. This is not true for the spectrum, where spectral coefficients at different frequency bands are correlated. For those who have had signal processing, the cepstrum is more formally defined as the inverse DFT of the log magnitude of the DFT of a signal; hence, for a windowed frame of speech x[n], c[n] = N−1 X n=0 log N−1 X n=0 x[n]e−j 2π N kn !

## Key terms
- **phonetic** — 17 mentions
- **feature** — 15 mentions
- **speech** — 10 mentions
- **energy** — 10 mentions
- **cepstral** — 9 mentions
- **phone** — 9 mentions
- **delta** — 9 mentions
- **frame** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=344|Speech and Language Processing.pdf p. 344]]

## Liens
- Up: [[research/slp/phonetics-and-speech-feature-extraction]]
- ← Prev: [[research/slp/historical-notes-13]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
