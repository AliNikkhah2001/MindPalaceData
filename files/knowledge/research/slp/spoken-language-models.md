---
title: "Spoken Language Models"
summary: "§I Large Language Models › Text-to-Speech › Spoken Language M: CHAPTER 16 • TEXT-TO-SPEECH If we are comparing exactly two systems (perhaps to see if a particular change actually improved the system), we can also compare using CMOS (Comparative CMOS MOS)."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "384-384"
---

# Spoken Language Models

§I Large Language Models › Text-to-Speech › Spoken Language Models · pp. 384–384 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 16 • TEXT-TO-SPEECH If we are comparing exactly two systems (perhaps to see if a particular change actually improved the system), we can also compare using CMOS (Comparative CMOS MOS). where users give their preference on which of the two utterances is better. CMOS scores range from -3 (the system is much worse than the reference) to 3 (the system is better than the reference) Here we play the same sentence synthesized by two different systems. The human listeners choose which of the two utterances they like better. We do this for say 50 sentences (presented in random order) and compare the number of sentences preferred for each system. Although speech synthesis systems are best evaluated by human listeners, some automatic metrics can be used to add more information. For example we can run the output through an ASR system and compute the word error rate (WER) to see how robust the synthesized output is. Or for measuring how well the voice output of the TTS system matches the enrolled voice, we can treat the task as if it were speaker verification, passing the two voices to a speaker verification system and using the resulting score as a similarity score. There are a wide variety of other speech-related tasks.

## Key terms
- **speaker** — 16 mentions
- **system** — 12 mentions
- **word** — 7 mentions
- **task** — 6 mentions
- **wake** — 6 mentions
- **speech** — 5 mentions
- **voice** — 5 mentions
- **verification** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=384|Speech and Language Processing.pdf p. 384]]

## Liens
- Up: [[research/slp/text-to-speech]]
- ← Prev: [[research/slp/other-speech-tasks]]
- Next: [[research/slp/summary-15]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
