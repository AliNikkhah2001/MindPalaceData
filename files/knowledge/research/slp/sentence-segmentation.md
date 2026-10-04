---
title: "Sentence Segmentation"
summary: "§I Large Language Models › Words and Tokens › Rule-based toke: 2.8 • RULE-BASED TOKENIZATION are interested in studying. Or it can be useful for social science applications where orthographic words are useful domains of study."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "37-37"
---

# Sentence Segmentation

§I Large Language Models › Words and Tokens › Rule-based tokenization › Sentence Segmentation · pp. 37–37 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
2.8 • RULE-BASED TOKENIZATION are interested in studying. Or it can be useful for social science applications where orthographic words are useful domains of study. In rule-based tokenization, we pre-define a standard and implement rules to implement that kind of tokenization. Let’s explore this for English word tokenization. We have some desiderata for English. We often want to break off punctuation as a separate token; commas are a useful piece of information for parsers, and periods help indicate sentence boundaries. But we’ll often want to keep the punctuation that occurs word internally, in examples like m.p.h., Ph.D., AT&T, and cap’n. Special characters and numbers will need to be kept in prices ($45.55) and dates (01/02/06); we don’t want to segment that price into separate tokens of “45” and “55”. And there are URLs (https://www.stanford.edu), Twitter hashtags (#nlproc), or email addresses (someone@cs.colorado.edu). Number expressions introduce complications; in addition to appearing at word boundaries, commas appear inside numbers in English, every three digits: 555,500.50. Tokenization differs by language; languages like Spanish, French, and German, for example, use a comma to mark the decimal point, and spaces (or sometimes periods) where English puts commas, for example, 555 500,50.

## Key terms
- **tokenization** — 11 mentions
- **word** — 8 mentions
- **rule-based** — 5 mentions
- **english** — 5 mentions
- **token** — 5 mentions
- **language** — 5 mentions
- **clitic** — 5 mentions
- **expression** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=37|Speech and Language Processing.pdf p. 37]]

## Liens
- Up: [[research/slp/rule-based-tokenization]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
