---
title: "Instruction Tuning"
summary: "§I Large Language Models › Post-training: Instruction Tuning,: 10.1 • INSTRUCTION TUNING need for models to be helpful and non-harmful. To address these two problems, language models include two additional kinds of training for model alignment: methods designed to adjust LLMs to "
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "227-231"
---

# Instruction Tuning

§I Large Language Models › Post-training: Instruction Tuning, Alignment, and Test-Time Compute › Instruction Tuning · pp. 227–231 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
10.1 • INSTRUCTION TUNING need for models to be helpful and non-harmful. To address these two problems, language models include two additional kinds of training for model alignment: methods designed to adjust LLMs to better align model alignment them to human needs for models to be helpful and non-harmful. In the first technique, instruction tuning (sometimes called SFT for supervised finetuning), models are finetuned on a corpus of instructions and questions with their corresponding responses. We’ll describe this in the next section. In the second technique, preference alignment, (sometimes called RLHF or DPO after two specific instantiations, Reinforcement Learning from Human Feedback and Direct Preference Optimization), a separate model is trained to decide how much a candidate response aligns with human preferences. This model is then used to finetune the base model. We’ll describe preference alignment in Section 10.2. We’ll use the term base model to mean a model that has been pretrained but base model hasn’t yet been aligned either by instruction tuning or preference alignment. And aligned we refer to these steps as post-training, meaning that they apply after the model has post-training been pretrained.

## Key terms
- **instruction** — 42 mentions
- **model** — 28 mentions
- **task** — 22 mentions
- **finetuning** — 21 mentions
- **tuning** — 20 mentions
- **language** — 16 mentions
- **question** — 16 mentions
- **training** — 15 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=227|Speech and Language Processing.pdf p. 227]]

## Liens
- Up: [[research/slp/post-training-instruction-tuning-alignment-and-test-time-compute]]
- Next: [[research/slp/learning-from-preferences]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
