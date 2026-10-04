---
title: "Sequence-Pair Classification"
summary: "§I Large Language Models › Masked Language Models › Fine-Tuni: CHAPTER 9 • MASKED LANGUAGE MODELS sequences labeled with the appropriate sentiment class. Training proceeds in the usual way; cross-entropy loss between the softmax output and the correct answer is used to drive the "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "220-220"
---

# Sequence-Pair Classification

§I Large Language Models › Masked Language Models › Fine-Tuning for Classification › Sequence-Pair Classification · pp. 220–220 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 9 • MASKED LANGUAGE MODELS sequences labeled with the appropriate sentiment class. Training proceeds in the usual way; cross-entropy loss between the softmax output and the correct answer is used to drive the learning that produces WC. This loss can be used to not only learn the weights of the classifier, but also to update the weights for the pretrained language model itself. In practice, reasonable classification performance is typically achieved with only minimal changes to the language model parameters, often limited to updates over the final few layers of the transformer. Fig. 9.9 illustrates this overall approach to sequence classification. [CLS] entirely predictable and lacks energy Bidirectional Transformer Encoder hCLS E i + E i + E i + E i + E i + E i + head WC y Figure 9.9 Sequence classification with a bidirectional transformer encoder. The output vector for the [CLS] token serves as input to a simple classifier. As mentioned in Section 9.2.2, an important type of problem involves the classification of pairs of input sequences. Practical applications that fall into this class include paraphrase detection (are the two sentences paraphrases of each other?), logical entailment (does sentence A logically entail sentence B?), and discourse coherence (how coherent is sentence B as a follow-on to sentence A?).

## Key terms
- **classification** — 8 mentions
- **sentence** — 8 mentions
- **model** — 7 mentions
- **language** — 6 mentions
- **sequence** — 5 mentions
- **input** — 5 mentions
- **pair** — 5 mentions
- **output** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=220|Speech and Language Processing.pdf p. 220]]

## Liens
- Up: [[research/slp/fine-tuning-for-classification]]
- ← Prev: [[research/slp/sequence-classification]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
