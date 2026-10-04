---
title: "TTS overview"
summary: "§I Large Language Models › Text-to-Speech › TTS overview: CHAPTER 16 • TEXT-TO-SPEECH The task of text-to-speech is to generate a speech waveform that corresponds to a desired text, using in a particular voice specified by the user."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "374-374"
---

# TTS overview

§I Large Language Models › Text-to-Speech › TTS overview · pp. 374–374 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 16 • TEXT-TO-SPEECH The task of text-to-speech is to generate a speech waveform that corresponds to a desired text, using in a particular voice specified by the user. Historically TTS was done by collecting hundreds of hours of speech from a single talker in a lab and training a large system on it. The resulting TTS system only worked in one voice; if you wanted a second voice, you went back and collected data from a second talker. The modern method is instead to train a speaker-independent synthesizer on tens of thousands of hours of speech from thousands of talkers. To create speech in a new voice unseen in training, we use a very small amount of speech from the desired talker to guide the creation of the voice. So the input to a modern TTS system is a text prompt and perhaps 3 seconds of speech from the voice we’d like to generate the speech in. This TTS task is called zero-shot TTS because the desired voice may zero-shot TTS never have been seen in training. The way modern TTS systems address this task is to use language modeling, and in particular conditional generation. The intuition is to take an enormous dataset of speech, and use an audio tokenizer based on an audio codec to induce discrete audio tokens from that speech that represent the speech.

## Key terms
- **speech** — 15 mentions
- **voice** — 9 mentions
- **desired** — 7 mentions
- **text** — 7 mentions
- **system** — 7 mentions
- **audio** — 7 mentions
- **tokens** — 7 mentions
- **talker** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=374|Speech and Language Processing.pdf p. 374]]

## Liens
- Up: [[research/slp/text-to-speech]]
- Next: [[research/slp/using-a-codec-to-learn-discrete-audio-tokens]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
