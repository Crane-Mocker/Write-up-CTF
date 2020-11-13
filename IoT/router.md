# 路由器专题

**Discription**
路由器的CTF题解or复现

**目录**

<!-- vim-markdown-toc GFM -->

* [工具](#工具)
	* [firmwalker](#firmwalker)
	* [readelf](#readelf)
* [Forensics](#forensics)
	* [Router-01](#router-01)
* [](#)
* [RT-AC66U](#rt-ac66u)

<!-- vim-markdown-toc -->

## 工具

### firmwalker

找敏感信息
`./firmwalker.sh path`

### readelf

elf信息

## Forensics

### Router-01

*forensic*

Discription:
I had a router firmware upgrade.
I tried to log in as admin / admin with the default account information to set up the router, but it does not connect.
Analyze the cause and get your account information
md5(ID_PW)
https://drive.google.com/open?id=0B4SaQn817BNcc1BjRFVZV0EydUU

目标是管理员登录。

首先binwalk解包`binwalk -Me DS_CTF_FORENSIC03`
使用firmwalker找敏感信息，迅速找到cgi位置,`/squashfs-root/home/httpd/m_login.cgi`

m_login.cgi放hopper里面disassemble. 由于要登录，在hopper里面搜索字符串`"POST"`
`<form name=\"form\" method=\"POST\" action=\"m_handler.cgi\">`
POST方法登录，m_handler.cgi对登录进行验证。

m_handler.cgi放hopper里面.label里面搜索"password", "passwd",找到一个`get_id_password`的label,可能是用来通过id获取争取的password。`aPasswd`label,get请求获取id之类的。

`readelf -d m_handler.cgi`查看有哪些动态链接库，有一个`libuserland.so`比较可疑。

`squashfs-root`下`find . -name "libuserland.so"`
> ./lib/libuserland.so
`readelf -s libuserland.so`查看这个.so里面的symbol table,找到了
> 00008da0   204 FUNC    GLOBAL DEFAULT   10 get_id_password
这个.so丢进hopper,搜索label`get_id_pasword`(或者直接跳转到00008da0)看到该function的定义。

`0000bf38-4f`看到了一个配置文件。

简单解法：
firmwalker跑完了直接搜索password看到配置文件`/squashfs-root/default/etc/iconfig.cfg`，在该配置文件里面直接搜索。

## 


## RT-AC66U

对http://bobao.360.cn/learning/detail/195.html的复现。

下载固件：http://ftp.tekwind.co.jp/pub/asustw/wireless/RT-AC66U/FW_RT_AC66U_VER3004266.zip
v3.0.0.4.376.1123没找到

配置工具:Meld
