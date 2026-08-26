---
title: Soft Clustering Anchors for Self-Supervised Speech Representation Learning in Joint Embedding
  Prediction Architectures
authors:
- Georgios Ioannides
- Adrian Kieback
- Judah Goldfeder
- Linsey Pang
- Aman Chadha
- Aaron Elkins
- Yann LeCun
- admin
date: '2026-01-30T20:51:37Z'
lastmod: '2026-08-26'
publication_types:
- '3'
publication: arXiv preprint
publication_short: arXiv, 2026
abstract: GMM-Anchored JEPA fits soft clusters to acoustic features and uses them as auxiliary
  targets during self-supervised speech training. A changing supervision weight balances this
  grounding signal with latent prediction, avoiding iterative offline reclustering.
summary: An earlier speech JEPA study using fixed soft clustering targets to stabilize representation
  learning.
tags:
- JEPA
- Speech
- Representation Learning
featured: false
url_pdf: https://arxiv.org/pdf/2602.09040
url_code: https://github.com/gioannides/clustering-anchored-jepa
links:
- name: arXiv
  url: https://arxiv.org/abs/2602.09040
---

Related work: [S-JEPA]({{< ref "/publication/s-jepa/index.md" >}}) is the later speech study with a continuous two-phase training procedure and online clustering targets.
