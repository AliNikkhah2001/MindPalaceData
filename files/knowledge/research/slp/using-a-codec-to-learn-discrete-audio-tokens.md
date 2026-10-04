---
title: "Using a codec to learn discrete audio tokens"
summary: "§I Large Language Models › Text-to-Speech › Using a codec to : 16.2 • USING A CODEC TO LEARN DISCRETE AUDIO TOKENS scribe in the next section. Codecs have three parts: an encoder (that turns speech into embedding vectors), a quantizer (that turns the embeddings into discrete toke"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "375-380"
---

# Using a codec to learn discrete audio tokens

§I Large Language Models › Text-to-Speech › Using a codec to learn discrete audio tokens · pp. 375–380 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
16.2 • USING A CODEC TO LEARN DISCRETE AUDIO TOKENS scribe in the next section. Codecs have three parts: an encoder (that turns speech into embedding vectors), a quantizer (that turns the embeddings into discrete tokens) and decoders (that turns the discrete tokens back into speech). 2. The 2-stage conditional language model that can generate audio tokens corresponding to the desired text. We’ll sketch this in Section 16.3. Modern TTS systems are based around converting the waveform into a sequence of discrete audio tokens. This idea of manipulating discrete audio tokens is also useful for other speech-enabled systems like spoken language models, which take text or speech input and can generate text or speech output to solve tasks like speechto-speech translation, diarization, or spoken question answering. Having discrete tokens means that we can make use of language model technology, since language models are specialized for sequences of discrete tokens. Audio tokenizers are thus an important component of the modern speech toolkit. The standard way to learn audio tokens is from a neural audio codec (the word codec is formed from coder/decoder). Historically a codec was a hardware device that digitized analog symbols.

## Key terms
- **vector** — 47 mentions
- **speech** — 24 mentions
- **discrete** — 23 mentions
- **waveform** — 20 mentions
- **audio** — 19 mentions
- **tokens** — 19 mentions
- **cluster** — 18 mentions
- **embedding** — 17 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=375|Speech and Language Processing.pdf p. 375]]

## Liens
- Up: [[research/slp/text-to-speech]]
- ← Prev: [[research/slp/tts-overview]]
- Next: [[research/slp/vall-e-generating-audio-with-2-stage-lm]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
