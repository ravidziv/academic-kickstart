---
title: "Sequence Modeling Using a Memory Controller Extension for LSTM"
authors:
- admin
-  Ben-Ari Itamar
date: "2017-12-01"
author_notes:
- "Equal contribution"
- "Equal contribution"
doi: ""

# Schedule page publish date (NOT publication's date).
# publishDate: "2017-05-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: NIPS 2017 Time Series Workshop
publication_short: NIPS 2017 Time Series Workshop
abstract: "The Long Short-term Memory (LSTM) recurrent neural network is a powerful model for time series forecasting and various temporal tasks. In this work we extend the standard LSTM architecture by augmenting it with an additional gate which produces a memory control vector signal inspired by the Differentiable Neural Computer (DNC) model. This vector is fed back to the LSTM instead of the original output prediction. By decoupling the LSTM prediction from its role as a memory controller we allow each output to specialize in its own task. The result is that our LSTM prediction is dependent on its memory state and not the other way around (as in standard LSTM). We demonstrate our architecture on two time-series forecast tasks and show that our model achieves up to 8% lower loss than the standard LSTM model."
# Summarye. An optional shortened abstract.
summary: "We extend the standard LSTM architecture by augmenting it with an additional gate which produces a memory control vector signal. This vector is fed back to the LSTM instead of the original output prediction. By decoupling the LSTM prediction from its role as a memory controller we allow each output to specialize in its own task."
 
tags:
- Source Themes
featured: true

links:
#- name: Custom Link
url_pdf: https://www.intel.com/content/dam/www/public/us/en/ai/documents/Sequence-Modeling-NIPS-2017.pdf
# url_code: 

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
- internal-project

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
