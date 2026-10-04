---
title: "TTS Evaluation"
summary: "§I Large Language Models › Text-to-Speech › TTS Evaluation: We first run the codec to get an acoustic code matrix for y′, which will be CP = C:T ′,: = [c0,:,c1,:,...cT ′,: :]. Next we concatenate the transcription of y′ to the text sequence to be spoken to create the total input "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "383-383"
---

# TTS Evaluation

§I Large Language Models › Text-to-Speech › TTS Evaluation · pp. 383–383 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
16.4 • TTS EVALUATION transcript(y′). We first run the codec to get an acoustic code matrix for y′, which will be CP = C:T ′,: = [c0,:,c1,:,...cT ′,: :]. Next we concatenate the transcription of y′ to the text sequence to be spoken to create the total input text x, which we pass through a text tokenizer. At this stage we thus have a tokenized text x and a tokenized audio prompt CP. Then we generate CT = C>T ′,: = [cT ′+1,:,...cT,:] conditioned on the text sequence x and the prompt CP: CT = argmax CT p(CT|CP,x) = argmax CT TY t=T ′+1 p(ct,:|c<t,:,x) (16.7) Then the generated tokens CT can be converted by the ENCODEC decoder into a waveform. Fig. 16.9 shows the intuition. Figure 16.9 Inference procedure for VALL-E. Figure from Chen et al. (2025). The transcript for the 3 seconds of enrolled speech is first prepended to the text to be generated, and both the speech and text are tokenized. Next the autoregressive transformer starts generating the first codes ct′+1,1 conditioned on the transcript and acoustic prompt. See Chen et al. (2025) for more details on the transformer components and other details of training. TTS systems are evaluated by humans, by playing an utterance to listeners and asking them to give a mean opinion score (MOS), a rating of how good the synthesized MOS utterances are, usually on a scale from 1-5.

## Key terms
- **text** — 7 mentions
- **transcript** — 3 mentions
- **first** — 3 mentions
- **tokenized** — 3 mentions
- **prompt** — 3 mentions
- **acoustic** — 2 mentions
- **code** — 2 mentions
- **next** — 2 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=383|Speech and Language Processing.pdf p. 383]]

## Liens
- Up: [[research/slp/text-to-speech]]
- ← Prev: [[research/slp/vall-e-generating-audio-with-2-stage-lm]]
- Next: [[research/slp/other-speech-tasks]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
