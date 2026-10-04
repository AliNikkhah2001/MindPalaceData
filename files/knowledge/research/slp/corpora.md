---
title: "Corpora"
summary: "§I Large Language Models › Words and Tokens › Corpora: 2.5 • CORPORA Some of these are related to preprocessing steps. As we mentioned briefly above, language models usually create their tokens in a pretokenization stage that first segpretokenization ments the input using regular"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "25-26"
---

# Corpora

§I Large Language Models › Words and Tokens › Corpora · pp. 25–26 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
2.5 • CORPORA Some of these are related to preprocessing steps. As we mentioned briefly above, language models usually create their tokens in a pretokenization stage that first segpretokenization ments the input using regular expressions, for example breaking the input at spaces and punctuation, stripping off clitics, and breaking numbers into sets of digits. We’ll see how to use regular expressions in Section 2.6. It’s possible to change this pretokenization to allow BPE tokens to span multiple words. For example the SuperBPE (Liu et al., 2025) and BoundlessBPE (Schmidt SuperBPE BoundlessBPE et al., 2025) algorithms first induce regular BPE subword tokens by enforcing pretokenization. They then run a second stage of BPE allowing merges across spaces and punctuation. The result is a large set of tokens that can be more efficient (Fig. 2.7). Figure 2.7 The SuperBPE algorithm creating larger tokens by allowing a second stage of merging across spaces. Figure from Liu et al. (2025). Many of the tokenizers used in practice for large language models are multilingual, trained on many languages. But because the training data for large language models is vastly dominated by English text, these multilingual BPE tokenizers tend to use most of the tokens for English, leaving fewer of them for other languages.

## Key terms
- **language** — 25 mentions
- **english** — 13 mentions
- **token** — 13 mentions
- **text** — 11 mentions
- **word** — 9 mentions
- **algorithm** — 7 mentions
- **models** — 6 mentions
- **specific** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=25|Speech and Language Processing.pdf p. 25]]

## Liens
- Up: [[research/slp/words-and-tokens]]
- ← Prev: [[research/slp/subword-tokenization-byte-pair-encoding]]
- Next: [[research/slp/regular-expressions]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
