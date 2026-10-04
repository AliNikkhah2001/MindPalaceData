---
title: "Perplexity"
summary: "§I Large Language Models › Large Language Models › Evaluating: CHAPTER 7 • LARGE LANGUAGE MODELS Finetuning Data Pretraining Data Pretraining … … … Fine-tuning … … … Pretrained LM Fine-tuned LM Figure 7.15 Pretraining and finetuning."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "172-172"
---

# Perplexity

§I Large Language Models › Large Language Models › Evaluating Large Language Models › Perplexity · pp. 172–172 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 7 • LARGE LANGUAGE MODELS Finetuning Data Pretraining Data Pretraining … … … Fine-tuning … … … Pretrained LM Fine-tuned LM Figure 7.15 Pretraining and finetuning. A pre-trained model can be finetuned to a particular domain or dataset. There are many different ways to finetune, depending on exactly which parameters are updated from the finetuning data: all the parameters, some of the parameters, or only the parameters of specific extra circuitry, as we’ll see in future chapters. 7.6 Evaluating Large Language Models We can evaluate language models by accuracy (how well they predict unseen text, by how well they perform tasks like answering questions or translating text), or by other factors like how fast they can be run, how much energy they use, or how fair they are. We’ll explore all of these in the next three sections. As we first saw in Chapter 3, one way to evaluate language models is to measure how well they predict unseen text. A better language model is better at predicting upcoming words, and so it will be less surprised by (i.e., assign a higher probability to) each word when it occurs in the test set. If we want to know which of two language models is a better model of some text, we can just see which assigns it a higher probability, or in practice, since we mostly deal with probabilities in log space, we see which assigns a higher log likelihood.

## Key terms
- **model** — 10 mentions
- **text** — 9 mentions
- **language** — 8 mentions
- **probability** — 8 mentions
- **parameters** — 4 mentions
- **word** — 4 mentions
- **likelihood** — 4 mentions
- **token** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=172|Speech and Language Processing.pdf p. 172]]

## Liens
- Up: [[research/slp/evaluating-large-language-models]]
- Next: [[research/slp/downstream-tasks-reasoning-and-world-knowledge]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
