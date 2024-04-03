# Tong Class Website Ops Guide

> By [Yuyang Li](https://yuyangli.com/). Last update on Mar 3, 2024.

## Basic Information

The source code of the website is hosted on GitHub Repo: [TP-Tong/Website](https://github.com/TP-Tong/Website). It is published on the Internet via Cloudflare Pages (in Yuyang's account), and can be accessed via [tongclass.ac.cn](https://tongclass.ac.cn). It uses the [Hugo](https://gohugo.io/), with templates from [HugoBlox](https://hugoblox.com/) (previously WowChemy) a framework for building static websites.

## Ops Guide

### Install Hugo

Please refer to [official docs](https://gohugo.io/installation/).

### Local Server

Use `hugo server` to start a local server.

### Compile

Use `hugo` to compile static files into `public`

### Publish

Due to the lack of support of hugo-extended by Cloudflare, we currently need to build the website to generate static files under `public/` before pushing the contents. Commits to the `main` branch will automatically trigger the website update.

Please refer to [official docs](https://gohugo.io/getting-started/usage/) for more usage.

### Dev Branch

If you push the contents to any non-`main` branch, you can access the website via `https://[BRANCH_NAME].tongclass.ac.cn` (as long as the branch name is not occupied by other DNS items), like `https://dev.tongclass.ac.cn` if you push to `dev`.
