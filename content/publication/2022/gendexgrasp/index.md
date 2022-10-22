---
title: 'GenDexGrasp'
authors:
  - Puhao Li
  - Tengyu Liu
  - Yuyang Li
  - Yiran Geng
  - Yixin Zhu
  - Yaodong Yang
  - Siyuan Huang
date: '2022-10-10T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2022-10-10T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1', '3']

# Publication name and optional abbreviated publication name.
publication: ''
publication_short: ''

abstract: Generating dexterous grasping has been a long-standing and challenging robotic task. Despite recent progress, existing methods primarily suffer from two issues. First, most prior arts focus on a specific type of robot hand, lacking generalizable capability of handling unseen ones. Second, prior arts oftentimes fail to rapidly generate diverse grasps with a high success rate. To jointly tackle these challenges with a unified solution, we propose GenDexGrasp, a novel hand-agnostic grasping algorithm for generalizable grasping. GenDexGrasp is trained on our proposed large-scale multi-hand grasping dataset MultiDex synthesized with force closure optimization. By leveraging the contact map as a hand-agnostic intermediate representation, GenDexGrasp efficiently generates diverse and plausible grasping poses with a high success rate and can transfer among diverse multi-fingered robotic hands. Compared with previous methods, GenDexGrasp achieves a three-way trade-off among success rate, inference speed, and diversity.

# Summary. An optional shortened abstract.
summary: We propose GenDexGrasp, a versatile dexterous grasping method that can generalize to out-of-domain robotic hands. In addition, we contribute MultiDex, a large-scale synthetic dexterous grasping dataset.

tags:
  - Source Themes
featured: false

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
image:
  caption: 'Teaser for GenDexGrasp'
  focal_point: ''
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
slides:
---

Supplementary notes can be added here, including [code and math](https://wowchemy.com/docs/content/writing-markdown-latex/).
