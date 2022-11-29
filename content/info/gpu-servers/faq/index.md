---
title: FAQ
type: book
toc: true
date: false
weight: 40
---

This page provides FAQs for our computing servers.

## Conda and PyPI

Conda and PyPI are used to manage your Python development environment and packages.

### Installation

You can find installation package for Anaconda at `/home/shared/utils/conda`, so you don't need to download them again.

### Switching Mirrors

For faster access, you can switch to other mirrors. Please refer to:

- [TUNA Conda Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)
- [TUNA PyPI Mirror](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)
- Other Conda and PyPI mirrors

## CUDA

We provide the latest NVIDIA GPU drivers and CUDA Toolkit in various versions.

- In most cases, CUDA 11.x are compatible
- GPUs like 3090 with Ampere architecture only supports `CUDA>=11.1`
- To check compatibility, please check [this page](https://docs..vidia.com/deploy/cuda-compatibility/index.html).

### CUDA Toolkit

In order to provide CUDA with various versions, we do not create symbolic link in `/usr/local/cuda/`. Instead, they are in `/usr/local/cuda-xy.z` with `xy.z` being the version. To use them, you may need to specify environment variables like `CUDA_PATH` (depends on your program). You can use `export` to set them. For convenience, you can export them in your shell profile.

For example, to use CUDA 11.7 by default in `bash`, you should add the following script to your `~/.bashrc`:

```shell
export PATH="/usr/local/cuda-11.7/bin/:$PATH"
export LD_LIBRARY_PATH="/usr/local/cuda-11.7/lib64:$LD_LIBRARY_PATH"
export CUDA_HOME="/usr/local/cuda-11.7"
export CUDA_PATH="/usr/local/cuda-11.7"
export CPATH="/usr/local/cuda-11.7/include:$CPATH"
```

We only install some important versions but not all of them. To use a certain unprovided versions, please use Docker. You can find and pull images from here.