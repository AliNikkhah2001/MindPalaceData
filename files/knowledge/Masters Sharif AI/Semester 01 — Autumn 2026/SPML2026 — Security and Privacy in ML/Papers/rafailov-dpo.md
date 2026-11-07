---
title: Direct Preference Optimization (DPO)
summary: Skip explicit RL: optimize the policy directly from preferences with a closed-form objective.
course: SPML2026 — Security and Privacy in ML
tags: [masters, spml, paper, study]
arxiv: "2305.18290"
read: false
---

# Direct Preference Optimization (DPO)

> Skip explicit RL: optimize the policy directly from preferences with a closed-form objective.

## Why this paper (for SPML)
Modern, simpler alignment method next to RLHF.

## Core ideas
- Reparameterize reward → policy.
- Classification-style loss on preference pairs.
- No sampling loop during training.

## How to study it
DPO loss derivation intuition + practical pros/cons vs PPO-RLHF.

## Links
- arXiv: [2305.18290](https://arxiv.org/abs/2305.18290)
- PDF (library): `SPML2026-rafailov-dpo.pdf`
- Papers index: [[index|Papers]]
- Course: [[../index|SPML2026 — Security and Privacy in ML]]

## Linked lectures
- [[../Lectures/2026-12-20 RLHF]]

## Goal
`Masters Sharif AI > Semester 01 — Autumn 2026 > SPML2026 — Security and Privacy in ML > Papers`
