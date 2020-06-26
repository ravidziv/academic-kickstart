\cventry{2017}{"Open the Black Box of Deep Neural Networks"}{Future Leaders of AI Retreat (FLAIR)}{New York University Shanghai}{Shanghai, China}{}{}
---
title: Open the Black Box of Deep Neural Networks
event: Future Leaders of AI Retreat (FLAIR)
event_url: https://ai-flair.org/

location: New York University Shanghai
address:
  city: Shanghai
  country: China
  
summary: Understaing Deep Neural Networks with the information bottleneck principle between the layers.
abstract: "Despite numerous breakthroughs, Deep Neural Networks (DNNS) are often treated as black boxes owing to our poor understanding of their internal organization and optimization process. 
We address this limitation by suggesting that DNNS learn to optimize the mutual information that each layer preserves on the input and output variables, resulting from tradeoff in compression and prediction per each layer. In this talk, we will present  analytical and numerical study of DNNS in the Information Plane,  and how the Stochastic Gradient Decent (SGD) algorithm follows the information bottleneck trade-off principle. We show how SGD achieves this optimal bound, as the compression for each layer amounts to relaxation to a maximum conditional entropy state subject to the proper constraints on the error and information of the labels. Thus, our works suggests that DNNs are essentially a technique for solving the information bottleneck problem for large scale learning tasks."


# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "2017-12-28T13:00:00Z"
#date_end: "2030-06-01T15:00:00Z"
all_day: false

# Schedule page publish date (NOT talk date).
#publishDate: "2017-01-01T00:00:00Z"

authors: []
tags: []

# Is this a featured talk? (true/false)
featured: true

image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
  focal_point: Right

links:
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: example

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
- internal-project

# Enable math on this page?
math: true
---