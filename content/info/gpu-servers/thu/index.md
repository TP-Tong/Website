---
title: THU Servers
type: book
toc: true
date: false
---

Please contact [Yuyang Li](https://yuyangli.com) for more information. 
<!-- more -->

## Server Status

<!-- Use 🟢(up), 🟡 (under maintain), 🔴(down), ⚫ (unavailable) -->

- `Talented Terms` (THU Central Building 501): `terms.gpu.tongclass.ac.cn`
    - 🟢 `adequate accuracy` - UP
    - 🟢 `bold bayesian` - UP
    - 🟢 `civil clustering` - UP
    - 🟢 `dynamic descrptive` - UP
    - 🟢 `exotic epoch` - UP
    - 🟢 `factual feature` - UP
    - 🟢 `grown genetic` - UP
    - 🟢 `honest heuristics` - UP
    - 🟢 `ideal inductive` - UP
    - 🟢 `just jacobian` - UP
- `Healthy Harry` (BIGAI Server Room): `[HOSTNAME].gpu.tongclass.ac.cn`
    - 🔴 `smart snape` - DOWN
    - 🟢 `stable lupin` - UP
    - 🔴 `serious sirius` - DOWN
    - 🟢 `daring dobby` - UP
- `Polished Peanuts` (Thirdparty-maintained): `[HOSTNAME].gpu.tongclass.ac.cn`
    - ⚫ `stirred schultz` - UNAVAILABLE, pending...
    - ⚫ `certain charlie` - UNAVAILABLE, pending...
    - ⚫ `sweet snoopy` - UNAVAILABLE, pending...
    - ⚫ `legal linus` - UNAVAILABLE, pending...
    - ⚫ `lasting lucy` - UNAVAILABLE, pending...
    - ⚫ `rare rerun` - UNAVAILABLE, pending...
- `Free Fish`: Free GPU Resources, please refer to [this page](/info/gpu-servers/free-gpu/).


## Preliminaries

To make sure that you're capable of using a server for computation, it's suggested that you go through [this guide](/info/gpu-servers/gpu-server-prelinilaries/) several stuffs as preliminaries.

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
