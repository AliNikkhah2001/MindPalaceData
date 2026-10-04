---
title: "The Language Modeling Head"
summary: "§I Large Language Models › Transformers › The Language Modeli: 8.5 • THE LANGUAGE MODELING HEAD positions, like the fact that position 4 in an input is more closely related to position 5 than it is to position 17."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "197-197"
---

# The Language Modeling Head

§I Large Language Models › Transformers › The Language Modeling Head · pp. 197–197 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
8.5 • THE LANGUAGE MODELING HEAD positions, like the fact that position 4 in an input is more closely related to position 5 than it is to position 17. A more complex style of positional embedding methods extend this idea of capturing relationships even further to directly represent relative position instead of relative position absolute position, often implemented in the attention mechanism at each layer rather than being added once at the initial input. The last component of the transformer we must introduce is the language modeling head. Here we are using the word head to mean the additional neural circuitry we language modeling head head add on top of the basic transformer architecture when we apply pretrained transformer models to various tasks. The language modeling head is the circuitry we need to do language modeling. Recall that language models, from the simple n-gram models of Chapter 3 through the feedforward and RNN language models of Chapter 6 and Chapter 13, are word predictors. Given a context of words, they assign a probability to each possible next word. For example, if the preceding context is “Thanks for all the” and we want to know how likely the next word is “fish” we would compute: P(fish|Thanks for all the) Language models give us the ability to assign such a conditional probability to every possible next word, giving us a distribution over the entire vocabulary.

## Key terms
- **language** — 12 mentions
- **word** — 12 mentions
- **model** — 10 mentions
- **position** — 9 mentions
- **head** — 8 mentions
- **embedding** — 8 mentions
- **shape** — 8 mentions
- **transformer** — 7 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=197|Speech and Language Processing.pdf p. 197]]

## Liens
- Up: [[research/slp/transformers]]
- ← Prev: [[research/slp/the-input-embeddings-for-token-and-position]]
- Next: [[research/slp/more-on-sampling]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
