---
title: "Machine Translation using Encoder-Decoder"
summary: "§I Large Language Models › Machine Translation › Machine Tran: 12.2 • MACHINE TRANSLATION USING ENCODER-DECODER may conflate multiple morphemes, like -om in the word stolom (table-SG-INSTRDECL1), which fuses the distinct morphological categories instrumental, singular, and first "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "271-274"
---

# Machine Translation using Encoder-Decoder

§I Large Language Models › Machine Translation › Machine Translation using Encoder-Decoder · pp. 271–274 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
12.2 • MACHINE TRANSLATION USING ENCODER-DECODER may conflate multiple morphemes, like -om in the word stolom (table-SG-INSTRDECL1), which fuses the distinct morphological categories instrumental, singular, and first declension. Translating between languages with rich morphology requires dealing with structure below the word level, and for this reason modern systems generally use subword models like the wordpiece or BPE models of Section 12.2.1. Finally, languages vary along a typological dimension related to the things they tend to omit. Some languages, like English, require that we use an explicit pronoun when talking about a referent that is given in the discourse. In other languages, however, we can sometimes omit pronouns altogether, as the following example from Spanish shows1: (12.6) [El jefe]i dio con un libro. /0i Mostr´o su hallazgo a un descifrador ambulante. [The boss] came upon a book. [He] showed his find to a wandering decoder. Languages that can omit pronouns are called pro-drop languages. Even among pro-drop the pro-drop languages, there are marked differences in frequencies of omission. Japanese and Chinese, for example, tend to omit far more than does Spanish. This dimension of variation across languages is called the dimension of referential density.

## Key terms
- **language** — 39 mentions
- **sentence** — 36 mentions
- **token** — 20 mentions
- **algorithm** — 19 mentions
- **tokenization** — 15 mentions
- **word** — 13 mentions
- **wordpiece** — 13 mentions
- **alignment** — 12 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=271|Speech and Language Processing.pdf p. 271]]

## Liens
- Up: [[research/slp/machine-translation]]
- ← Prev: [[research/slp/language-divergences-and-typology]]
- Next: [[research/slp/details-of-the-encoder-decoder-model]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
