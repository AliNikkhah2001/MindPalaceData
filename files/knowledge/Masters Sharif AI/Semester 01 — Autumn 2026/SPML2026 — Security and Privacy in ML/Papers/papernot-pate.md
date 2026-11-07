---
title: Semi-supervised Knowledge Transfer (PATE)
summary: Ensemble of teachers on disjoint private data; noisy vote trains a public student.
course: SPML2026 — Security and Privacy in ML
tags: [masters, spml, paper, study]
arxiv: "1610.05755"
read: false
---

# Semi-supervised Knowledge Transfer (PATE)

> Ensemble of teachers on disjoint private data; noisy vote trains a public student.

## Why this paper (for SPML)
Alternative to DP-SGD when you can host teacher ensembles.

## Core ideas
- Teachers never expose raw data.
- Laplacian/Gaussian noise on votes.
- Student learns on public unlabeled data + noisy labels.

## How to study it
PATE pipeline diagram; compare privacy cost to DP-SGD.

## Links
- arXiv: [1610.05755](https://arxiv.org/abs/1610.05755)
- PDF (library): `SPML2026-papernot-pate.pdf`
- Papers index: [[index|Papers]]
- Course: [[../index|SPML2026 — Security and Privacy in ML]]

## Linked lectures
- [[../Lectures/2026-12-13 Private Deep Learning DP-SGD & PATE]]

## Goal
`Masters Sharif AI > Semester 01 — Autumn 2026 > SPML2026 — Security and Privacy in ML > Papers`
