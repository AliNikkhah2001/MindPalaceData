---
title: "Post-training: Instruction Tuning, Alignment, and Test-Time Compute"
summary: "§I Large Language Models › Post-training: Instruction Tuning,: CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE CHAPTER Post-training: Instruction Tuning, Alignment, and Test-Time Compute “Hal,” said Bowman, now speaking with an icy calm."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "226-242"
---

# Post-training: Instruction Tuning, Alignment, and Test-Time Compute

§I Large Language Models › Post-training: Instruction Tuning, Alignment, and Test-Time Compute · pp. 226–242 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE CHAPTER Post-training: Instruction Tuning, Alignment, and Test-Time Compute “Hal,” said Bowman, now speaking with an icy calm. “I am not incapacitated. Unless you obey my instructions, I shall be forced to disconnect you.” Arthur C. Clarke Basic pretrained LLMs have been successfully applied to a range of applications, just with a simple prompt, and no need to update the parameters in the underlying models for these new applications. Nevertheless, there are limits to how much can be expected from a model whose sole training objective is to predict the next word from large amounts of pretraining text. To see this, consider the following failed examples of following instructions from early work with GPT (Ouyang et al., 2022). Prompt: Explain the moon landing to a six year old in a few sentences. Output: Explain the theory of gravity to a 6 year old. Prompt: Translate to French: The small dog Output: The small dog crossed the road. Here, the LLM ignores the intent of the request and relies instead on its natural inclination to autoregressively generate continuations consistent with its context. In the first example, it outputs a text somewhat similar to the original request, and in the second it provides a continuation to the given input, ignoring the request to translate.

## Key terms
- **instruction** — 44 mentions
- **model** — 31 mentions
- **tuning** — 21 mentions
- **finetuning** — 21 mentions
- **task** — 17 mentions
- **language** — 16 mentions
- **training** — 15 mentions
- **data** — 13 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=226|Speech and Language Processing.pdf p. 226]]

## Liens
- Up: [[research/slp/i-large-language-models]]
- ← Prev: [[research/slp/masked-language-models]]
- Next: [[research/slp/retrieval-based-models]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
