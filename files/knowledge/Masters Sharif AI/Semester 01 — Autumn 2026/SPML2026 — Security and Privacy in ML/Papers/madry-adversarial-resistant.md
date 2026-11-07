---
title: Towards Deep Learning Models Resistant to Adversarial Attacks
summary: Robustness as a **min-max** game; PGD is a universal first-order adversary; adversarial training against PGD.
course: SPML2026 — Security and Privacy in ML
tags: [masters, spml, paper, study]
arxiv: "1706.06083"
read: false
---

# Towards Deep Learning Models Resistant to Adversarial Attacks

> Robustness as a **min-max** game; PGD is a universal first-order adversary; adversarial training against PGD.

## Why this paper (for SPML)
Canonical robust-training paper; also used when discussing defenses that fail under adaptive attacks.

## Core ideas
- Inner max ≈ PGD in ℓ_∞/ℓ_2 balls.
- Outer min = train on worst-case perturbations.
- Capacity and threat model must match the evaluation.

## How to study it
Threat model section + PGD algorithm; remember evaluation must use the same norm budget.

## Links
- arXiv: [1706.06083](https://arxiv.org/abs/1706.06083)
- PDF (library): `SPML2026-madry-adversarial-resistant.pdf`
- Papers index: [[index|Papers]]
- Course: [[../index|SPML2026 — Security and Privacy in ML]]

## Linked lectures
- [[../Lectures/2026-11-03 Iterative Adversarial Attacks]]
- [[../Lectures/2026-11-15 Obfuscated Gradients & Empirical Defenses]]

## Goal
`Masters Sharif AI > Semester 01 — Autumn 2026 > SPML2026 — Security and Privacy in ML > Papers`
