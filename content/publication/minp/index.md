---
title: "Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs"
authors:
- admin
- Minh, Nguyen Nhat
- Baker, Andrew
- Neo, Clement
- Roush, Allen
- Kirsch, Andreas
- Shwartz-Ziv, Ravid
date: "2025-01-01"
doi: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "International Conference on Learning Representations"
publication_short: "In *ICLR*"

abstract: "Large Language Models (LLMs) generate text by sampling the next token from a probability distribution over the vocabulary at each decoding step. However, popular sampling methods like top-p (nucleus sampling) often struggle to balance quality and diversity, especially at higher temperatures, leading to incoherent or repetitive outputs. To address this challenge, we propose min-p sampling, a dynamic truncation method that adjusts the sampling threshold based on the model's confidence by scaling according to the top token's probability. We conduct extensive experiments on benchmarks including GPQA, GSM8K, and AlpacaEval Creative Writing, demonstrating that min-p sampling improves both the quality and diversity of generated text, particularly at high temperatures. Moreover, human evaluations reveal a clear preference for min-p sampling in terms of both text quality and diversity. Min-p sampling has been adopted by multiple open-source LLM implementations, highlighting its practical utility and potential impact."

# Summary. An optional shortened abstract.
summary: "We introduce min-p sampling, a dynamic truncation method for language models that improves text generation quality and diversity, especially at high temperatures, showing superior performance across multiple benchmarks."

tags:
- Language Models
- Sampling Methods
- Text Generation
- Deep Learning
- Natural Language Processing

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
