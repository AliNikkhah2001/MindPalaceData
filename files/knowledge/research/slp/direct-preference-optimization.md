---
title: "Direct Preference Optimization"
summary: "§I Large Language Models › Post-training: Instruction Tuning,: CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE The second term in this formulation, DKL(πθ(o|x)||πref(o|x)), is the KullbackLeibler (KL) divergence."
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "238-239"
---

# Direct Preference Optimization

§I Large Language Models › Post-training: Instruction Tuning, Alignment, and Test-Time Compute › LLM Alignment via Preference-Based Learning › Direct Preference Optimization · pp. 238–239 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 10 • POST-TRAINING: INSTRUCTION TUNING, ALIGNMENT, AND TEST-TIME COMPUTE The second term in this formulation, DKL(πθ(o|x)||πref(o|x)), is the KullbackLeibler (KL) divergence. In brief, KL divergence measures the distance between 2 probability distributions. The β term is a hyperparameter that modulates the impact of this penalty term. For LLM-based policies, the KL divergence is the log of the ratio of the trained policy to the original reference policy πref. π∗= argmax πθ Ex∼D,o∼πθ (o|x)  rφ(x,o)−β log πθ(o|x) πref(o|x)  (10.6) In the following sections, we’ll explore two learning approaches to aligning LLMs based on this optimization framework. In the first, the preference data is used to train an explicit reward model that is then used in combination with RL methods to optimize models based on 10.6. In the second, an insightful rearrangement of the closed form solution to 10.6 is used to finetune models directly from existing preference data. TBD Direct Preference Optimization (DPO) (Rafailov et al., 2023) employs gradientbased learning to optimize candidate LLMs using preference data, without learning an explicit reward model or sampling from the model being updated. Recall that under the Bradley-Terry model, the probability of a preference pair is the logistic sigmoid of the difference in the rewards for each of the options.

## Key terms
- **model** — 13 mentions
- **preference** — 10 mentions
- **reward** — 10 mentions
- **term** — 9 mentions
- **policy** — 9 mentions
- **learning** — 7 mentions
- **data** — 5 mentions
- **function** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=238|Speech and Language Processing.pdf p. 238]]

## Liens
- Up: [[research/slp/llm-alignment-via-preference-based-learning]]
- ← Prev: [[research/slp/reinforcement-learning-with-preference-feedback-ppo]]
- Next: [[research/slp/evaluation-of-preference-aligned-models]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
