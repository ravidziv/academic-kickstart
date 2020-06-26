---
title: "Automated Testing of Graphics Units by Deep-Learning Detection of Visual Anomalies"
authors:
- Faivishevsky Lev
- Muppalla Ashwin
- admin
- Laperdon Ronen
- Melloul Benjamin
- Hollander Tahi
- Amitai Armon

date: "2018-1-01T00:00:00Z"
doi: ""

# Schedule page publish date (NOT publication's date).
#publishDate: "2017-01-01T00:00:00Z"

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "NIPS 2018 Machine Learning for Systems Workshop"
#publication_short: ""

abstract: We present a deep-learning based system we developed, which performs real-time detection of diverse visual corruptions in videos. It is applied to validating the
quality of graphics units in our company. The system is used for several types of content, including movies and 3D graphics. A reference video is not available
during this stage of tests, due to the randomness in movie ads, game actions, website
updates etc. Developing this system involved challenging data-science aspects to
enable detection of small distortions with low false alert rates. We describe the full
detection system, including the hardware and software aspects, and focus on the
modeling approaches used. 

# Summary. An optional shortened abstract.
summary: We propose a semi supervised model for detecting anomalies in videos inspiredby the Video Pixel Network [van den Oord et al., 2016]. Our model extends the Convolutional LSTM video encoder part of the VPN with a novel convolutional based attention mechanism. We also modify the Pixel CNN decoder part of the VPN to a frame inpainting task where a partially masked version of the frame to predict is given as input. Our model is shown to be effective in detecting anomalies in videos. This approachcould be a component in applications requiring visual common sense.

tags:
- Source Themes
featured: false

# links:
# - name: ""
#   url: ""
url_pdf: http://mlforsystems.org/assets/papers/neurips2018/automated_faivishevsky_2018.pdf
#url_code: ''
#url_dataset: ''
#url_poster: ''
#url_project: ''
#url_slides: ''
#url_source: ''
#url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/jdD8gXaTZsc)'
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: example
---
