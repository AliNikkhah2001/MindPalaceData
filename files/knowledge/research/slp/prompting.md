---
title: "Prompting"
summary: "§I Large Language Models › Large Language Models › Prompting: 7.3 • PROMPTING We’ll talk in future sections about all the details, but in this section our goal is just to establish the intuition."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "159-161"
---

# Prompting

§I Large Language Models › Large Language Models › Prompting · pp. 159–161 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
7.3 • PROMPTING We’ll talk in future sections about all the details, but in this section our goal is just to establish the intuition. How can simply computing the probability of the next token help an LLM do all sorts of different language-related tasks? Imagine we want to do a classification tasks like sentiment analysis. We can treat this as conditional generation by giving a language model a context like: The sentiment of the sentence ‘‘I like Jackie Chan" is: and comparing the conditional probability of the following token “positive” and the following token “negative” to see which is higher. That is, as sketched in Fig. 7.4, we compare these two probabilities: P(“positive”|“The sentiment of the sentence ‘I like Jackie Chan’ is:”) P(“negative”|“The sentiment of the sentence ‘I like Jackie Chan’ is:”) If the token “positive” is more probable, we could say the sentiment of the sen- ? ? “positive” “negative” Transformer (or other decoder) The sentiment of the sentence “I like Jackie Chan” is: prob Figure 7.4 Computing the probabilities of the tokens positive and negative occurring after this prefix. tence is positive, otherwise if the token “negative” is more probable we say the sentiment is negative.

## Key terms
- **prompt** — 25 mentions
- **model** — 21 mentions
- **token** — 18 mentions
- **language** — 16 mentions
- **question** — 15 mentions
- **answer** — 14 mentions
- **demonstrations** — 12 mentions
- **task** — 11 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=159|Speech and Language Processing.pdf p. 159]]

## Liens
- Up: [[research/slp/large-language-models]]
- ← Prev: [[research/slp/conditional-generation-of-text-the-intuition]]
- Next: [[research/slp/generation-and-sampling]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
