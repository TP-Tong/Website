---
title: 'Faster VoxelPose: Real-time 3D Human Pose Estimation by Orthographic Projection'
authors:
  - Hang Ye
  - Wentao Zhu
  - Chunyu Wang
  - Rujie Wu
  - Yizhou Wang
date: '2022-07-22T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2023-01-16T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: 'International Conference on Robotics and Automation 2023'
publication_short: 'ICRA 2023'

abstract: While the voxel-based methods have achieved promising results for multi-person 3D pose estimation from multi-cameras, they suffer from heavy computation burdens, especially for large scenes. We present Faster VoxelPose to address the challenge by re-projecting the feature volume to the three two-dimensional coordinate planes and estimating X, Y, Z coordinates from them separately. To that end, we first localize each person by a 3D bounding box by estimating a 2D box and its height based on the volume features projected to the xy-plane and z-axis, respectively. Then for each person, we estimate partial joint coordinates from the three coordinate planes separately which are then fused to obtain the final 3D pose. The method is free from costly 3D-CNNs and improves the speed of VoxelPose by ten times and meanwhile achieves competitive accuracy as the state-of-the-art methods, proving its potential in real-time applications.

# Summary. An optional shortened abstract.
# summary: We propose GenDexGrasp, a versatile dexterous grasping method that can generalize to out-of-domain robotic hands. In addition, we contribute MultiDex, a large-scale synthetic dexterous grasping dataset.

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
