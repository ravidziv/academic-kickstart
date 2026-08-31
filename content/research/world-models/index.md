---
title: World Models and Predictive Representations
summary: Ravid Shwartz Ziv's research on world models, predictive representations, learned dynamics, and training agents in imagination.
date: "2026-08-26"
lastmod: "2026-08-26"
authors:
- admin
tags:
- World Models
- Representation Learning
- Reinforcement Learning
---

World models learn useful structure about how an environment changes. The goal is not simply to generate a realistic next frame. A useful model should support prediction, planning, and action in a representation where the important dynamics are easier to learn and reason about.

My work in this area asks three related questions:

- What should a model predict so that its representation captures the structure needed for downstream decisions?
- How should we evaluate a world model beyond visual realism or a single probing task?
- When an agent learns from imagined trajectories, how do errors in learned dynamics and rewards affect policy optimization?

## Related research

**[On Training in Imagination](/publication/training-in-imagination/)** directly studies policies trained on trajectories produced by learned dynamics and reward models. It analyzes how model error, regularity, sampling, and noisy rewards shape return estimates and optimization.

The broader program also includes joint-embedding predictive architectures. **[S-JEPA](/publication/s-jepa/)** learns predictive speech representations with soft targets, while **[HP-JEPA](/publication/hp-jepa/)** studies latent prediction over graphs at multiple resolutions. These are representation-learning systems relevant to the world-model agenda; they are not presented as complete environment simulators.

My background in information theory and computational neuroscience shapes how I approach these systems: a representation should retain the information needed for prediction and action while exposing dynamics in a form that models can use efficiently.

[See all publications](/publication/) or [share a research idea](/#contact).
