---
title: "Supervised Learning of Word Sentiment"
summary: "§II Annotating Linguistic Structure › Lexicons for Sentiment,: CHAPTER 22 • LEXICONS FOR SENTIMENT, AFFECT, AND CONNOTATION fair but brutal Another cue to opposite polarity comes from morphological negation (un-, im-, -less)."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "518-522"
---

# Supervised Learning of Word Sentiment

§II Annotating Linguistic Structure › Lexicons for Sentiment, Affect, and Connotation › Supervised Learning of Word Sentiment · pp. 518–522 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 22 • LEXICONS FOR SENTIMENT, AFFECT, AND CONNOTATION fair but brutal Another cue to opposite polarity comes from morphological negation (un-, im-, -less). Adjectives with the same root but differing in a morphological negative (adequate/inadequate, thoughtful/thoughtless) tend to be of opposite polarity. Yet another method for finding words that have a similar polarity to seed words is to make use of a thesaurus like WordNet (Kim and Hovy 2004, Hu and Liu 2004). A word’s synonyms presumably share its polarity while a word’s antonyms probably have the opposite polarity. After a seed lexicon is built, each lexicon is updated as follows, possibly iterated. Lex+: Add synonyms of positive words (well) and antonyms (like fine) of negative words Lex−: Add synonyms of negative words (awful) and antonyms (like evil) of positive An extension of this algorithm assigns polarity to WordNet senses, called SentiWordNet (Baccianella et al., 2010). Fig. 22.8 shows some examples. SentiWordNet Synset Pos Neg Obj good#6 ‘agreeable or pleasing’ respectable#2 honorable#4 good#4 estimable#2 ‘deserving of esteem’ 0.75 0.25 estimable#3 computable#1 ‘may be computed or estimated’ sting#1 burn#4 bite…

## Key terms
- **word** — 49 mentions
- **review** — 20 mentions
- **positive** — 18 mentions
- **negative** — 17 mentions
- **rating** — 13 mentions
- **star** — 12 mentions
- **potts** — 12 mentions
- **polarity** — 11 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=518|Speech and Language Processing.pdf p. 518]]

## Liens
- Up: [[research/slp/lexicons-for-sentiment-affect-and-connotation]]
- ← Prev: [[research/slp/semi-supervised-induction-of-affect-lexicons]]
- Next: [[research/slp/using-lexicons-for-sentiment-recognition]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
