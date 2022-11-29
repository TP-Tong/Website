---
title: Preliminaries
type: book
toc: true
date: false
weight: 10
---

We provides resources to learn preliminaries for using computing servers. Remember that it's common to be frustrated dealing with a command line Linux and other new tech stuffs, but you will master it after try-and-errors with repeated practice. Good luck!

<!-- more -->

## Linux

Instead of fully learning Linux, you can just go through:

- [An Intro to Linux](https://www.runoob.com/linux/linux-intro.html)
- [Linux System Contents](https://www.runoob.com/linux/linux-system-contents.html)
- [Remote Login (with PuTTY)](https://www.runoob.com/linux/linux-remote-login.html)
  - Note that you can also login with `ssh` command or other softwares like Termius and VSCode
- [File Attributes and Permissions](https://www.runoob.com/linux/linux-file-attr-permission.html)
- [Vi/Vim](https://www.runoob.com/linux/linux-vim.html)


## Conda

You should work in virtual environments to isolate packages among your projects to avoid bad dependencies. You can go through:

- [An Intro to Anaconda](https://zhuanlan.zhihu.com/p/351348108)

## Docker

For environments that requires system-level dependencies, please use Docker. [This tutorial](https://docker-curriculum.com) provides detail information that helps you understand and use docker.

> Note that in our current setting, you can manage all the docker containers (including others) on the machine. Please DO NOT use or delete containers that you do not own.

## SSH

You need SSH to login to the server:

```shell
ssh USERNAME@URL -p PORT
```

Note that you should change the `USERNAME` and `PORT` to your account name and the server port. E.g. To login to the server at `server.net` on the port `23333` with account `alice`, use:

```shell
ssh alice@server.net -p 23333
```

with `PORT` unspecified, the SSH default port `22` is used.

For more information, You can go through [this SSH guide](https://wangdoc.com/ssh/).
