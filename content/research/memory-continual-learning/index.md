---
title: Memory, Personalization, and Continual Learning
summary: Ravid Shwartz Ziv's research interests in AI memory, personalization, continual learning, and updating knowledge without destructive interference.
date: "2026-08-26"
lastmod: "2026-08-26"
authors:
- admin
tags:
- Memory
- Personalization
- Continual Learning
- AI Agents
---

AI systems need several kinds of memory. They must use information from the current context, retain useful knowledge over longer periods, adapt to new experience, and sometimes personalize behavior without damaging capabilities learned earlier. Treating all of these as one problem hides the tradeoffs that matter.

I am interested in four practical questions:

- How can a fixed-size state retain the right information from a long context?
- How can a model update one association without interfering with many others?
- What should be stored in weights, external memory, or an agent's working context?
- How can a system learn continually while measuring what it preserves and what it forgets?

## Memory under a fixed budget

My essay **[Editing a Compressed Memory](https://www.the-information-bottleneck.com/p/editing-a-compressed-memory)** explains one concrete version of the problem. Linear attention replaces a growing key-value cache with a fixed-size recurrent state. This makes memory and decoding costs independent of context length, but introduces interference when many associations share the same representation. Delta-style updates, decay, and gating provide progressively more selective ways to edit that state.

This form of in-context memory is different from personalization across sessions or continual learning in model weights. The common question is what information a bounded system should preserve, how it should update that information, and how we can evaluate the resulting behavior.

For agents, memory must also interact with planning and verification. **[Minitap](/publication/minitap/)** studies a mobile-agent system that separates these responsibilities across specialized components, making failures easier to detect and recover from.

[Read my writing and podcast conversations](/#podcast) or [discuss a collaboration](/#contact).
