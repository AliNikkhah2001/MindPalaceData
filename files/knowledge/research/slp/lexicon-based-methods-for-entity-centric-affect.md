---
title: "Lexicon-based methods for Entity-Centric Affect"
summary: "§II Annotating Linguistic Structure › Lexicons for Sentiment,: 22.8 • LEXICON-BASED METHODS FOR ENTITY-CENTRIC AFFECT Counts can alternatively be logged or normalized per writer as in Eq."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "525-525"
---

# Lexicon-based methods for Entity-Centric Affect

§II Annotating Linguistic Structure › Lexicons for Sentiment, Affect, and Connotation › Lexicon-based methods for Entity-Centric Affect · pp. 525–525 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
22.8 • LEXICON-BASED METHODS FOR ENTITY-CENTRIC AFFECT Counts can alternatively be logged or normalized per writer as in Eq. 22.14. However they are defined, these lexicon features are then used in a supervised classifier to predict the desired affective category for the text or document. Once a classifier is trained, we can examine which lexicon features are associated with which classes. For a classifier like logistic regression the feature weight gives an indication of how associated the feature is with the class. What if we want to get an affect score not for an entire document, but for a particular entity in the text? The entity-centric method of Field and Tsvetkov (2019) combines affect lexicons with contextual embeddings to assign an affect score to an entity in text. In the context of affect about people, they relabel the Valence/Arousal/Dominance dimension as Sentiment/Agency/Power. The algorithm first trains classifiers to map embeddings to scores: 1. For each word w in the training corpus: (a) Use off-the-shelf pretrained encoders (like BERT) to extract a contextual embedding e for each instance of the word. No additional finetuning is done. (b) Average over the e embeddings of each instance of w to obtain a single embedding vector for one training point w.

## Key terms
- **score** — 10 mentions
- **lexicon** — 9 mentions
- **embedding** — 8 mentions
- **affect** — 6 mentions
- **entity** — 6 mentions
- **text** — 5 mentions
- **word** — 5 mentions
- **classifier** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=525|Speech and Language Processing.pdf p. 525]]

## Liens
- Up: [[research/slp/lexicons-for-sentiment-affect-and-connotation]]
- ← Prev: [[research/slp/using-lexicons-for-affect-recognition]]
- Next: [[research/slp/connotation-frames]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
