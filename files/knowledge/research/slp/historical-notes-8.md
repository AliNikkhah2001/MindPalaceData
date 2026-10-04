---
title: "Historical Notes"
summary: "§I Large Language Models › Masked Language Models › Historica: CHAPTER 9 • MASKED LANGUAGE MODELS Tokenization and NER Note that supervised training data for NER is typically in the form of BIO tags associated with text segmented at the word level."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "224-225"
---

# Historical Notes

§I Large Language Models › Masked Language Models › Historical Notes · pp. 224–225 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 9 • MASKED LANGUAGE MODELS Tokenization and NER Note that supervised training data for NER is typically in the form of BIO tags associated with text segmented at the word level. For example the following sentence containing two named entities: [LOC Mt. Sanitas ] is in [LOC Sunshine Canyon] . would have the following set of per-word BIO tags. (9.14) Mt. B-LOC Sanitas I-LOC is O in O Sunshine B-LOC Canyon I-LOC . O Unfortunately, the sequence of WordPiece tokens for this sentence doesn’t align directly with BIO tags in the annotation: ’Mt’, ’.’, ’San’, ’##itas’, ’is’, ’in’, ’Sunshine’, ’Canyon’ ’.’ To deal with this misalignment, we need a way to assign BIO tags to subword tokens during training and a corresponding way to recover word-level tags from subwords during decoding. For training, we can just assign the gold-standard tag associated with each word to all of the subword tokens derived from it. For decoding, the simplest approach is to use the argmax BIO tag associated with the first subword token of a word. Thus, in our example, the BIO tag assigned to “Mt” would be assigned to “Mt.” and the tag assigned to “San” would be assigned to “Sanitas”, effectively ignoring the information in the tags assigned to “.” and “##itas”.

## Key terms
- **model** — 9 mentions
- **word** — 8 mentions
- **language** — 6 mentions
- **tags** — 6 mentions
- **token** — 6 mentions
- **training** — 5 mentions
- **named** — 5 mentions
- **subword** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=224|Speech and Language Processing.pdf p. 224]]

## Liens
- Up: [[research/slp/masked-language-models]]
- ← Prev: [[research/slp/summary-8]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
