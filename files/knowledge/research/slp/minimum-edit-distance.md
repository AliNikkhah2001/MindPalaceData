---
title: "Minimum Edit Distance"
summary: "§I Large Language Models › Words and Tokens › Minimum Edit Di: CHAPTER 2 • WORDS AND TOKENS >>> text = ’That U.S.A. poster-print costs $12.40...’ >>> pattern = r’’’(?x) # set flag to allow verbose regexps ..."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "38-42"
---

# Minimum Edit Distance

§I Large Language Models › Words and Tokens › Minimum Edit Distance · pp. 38–42 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 2 • WORDS AND TOKENS >>> text = ’That U.S.A. poster-print costs $12.40...’ >>> pattern = r’’’(?x) # set flag to allow verbose regexps ... (?:[A-Z]\.)+ # abbreviations, e.g. U.S.A. ... | \w+(?:-\w+)* # words with optional internal hyphens ... | \$?\d+(?:\.\d+)?%? # currency, percentages, e.g. $12.40, 82% ... | \.\.\. # ellipsis ... | [][.,;"’?():_‘-] # these are separate tokens; includes ], [ ... ’’’ >>> nltk.regexp_tokenize(text, pattern) [’That’, ’U.S.A.’, ’poster-print’, ’costs’, ’$12.40’, ’...’] Figure 2.16 A Python trace of regular expression tokenization in the NLTK Python-based natural language processing toolkit (Bird et al., 2009), commented for readability; the (?x) verbose flag tells Python to strip comments and whitespace. Figure from Chapter 3 of Bird et al. (2009). Rule-based segmentation is commonly used for another kind of tokenization process: the sentence. Sentence segmentation is a step that is can be optionally applied sentence segmentation in text processing. It is especially important when applying NLP algorithms to tasks of detecting structure, like parse structure. Sentence segmentation depends on the language and the genre. The most useful cues for segmenting a text into sentences in English written text tend to be punctuation, like periods, question marks, and exclamation points.

## Key terms
- **distance** — 30 mentions
- **string** — 27 mentions
- **edit** — 23 mentions
- **sentence** — 16 mentions
- **minimum** — 16 mentions
- **algorithm** — 15 mentions
- **cost** — 15 mentions
- **substitution** — 12 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=38|Speech and Language Processing.pdf p. 38]]

## Liens
- Up: [[research/slp/words-and-tokens]]
- ← Prev: [[research/slp/rule-based-tokenization]]
- Next: [[research/slp/summary]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
