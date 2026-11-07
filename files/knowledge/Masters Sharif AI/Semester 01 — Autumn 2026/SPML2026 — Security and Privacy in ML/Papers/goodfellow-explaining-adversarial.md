---
title: Explaining and Harnessing Adversarial Examples
summary: Linearity in high dimension explains AEs; FGSM crafts them cheaply; adversarial training helps.
course: SPML2026 — Security and Privacy in ML
tags: [masters, spml, paper, study]
arxiv: "1412.6572"
read: false
---

# Explaining and Harnessing Adversarial Examples

> Linearity in high dimension explains AEs; FGSM crafts them cheaply; adversarial training helps.

## Why this paper (for SPML)
The practical attack/defense starter kit before PGD and C&W.

## Core ideas
- **FGSM**: one-step sign of loss gradient.
- Linear view: small ε accumulates across many dimensions.
- Adversarial training as a regularizer (early form).

## How to study it
FGSM derivation + experiments; compare later to iterative PGD.

## Links
- arXiv: [1412.6572](https://arxiv.org/abs/1412.6572)
- PDF (library): `SPML2026-goodfellow-explaining-adversarial.pdf`
- Papers index: [[index|Papers]]
- Course: [[../index|SPML2026 — Security and Privacy in ML]]

## Linked lectures
- [[../Lectures/2026-11-01 Adversarial Examples Intro]]

## Goal
`Masters Sharif AI > Semester 01 — Autumn 2026 > SPML2026 — Security and Privacy in ML > Papers`
