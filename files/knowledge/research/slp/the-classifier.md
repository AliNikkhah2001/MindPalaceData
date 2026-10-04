---
title: "The classifier"
summary: "§I Large Language Models › Embeddings › Word2vec › The classi: CHAPTER 5 • EMBEDDINGS beddings, meaning that the method learns one fixed embedding for each word in the static embeddings vocabulary."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "114-115"
---

# The classifier

§I Large Language Models › Embeddings › Word2vec › The classifier · pp. 114–115 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 5 • EMBEDDINGS beddings, meaning that the method learns one fixed embedding for each word in the static embeddings vocabulary. In Chapter 9 we’ll introduce methods for learning dynamic contextual embeddings like the popular family of BERT representations, in which the vector for each word is different in different contexts. The intuition of word2vec is that instead of counting how often each context word c occurs near, say, apricot, we’ll instead train a classifier on a binary prediction task: “Is word c likely to show up near apricot?” We don’t actually care about this prediction task; instead we’ll take the learned classifier weights as the word embeddings. The revolutionary intuition here is that we can just use running text as implicitly supervised training data for such a classifier; a word c that occurs near the target word apricot acts as gold ‘correct answer’ to the question “Is word c likely to show up near apricot?” This method, often called self-supervision, avoids the need for self-supervision any sort of hand-labeled supervision signal. This idea was first proposed in the task of neural language modeling, when Bengio et al. (2003) and Collobert et al. (2011) sh…

## Key terms
- **word** — 46 mentions
- **context** — 19 mentions
- **embedding** — 17 mentions
- **probability** — 14 mentions
- **target** — 13 mentions
- **classifier** — 9 mentions
- **apricot** — 8 mentions
- **intuition** — 6 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=114|Speech and Language Processing.pdf p. 114]]

## Liens
- Up: [[research/slp/word2vec]]
- Next: [[research/slp/learning-skip-gram-embeddings]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
