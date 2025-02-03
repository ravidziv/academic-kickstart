---
title: "Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning"
authors:
- admin
- Arefin, Md Rifat
- Subbaraj, Gopeshh
- Gontier, Nicolas
- LeCun, Yann
- Rish, Irina
- Shwartz-Ziv, Ravid
- Pal, Christopher
date: "2024-11-04"
doi: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "International Conference on Learning Representations"
publication_short: "In *ICLR*"

abstract: "Decoder-only Transformers often struggle with complex reasoning tasks, particularly arithmetic reasoning requiring multiple sequential operations. In this work, we identify representation collapse in the model's intermediate layers as a key factor limiting their reasoning capabilities. To address this, we propose Sequential Variance-Covariance Regularization (Seq-VCR), which enhances the entropy of intermediate representations and prevents collapse. Combined with dummy pause tokens as substitutes for chain-of-thought (CoT) tokens, our method significantly improves performance in arithmetic reasoning problems. In the challenging 5×5 integer multiplication task, our approach achieves 99.5% exact match accuracy, outperforming models of the same size (which yield 0% accuracy) and GPT-4 with five-shot CoT prompting (44%). We also demonstrate superior results on arithmetic expression and longest increasing subsequence (LIS) datasets. Our findings highlight the importance of preventing intermediate layer representation collapse to enhance the reasoning capabilities of Transformers and show that Seq-VCR offers an effective solution without requiring explicit CoT supervision."

# Summary. An optional shortened abstract.
summary: "We propose Seq-VCR, a method to prevent representation collapse in Transformer models, significantly improving their performance on complex reasoning tasks without requiring chain-of-thought supervision."

tags:
- Transformers
- Representation Learning
- Deep Learning
- Reasoning
- Neural Networks

featured: true

links:
url_pdf: 
#url_code: 
#url_dataset: '#'
#url_poster: '#'
#url_project: ''
#url_slides: ''
#url_source: '#'
#url_video: '#'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
projects:
- internal-project

# Slides (optional).
slides: example
---
