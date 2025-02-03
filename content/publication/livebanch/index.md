---
title: "LiveBench: A Challenging, Contamination-Free LLM Benchmark"
authors:
- White Colin
- Dooley Samuel
- Roberts Manley
- Pal Arka
- Feuer Ben
- Jain Siddhartha
- admin
- Jain Neel
- Saifullah Khalid
- Naidu Siddartha
- Hegde Chinmay
- LeCun Yann
- Goldstein Tom
- Neiswanger Willie
- Goldblum Micah
date: "2024-06-27"
doi: ""

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "International Conference on Learning Representations"
publication_short: "In *ICLR*"

abstract: "Test set contamination, wherein test data from a benchmark ends up in a newer model's training set, is a well-documented obstacle for fair LLM evaluation and can quickly render benchmarks obsolete. To mitigate this, many recent benchmarks crowdsource new prompts and evaluations from human or LLM judges; however, these can introduce significant biases, and break down when scoring hard questions. In this work, we introduce a new benchmark for LLMs designed to be immune to both test set contamination and the pitfalls of LLM judging and human crowdsourcing. We release LiveBench, the first benchmark that (1) contains frequently-updated questions from recent information sources, (2) scores answers automatically according to objective ground-truth values, and (3) contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis. To achieve this, LiveBench contains questions that are based on recently-released math competitions, arXiv papers, news articles, and datasets, and it contains harder, contamination-free versions of tasks from previous benchmarks such as Big-Bench Hard, AMPS, and IFEval. We evaluate many prominent closed-source models, as well as dozens of open-source models ranging from 0.5B to 110B in size. LiveBench is difficult, with top models achieving below 65% accuracy. We release all questions, code, and model answers. Questions will be added and updated on a monthly basis, and we will release new tasks and harder versions of tasks over time so that LiveBench can distinguish between the capabilities of LLMs as they improve in the future. We welcome community engagement and collaboration for expanding the benchmark tasks and models."

# Summary. An optional shortened abstract.
summary: "We introduce LiveBench, a novel contamination-free LLM benchmark featuring continuously updated questions from recent sources, objective scoring, and challenging tasks across multiple domains."

tags:
- Benchmark
- Large Language Models
- Evaluation
- Machine Learning
- Natural Language Processing
- Test Set Contamination

featured: true

links:
url_pdf: https://arxiv.org/abs/2406.19314
#url_code: 
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

*[Submitted on 27 Jun 2024]*
