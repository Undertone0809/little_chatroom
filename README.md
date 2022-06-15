# 1.简介

用pyqt + socket实现一个简单的聊天室

主要功能：
- 简易聊天室
- 打开服务端和客户端可以发送聊天信息


> 本项目在pyqt的框架上进一步封装，基于springMVC架构进行封装，参考笔者之前写的：[【快速调用】基于mvc架构的pyqt架构封装](https://blog.csdn.net/linZinan_/article/details/112460133)




# 2.运行环境

- python3.7.6
- 使用pip安装下面的环境

```shell
pip install PyQt5
```

1.运行ClientApplication启动服务端

2.运行ServerApplication启动客户端

> 注意：要先启动服务端再启动客户端


- 目录结构

```shell
│  ClientApplication.py 客户端程序
│  ServerApplication.py 服务端程序
│  README.md
│
├─controller # 页面控制器
│  │  HomeController.py 继承home.py中的UI样式
│  │  __init__.py
│
│
├─service # 服务，包括服务端服务和客户端服务
│  │  socket_client.py  客户端封装
│  │  socket_server.py 服务端封装
│  │  __init__.py
│
├─static	# 静态文件
│  │  __init__.py
│  │
│  └─images
│          bg1.jpg
│          headPh.png
│
└─views
    │  home.py ui文件生成的代码
    │  home.ui
    │  __init__.py
```



# 3.参考资料

- [Python线程池及其原理和使用（超级详细）](https://blog.csdn.net/weixin_33953249/article/details/93740825?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165458898016781683918204%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=165458898016781683918204&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-3-93740825-null-null.142^v11^control,157^v13^new_3&utm_term=python+%E7%BA%BF%E7%A8%8B%E6%B1%A0&spm=1018.2226.3001.4187)

- [python socket编程详细介绍](https://blog.csdn.net/rebelqsp/article/details/22109925?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522165462527816782391857934%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=165462527816782391857934&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~hot_rank-2-22109925-null-null.142^v11^control,157^v13^new_3&utm_term=python+socket&spm=1018.2226.3001.4187)

- [python3 字符串str和bytes的相互转换](https://blog.csdn.net/kids_budong_c/article/details/123672994?ops_request_misc=&request_id=&biz_id=102&utm_term=python%20str%E8%BD%ACbytes&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-123672994.142^v11^control,157^v13^new_3&spm=1018.2226.3001.4187)

- [【快速调用】基于mvc架构的pyqt架构封装](https://blog.csdn.net/linZinan_/article/details/112460133)