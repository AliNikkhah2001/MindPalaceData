---
title: "LLM Alignment via Preference-Based Learning"
summary: "§I Large Language Models › Post-training: Instruction Tuning,: CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE Preference Data: Prompt/output pairs: Preferences: … … Reward Model r(x, oi) r(x, oi) Figure 10.7 Reward model learning with a pretraine"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "236-239"
---

# LLM Alignment via Preference-Based Learning

§I Large Language Models › Post-training: Instruction Tuning, Alignment, and Test-Time Compute › LLM Alignment via Preference-Based Learning · pp. 236–239 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE Preference Data: Prompt/output pairs: Preferences: … … Reward Model r(x, oi) r(x, oi) Figure 10.7 Reward model learning with a pretrained LLM. Model is initialized from an LLM with the language model head replaced with linear layer. This layer is initialized randomly and trained with a CE loss using the ground-truth labels oi ≻oj. linear layer. We then use gradient descent with the loss from 10.3 to learn to score model outputs using the preference training data. Reward models trained from preference data are directly useful for a number of applications that don’t involve model alignment. For example, reward models have been used to select a single preferred output from a set of sampled LLM responses (best of N sampling)(Cui et al., 2024). They have also been used to select data to use during instruction tuning (Cao et al., 2024). Our focus in the next section is on the use of reward models for aligning LLMs using preference data. Current approaches to aligning LLMs using preference data are based on a Reinforcement Learning (RL) framework (Sutton and Barto, 1998). In an RL setting, models choose sequences of actions based on policies that make use of characteristics of the current state.

## Key terms
- **reward** — 37 mentions
- **model** — 36 mentions
- **preference** — 24 mentions
- **data** — 17 mentions
- **policy** — 15 mentions
- **learning** — 13 mentions
- **output** — 12 mentions
- **term** — 10 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=236|Speech and Language Processing.pdf p. 236]]

## Liens
- Up: [[research/slp/post-training-instruction-tuning-alignment-and-test-time-compute]]
- ← Prev: [[research/slp/learning-from-preferences]]
- Next: [[research/slp/test-time-compute]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
