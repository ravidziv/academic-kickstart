
---
title: Compression in deep learning-  an information theory perspective
event: NYU CDS Seminar
event_url: 

location: NYU Center for Data Science
address:
  city:  New York, NY
  country: USA
  
summary: "While DNNs have achieved many breakthroughs, our understanding of their internal structure, optimization process, and generalization is poor, and we often treat them as black boxes. We attempt to resolve these issues by suggesting that DNNs learn to optimize the Information Bottleneck (IB) principle - the tradeoff between information compression and prediction quality. In the first part of the talk, I presented this approach, showing an analytical and numerical study of DNNs in the information plane. This analysis reveals how the training process compresses the input to an optimal, efficient representation.  I discussed recent works inspired by this analysis and show how we can apply them to real-world problems. In the second part of the talk, I will discuss information in infinitely-wide neural networks using recent results in Neural Tangent Kernels (NTK) networks. The NTK allows us to derive many tractable information-theoretic quantities. By utilizing these derivations, we can do an empirical search to find the important information-theoretic quantities that affect generalization in DNNs.  I aslo presented the Dual Information Bottleneck (dualIB) framework, to find an optimal representation that resolves some of the drawbacks of the original IB. A theoretical analysis of the dualIB shows the structure of its solution and its ability to preserve the original distribution's statistics. Within this, we focused on the variational form of the dualIB, allowing its application to DNNs."

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "2021-09-22"
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
- icon: twitter
  icon_pack: ai
  name: Slides
  url: files/nyu_talk.pdf
url_code: ""
url_pdf: ""
url_slides: files/nyu_talk.pdf
url_video: ""


# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: https://pan.baidu.com/s/1i5mxtNB

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
