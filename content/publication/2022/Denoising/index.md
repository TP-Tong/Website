---
title: 'Denoising Masked Autoencoders are Certifiable Robust Vision Learners'
authors:
  - QuanLin Wu
  - Hang Ye
  - Yuntian Gu
  - Huishuai Zhang
  - Liwei Wang
  - Di He
  
date: '2022-10-28T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2023-02-02T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: 'International Conference on Learning Representations'
publication_short: 'ICLR 2023'

abstract: In this paper, we propose a new self-supervised method, which is called denoising masked autoencoders (DMAE), for learning certified robust classifiers of images. In DMAE, we corrupt each image by adding Gaussian noises to each pixel value and randomly masking several patches. A Transformer-based encoder-decoder model is then trained to reconstruct the original image from the corrupted one. In this learning paradigm, the encoder will learn to capture relevant semantics for the downstream tasks, which is also robust to Gaussian additive noises. We show that the pre-trained encoder can naturally be used as the base classifier in Gaussian smoothed models, where we can analytically compute the certified radius for any data point. Although the proposed method is simple, it yields significant performance improvement in downstream classification tasks. We show that the DMAE ViT-Base model, which just uses 1/10 parameters of the model developed in recent work (Carlini et al., 2022), achieves competitive or better certified accuracy in various settings. The DMAE ViT-Large model significantly surpasses all previous results, establishing a new state-of-the-art on ImageNet dataset. We further demonstrate that the pre-trained model has good transferability to the CIFAR-10 dataset, suggesting its wide adaptability. All model checkpoints and code will be released soon.

# Summary. An optional shortened abstract.
# summary: We propose GenDexGrasp, a versatile dexterous grasping method that can generalize to out-of-domain robotic hands. In addition, we contribute MultiDex, a large-scale synthetic dexterous grasping dataset.

tags:
  - Source Themes
featured: false
# 这个地方还没改完
links:
  - name: Arxiv
    url: https://arxiv.org/abs/2210.00722
url_pdf: https://arxiv.org/pdf/2210.00722.pdf
url_code: https://github.com/tengyu-liu/GenDexGrasp
url_dataset: https://sites.google.com/view/gendexgrasp/multidex
url_poster: ''
url_project: https://sites.google.com/view/gendexgrasp
url_slides: ''
url_source: ''
url_video: https://vimeo.com/753797406/1ef3563db3

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# image:
#   caption: 'Teaser for GenDexGrasp'
#   focal_point: ''
#   preview_only: false

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
slides:
---
