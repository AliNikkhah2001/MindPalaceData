---
title: "Bias and Ethical Issues"
summary: "§I Large Language Models › Machine Translation › Bias and Eth: 12.7 • BIAS AND ETHICAL ISSUES recent metrics use BERT or other embeddings to implement this intuition. For example, in some situations we might have datasets that have human assessments of translation quality."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "287-287"
---

# Bias and Ethical Issues

§I Large Language Models › Machine Translation › Bias and Ethical Issues · pp. 287–287 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
12.7 • BIAS AND ETHICAL ISSUES recent metrics use BERT or other embeddings to implement this intuition. For example, in some situations we might have datasets that have human assessments of translation quality. Such datasets consists of tuples (x, ˜x,r), where x = (x1,...,xn) is a reference translation, ˜x = (˜x1,..., ˜xm) is a candidate machine translation, and r ∈R is a human rating that expresses the quality of ˜x with respect to x. Given such data, algorithms like COMET (Rei et al., 2020) BLEURT (Sellam et al., 2020) train a predictor on the human-labeled datasets, for example by passing x and ˜x through a version of BERT (trained with extra pretraining, and then finetuned on the human-labeled sentences), followed by a linear layer that is trained to predict r. The output of such models correlates highly with human labels. In other cases, however, we don’t have such human-labeled datasets. In that case we can measure the similarity of x and ˜x by the similarity of their embeddings. The BERTSCORE algorithm (Zhang et al., 2020) shown in Fig. 12.11, for example, passes the reference x and the candidate ˜x through BERT, computing a BERT embedding for each token xi and ˜xj. Each pair of tokens (xi, ˜xj) is scored by its cosine xi·˜x j |xi||˜x j|.

## Key terms
- **token** — 9 mentions
- **reference** — 6 mentions
- **gender** — 6 mentions
- **candidate** — 5 mentions
- **bert** — 4 mentions
- **datasets** — 4 mentions
- **translation** — 4 mentions
- **similarity** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=287|Speech and Language Processing.pdf p. 287]]

## Liens
- Up: [[research/slp/machine-translation]]
- ← Prev: [[research/slp/mt-evaluation]]
- Next: [[research/slp/summary-11]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
