---
title: "Chain-of-Thought Prompting"
summary: "§I Large Language Models › Post-training: Instruction Tuning,: CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE • DPO only incurs the cost of maintaining 2 LLMs during training, as opposed to the 4 models needed for PPO."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "240-240"
---

# Chain-of-Thought Prompting

§I Large Language Models › Post-training: Instruction Tuning, Alignment, and Test-Time Compute › Test-time Compute › Chain-of-Thought Prompting · pp. 240–240 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE • DPO only incurs the cost of maintaining 2 LLMs during training, as opposed to the 4 models needed for PPO. We’ve now seen 3 levels of training for large language models: pretraining, where models learn to predict words, and two kinds of post-training: instruct tuning, where they learn to follow instructions, and preference alignment, where they learn to prefer prompt continuations that are preferred by humans. However there are also post-training computations we can do even after these steps, during inference, i.e., when the model is generating its output. This class of post-training tasks is called test-time compute. We focus here on one representative test-time compute example, chain-of-thought prompting. There is a wide range of techniques to use prompts to improve the performance of language models on many tasks. Here we describe one of them, called chain-ofthought prompting. chain-of- thought The goal of chain-of-thought prompting is to improve performance on difficult reasoning tasks that language models tend to fail on. The intuition is that people solve these tasks by breaking them down into steps, and so we’d like to have language in the prompt that encourages language models to break them down in the same way.

## Key terms
- **model** — 11 mentions
- **language** — 8 mentions
- **steps** — 6 mentions
- **reasoning** — 6 mentions
- **tasks** — 5 mentions
- **prompting** — 5 mentions
- **post-training** — 4 mentions
- **prompt** — 4 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=240|Speech and Language Processing.pdf p. 240]]

## Liens
- Up: [[research/slp/test-time-compute]]
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
