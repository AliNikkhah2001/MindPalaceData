---
title: "Interpretation of Phones from a Waveform"
summary: "§I Large Language Models › Phonetics and Speech Feature Extra: CHAPTER 14 • PHONETICS AND SPEECH FEATURE EXTRACTION The loudness of a sound is the perceptual correlate of the power. So sounds with higher amplitudes are perceived as louder, but again the relationship is not linear"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "332-332"
---

# Interpretation of Phones from a Waveform

§I Large Language Models › Phonetics and Speech Feature Extraction › Acoustic Phonetics and Signals › Interpretation of Phones from a Waveform · pp. 332–332 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 14 • PHONETICS AND SPEECH FEATURE EXTRACTION The loudness of a sound is the perceptual correlate of the power. So sounds with higher amplitudes are perceived as louder, but again the relationship is not linear. First of all, as we mentioned above when we defined µ-law compression, humans have greater resolution in the low-power range; the ear is more sensitive to small power differences. Second, it turns out that there is a complex relationship between power, frequency, and perceived loudness; sounds in certain frequency ranges are perceived as being louder than those in other frequency ranges. Various algorithms exist for automatically extracting F0. In a slight abuse of terminology, these are called pitch extraction algorithms. The autocorrelation method pitch extraction of pitch extraction, for example, correlates the signal with itself at various offsets. The offset that gives the highest correlation gives the period of the signal. There are various publicly available pitch extraction toolkits; for example, an augmented autocorrelation pitch tracker is provided with Praat (Boersma and Weenink, 2005). Much can be learned from a visual inspection of a waveform. For example, vowels are pretty easy to spot.

## Key terms
- **waveform** — 6 mentions
- **extraction** — 5 mentions
- **pitch** — 5 mentions
- **amplitude** — 5 mentions
- **sound** — 4 mentions
- **vowels** — 4 mentions
- **baby** — 4 mentions
- **loudness** — 3 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=332|Speech and Language Processing.pdf p. 332]]

## Liens
- Up: [[research/slp/acoustic-phonetics-and-signals]]
- ← Prev: [[research/slp/frequency-and-amplitude-pitch-and-loudness]]
- Next: [[research/slp/spectra-and-the-frequency-domain]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
