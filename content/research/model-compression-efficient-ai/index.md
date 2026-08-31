---
title: Model Compression and Efficient AI
summary: Ravid Shwartz Ziv's research on model compression, task-aware quantization, efficient representations, and reducing AI memory and computation.
date: "2026-08-26"
lastmod: "2026-08-26"
authors:
- admin
tags:
- Model Compression
- Efficient AI
- Quantization
- Information Theory
---

Efficient AI is not one technique. A system can reduce the precision of its weights, reuse or remove redundant layers, change the structure of a linear transformation, or select a better internal representation for a downstream task. Each choice saves a different resource and risks losing a different capability.

My work connects three levels of compression:

## Models and weights

**[You Had One Job](/publication/task-aware-quantization/)** treats mixed-precision quantization as a task-conditioned allocation problem. It uses hidden representations and output sensitivity to identify which transformer layers deserve more precision under a fixed bit budget.

**[When Attention Collapses / Inheritune](/publication/inuit/)** studies redundant transformer layers and how useful layers can be reused to construct smaller language models. **[NdLinear](/publication/ndlinear/)** replaces a flattened linear map with transformations along the dimensions of a tensor, reducing parameters when the structure of the task supports that factorization.

## Representations

**[Layer by Layer](/publication/layer-by-layer/)** shows that intermediate representations can outperform final-layer embeddings. **[Attention Sinks and Compression Valleys](/publication/attention-sinks-compression-valleys/)** connects large residual-stream activations, attention sinks, and representational compression across model depth.

Representational compression is not automatically a smaller model. It explains which information is retained and where a model's computation becomes concentrated. That understanding can guide practical choices about layers, embeddings, and downstream systems.

## Inference

Efficient inference also depends on how a model generates. **[Min-p](/publication/minp/)** adapts a sampling cutoff to the model's confidence. My essay **[Speculative decoding, from zero to DSpark](https://www.the-information-bottleneck.com/p/speculative-decoding-from-zero-to)** explains how drafting, verification, and scheduling turn otherwise idle computation into higher serving throughput.

[Explore selected systems](/#work) or [see all publications](/publication/).
