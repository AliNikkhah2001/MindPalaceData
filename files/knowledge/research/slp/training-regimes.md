---
title: "Training Regimes"
summary: "§I Large Language Models › Masked Language Models › Training : 9.2 • TRAINING BIDIRECTIONAL ENCODERS X is actually formed by summing 3 embeddings: word, position, and first/second segment embeddings."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "213-213"
---

# Training Regimes

§I Large Language Models › Masked Language Models › Training Bidirectional Encoders › Training Regimes · pp. 213–213 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
9.2 • TRAINING BIDIRECTIONAL ENCODERS X is actually formed by summing 3 embeddings: word, position, and first/second segment embeddings. During training, the output vector hL CLS from the final layer associated with the [CLS] token represents the next sentence prediction. As with the MLM objective, we add a special head, in this case an NSP head, which consists of a learned set of classification weights WNSP ∈Rd×2 that produces a two-class prediction from the raw [CLS] vector hL CLS: yi = softmax(hL CLSWNSP) Cross entropy is used to compute the NSP loss for each sentence pair presented to the model. Fig. 9.4 illustrates the overall NSP training setup. In BERT, the NSP loss was used in conjunction with the MLM training objective to form final loss. Cancel my flight [SEP] CE Loss And the Bidirectional Transformer Encoder p1 p2 p3 p4 p5 p6 p7 p8 [CLS] + + s1 NSP Head Token + Segment + Positional Embeddings hotel p9 [SEP] + + s1 s1 s1 s1 s2 s2 s2 s2 + + + + + + + + + + + + + + hCLS Figure 9.4 An example of the NSP loss calculation. BERT and other early transformer-based language models were trained on about 3.3 billion words (a combination of English Wikipedia and a corpus of book texts called BooksCorpus (Zhu et al., 2015) that is no longer used for intellectual property reasons).

## Key terms
- **loss** — 8 mentions
- **model** — 7 mentions
- **token** — 6 mentions
- **training** — 5 mentions
- **embeddings** — 4 mentions
- **final** — 4 mentions
- **sentence** — 4 mentions
- **pair** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=213|Speech and Language Processing.pdf p. 213]]

## Liens
- Up: [[research/slp/training-bidirectional-encoders]]
- ← Prev: [[research/slp/next-sentence-prediction]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
