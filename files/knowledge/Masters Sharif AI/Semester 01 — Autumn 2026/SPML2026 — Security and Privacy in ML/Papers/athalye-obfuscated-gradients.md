---
title: Obfuscated Gradients Give a False Sense of Security
summary: Many ‘robust’ defenses only break gradients; BPDA/EOT/etc. recover strong attacks.
course: SPML2026 — Security and Privacy in ML
tags: [masters, spml, paper, study]
arxiv: "1802.00420"
read: false
---

# Obfuscated Gradients Give a False Sense of Security

> Many ‘robust’ defenses only break gradients; BPDA/EOT/etc. recover strong attacks.

## Why this paper (for SPML)
The paper that kills gradient-masking theater—read before trusting any empirical defense.

## Core ideas
- Shattered / stochastic / vanishing gradients as obfuscation.
- **BPDA**: approximate backward pass through non-diff defenses.
- Always try adaptive white-box evaluation.

## How to study it
Taxonomy of obfuscation + how each is circumvented.

## Links
- arXiv: [1802.00420](https://arxiv.org/abs/1802.00420)
- PDF (library): `SPML2026-athalye-obfuscated-gradients.pdf`
- Papers index: [[index|Papers]]
- Course: [[../index|SPML2026 — Security and Privacy in ML]]

## Linked lectures
- [[../Lectures/2026-11-15 Obfuscated Gradients & Empirical Defenses]]

## Goal
`Masters Sharif AI > Semester 01 — Autumn 2026 > SPML2026 — Security and Privacy in ML > Papers`
