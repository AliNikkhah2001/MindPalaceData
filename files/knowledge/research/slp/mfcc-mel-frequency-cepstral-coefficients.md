---
title: "MFCC: Mel Frequency Cepstral Coefficients"
summary: "§I Large Language Models › Phonetics and Speech Feature Extra: CHAPTER 14 • PHONETICS AND SPEECH FEATURE EXTRACTION et al. 1937, Stevens and Volkmann 1940) is a unit of pitch. Pairs of sounds that are perceptually equidistant in pitch are separated by an equal number of mels."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "342-343"
---

# MFCC: Mel Frequency Cepstral Coefficients

§I Large Language Models › Phonetics and Speech Feature Extraction › MFCC: Mel Frequency Cepstral Coefficients · pp. 342–343 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 14 • PHONETICS AND SPEECH FEATURE EXTRACTION et al. 1937, Stevens and Volkmann 1940) is a unit of pitch. Pairs of sounds that are perceptually equidistant in pitch are separated by an equal number of mels. The mel frequency m can be computed from the raw acoustic frequency by a log transformation: mel(f) = 1127ln(1+ f 700) (14.16) We implement this intuition by creating a bank of filters that collect energy from each frequency band, spread logarithmically so that we have very fine resolution at low frequencies, and less resolution at high frequencies. Figure 14.29 shows a sample bank of triangular filters that implement this idea, that can be multiplied by the spectrum to get a mel spectrum. m1 m2 mM ... mel spectrum 0.5 Amplitude Frequency (Hz) 8K Figure 14.29 The mel filter bank (Davis and Mermelstein, 1980). Each triangular filter, spaced logarithmically along the mel scale, collects energy from a given frequency range. Finally, we take the log of each of the mel spectrum values. The human response to signal level is logarithmic (like the human response to frequency). Humans are less sensitive to slight differences in amplitude at high amplitudes than at low amplitudes. In addition, using a log makes the feature estimates less sensitive to variations in input such as power variations due to the speaker’s mouth moving closer or further from the microphone.

## Key terms
- **spectrum** — 24 mentions
- **frequency** — 21 mentions
- **cepstrum** — 11 mentions
- **filter** — 9 mentions
- **coefficient** — 9 mentions
- **amplitude** — 8 mentions
- **energy** — 6 mentions
- **signal** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=342|Speech and Language Processing.pdf p. 342]]

## Liens
- Up: [[research/slp/phonetics-and-speech-feature-extraction]]
- ← Prev: [[research/slp/feature-extraction-for-speech-recognition-log-mel-spectrum]]
- Next: [[research/slp/summary-13]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
