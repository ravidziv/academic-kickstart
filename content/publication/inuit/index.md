---
title: "Inheritune: Training Smaller Yet More Attentive Language Models"
authors:
- Sanyal Sunny
- admin
- Dimakis Alexandros G.
- Sanghavi Sujay
date: "2024-04-17"
doi: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["3"]

# Publication name and optional abbreviated publication name.
publication: "arXiv"
publication_short: "arXiv"

abstract: "Large Language Models (LLMs) have achieved remarkable performance across various natural language processing tasks, primarily due to the transformer architecture and its self-attention mechanism. However, we observe that in standard decoder-style LLMs, attention matrices degenerate to single-column for deeper layers. Layers in this state are unable to learn anything meaningful and mostly redundant; we refer to these as lazy layers. The goal of this paper is to train smaller models by eliminating this structural inefficiency without compromising performance. Motivated by this observation, we propose Inheritune, a simple yet effective training recipe for developing smaller, high-performing language models. Smaller models trained with Inheritune, inherit early transformer layers from a larger pre-trained model, then retrain and progressively expand until they match or exceed the performance of the larger model. We demonstrate that Inheritune enables the training of various sizes of GPT-2 models on datasets like OpenWebText-9B and FineWeb_edu. Models trained with Inheritune, despite having significantly fewer layers, match or even surpass the performance of their larger counterparts. For instance, our 16-layer GPT-2 medium variant achieves comparable performance to the standard 24-layer GPT-2 medium model."

# Summary. An optional shortened abstract.
summary: "We present Inheritune, a training method that creates smaller yet equally effective language models by inheriting and fine-tuning early transformer layers from larger models, addressing the issue of lazy layers in deep networks."

tags:
- Language Models
- Model Compression
- Transfer Learning
- Neural Networks
- Attention Mechanism
- Efficient Training

featured: true

links:
url_pdf: https://arxiv.org/abs/2404.08634
url_code: https://github.com/example/inheritune  # Note: Placeholder URL
#url_dataset: 
#url_poster: '#'
#url_project: ''
#url_slides: ''
#url_source: '#'
#url_video: '#'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: ''
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
projects:
- internal-project

# Slides (optional).
slides: example
---

*[Submitted on 17 Apr 2024]*
