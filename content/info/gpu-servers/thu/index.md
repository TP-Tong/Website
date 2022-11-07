---
title: THU Servers
type: book
toc: false
date: false
---

Please contact [Yuyang Li](https://yuyangli.com) for more information. Note that you can only access them

<!-- more -->

## Preliminaries

To make sure that you're capable of using a server for computation, it's suggested that you go through [this guide](/info/gpu-servers/gpu-server-prelinilaries/) several stuffs as preliminaries.

Remember that it's common to be frustrated dealing with a command line Linux and other new tech stuffs, but you will master it after try-and-errors. Good luck!

## Login to the Servers

Of note, **using SSH keys as the login method is a must for remote login for security reasons**.

### GPU Servers in THU Central Building Room 501

**It's strongly recommended to go to Room 501 to use the machines in person, where you can access not only GUI desktops, but also guidance and help from our TAs.**

To access remotely, **please use `501.gpu.tongclass.ac.cn` with specified ports**, depending on the machine allocated to you. Please see the internally-shared Google doc or contact the TAs for information. E.g. your username is john, and you've been allocated the server `appleseed`, which in on the port `23333` according to the doc, so you login to the server with:

```shell
ssh john@501.gpu.tongclass.ac.cn -p 23333
```

### GPU Server in BIGAI Server Room

We currently have 4 GPU servers in BIGAI Server Room: `snape`, `lupin`, `sirius` and `dobby`.

#### Direct Connection in BIGAI Network

When you're connected to BIGAI's network directly or via BIGAI VPN, you can directly access them with:

```shell
ssh USERNAME@HOSTNAME.gpu.tongclass.ac.cn
```

E.g. to login to `dobby` with username `john`, use:

```shell
ssh john@dobby.gpu.tongclass.ac.cn
```
