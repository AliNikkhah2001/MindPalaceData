---
title: Practical Black-Box Attacks against Machine Learning
summary: Attack a substitute model, transfer AEs to the black-box victim—no gradients needed on the target.
course: SPML2026 — Security and Privacy in ML
tags: [masters, spml, paper, study]
arxiv: "1602.02697"
read: false
---

# Practical Black-Box Attacks against Machine Learning

> Attack a substitute model, transfer AEs to the black-box victim—no gradients needed on the target.

## Why this paper (for SPML)
Introduces transferability as a practical black-box strategy.

## Core ideas
- Query victim for labels → train substitute.
- Craft AEs on substitute; transfer to victim.
- Works across architectures when decision boundaries align.

## How to study it
Substitute-training loop + transfer rates.

## Links
- arXiv: [1602.02697](https://arxiv.org/abs/1602.02697)
- PDF (library): `SPML2026-papernot-practical-blackbox.pdf`
- Papers index: [[index|Papers]]
- Course: [[../index|SPML2026 — Security and Privacy in ML]]

## Linked lectures
- [[../Lectures/2026-11-10 Black-Box Adversarial Attacks]]

## Goal
`Masters Sharif AI > Semester 01 — Autumn 2026 > SPML2026 — Security and Privacy in ML > Papers`
