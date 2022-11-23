---
title: THU Servers
type: book
toc: true
date: false
---

To make sure that you're capable of using a server for computation, it's suggested that you go through [this guide](/info/gpu-servers/gpu-server-prelinilaries/) several stuffs as preliminaries. For more information, please contact [Yuyang Li](https://yuyangli.com).

## Server Status

> 🟢: Up; 🟡: Under maintain; 🔴: Down; ⚫: Unavailable.

- `Talented Terms` (THU Central Building 501)
    - 🟢 `adequate accuracy`
    - 🟢 `bold bayesian`
    - 🟢 `civil clustering`
    - 🟢 `dynamic descrptive`
    - 🟢 `exotic epoch` (Display unavailbale)
    - 🟢 `factual feature`
    - 🟢 `grown genetic`
    - 🟢 `honest heuristics`
    - 🟢 `ideal inductive`
    - 🟢 `just jacobian`
- `Healthy Harry` (BIGAI Server Room)
    - 🔴 `smart snape` (Maintaining currently blocked by COVID-19)
    - 🟡 `lucky lupin` (Incompatible CUDA and kernel)
    - 🟢 `serious sirius`
    - 🟢 `daring dobby`
- `Polished Peanuts` (Thirdparty-maintained)
    - 🟢 `certain charlie` (Will be open soon)
    - ⚫ `sweet snoopy`
    - ⚫ `legal linus`
    - ⚫ `lasting lucy`
    - ⚫ `rare rerun`
- `Free Fish`: Free GPU Resources, please refer to [this page](/info/gpu-servers/free-gpu/).


## Apply for an account

1. Fill out the [application form](https://go.tongclass.ac.cn/gpu/thu/apply).
2. Contact Liangru Xiang or Yuyang Li for account allocation information.

## Login to the Servers

Of note, **using SSH keys as the login method is a must for remote login for security reasons**.

### GPU Servers in THU Central Building Room 501

**It's strongly recommended to go to Room 501 to use the machines in person, where you can access not only GUI desktops, but also guidance and help from our TAs.**

To access remotely, **please use `terms.gpu.tongclass.ac.cn` or `501.gpu.tongclass.ac.cn` with specified ports**, depending on the machine allocated to you. Please see the internally-shared Google doc or contact the TAs for information. E.g. your username is john, and you've been allocated the server `appleseed`, which in on the port `23333` according to the doc, so you login to the server with:

```shell
ssh john@501.gpu.tongclass.ac.cn -p 23333
```

### GPU Server in BIGAI Server Room

We currently have 4 GPU servers in BIGAI Server Room: `snape`, `lupin`, `sirius` and `dobby`.

#### Direct Connection in BIGAI Network

When you're connected to BIGAI's student network (BIGAI-Student) directly, to the BIGAI VPN, you can directly access them with:

```shell
ssh USERNAME@HOSTNAME.gpu.tongclass.ac.cn
```
