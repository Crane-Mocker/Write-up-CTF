# 流量分析

[TOC]

## Q0

*medium*

追踪tcp流，在流6,看到`flag.txt`，

```
Rar!....3...
.............TU..<..... .+......flag.txt0.....n.Kr..z....uEo.Bn&=i.S..>....4.B..~...xj.".
...u......3.....jWj..%m..!.+h...+s..q#.]...3Ks.y.....r.2...wVQ....
```

` ccaatt  22 19aaFYsQQKr+hVX6hl2smAUQ5a767TsULEUebWSajEo=`以及下面这段

```python
# coding:utf-8
__author__ = 'YFP'
from Crypto import Random
from Crypto.Cipher import AES
import sys
import base64
IV = 'QWERTYUIOPASDFGH'
def decrypt(encrypted):
  aes = AES.new(IV, AES.MODE_CBC, IV)
  return aes.decrypt(encrypted)

def encrypt(message):
  length = 16
  count = len(message)
  padding = length - (count % length)
  message = message + '\0' * padding
  aes = AES.new(IV, AES.MODE_CBC, IV)
  return aes.encrypt(message)

str = 'this is a test'
example = encrypt(str)
print(decrypt(example))
```
先分析出现的flag.txt
很明显的rar压缩，这一堆看似乱码的东西实际上就是原始数据,所以接下来准备还原这个包。
先把原始数据直接`save as`保存在一个file里，然后随便找一个hex editor打开它。,注意，这里数据的格式是**raw**而不是**ascii**.
`52 61 72 21`是rar的文件头.(其实也可以和ascii对着看啦)
用hex editor将它掐头去尾然后保存。尾部删除到boundary分隔符处。

再分析代码
aes加密，cbc模式，偏移量IV为`IV = 'QWERTYUIOPASDFGH'`，密钥也是它（由`aes = AES.new(IV, AES.MODE_CBC, IV)`看出）
密文为`19aaFYsQQKr+hVX6hl2smAUQ5a767TsULEUebWSajEo=`
解密得`passwd={No_One_Can_Decrypt_Me}`
（至于字符集和填充就试吧，字符集是gb2312,填充是ZeroPadding）

于是拿这个password去解压缩




## Q1

*easy*

打开包，看到

```
10	0.435958	192.168.1.87	123.58.178.59	SMTP	76	C: User: dGVzdEA1MWVsYWIuY29t

12	0.485855	192.168.1.87	123.58.178.59	SMTP	80	C: Pass: RkxBRzpJU0NDVEVTVHBhcw==
```

目测是base64
解密得到

```
User: test@51elab.com
Pass: FLAG:ISCCTESTpas
```

## Q2

*easy*

追踪TCP流，可以发现`Password`，在流1中，可以发现
` moctf{c@N_y0U_4lnd_m8}`

> 包与流
> 在一个 stream 中，按照某种协议或者规定，把 stream 切割成一块块 buffer 的时候，就得到了一个个的 packet。发送数据时，一个个发包，形成一个 stream。接收到 stream 后，再按照具体的协议切割还原成发送方所发送的包。

## Q3

*medium*

简单看了下，感觉是在sql注入

看http,看到后面可以发现

```
157893	300.720875	192.168.173.1	192.168.173.134	HTTP	329	GET /index.php?id=1%27and%20(select%20ascii(substr((select%20skyflag_is_here2333%20from%20flag%20limit%200,1),8,1)))=42%23 HTTP/1.1 
```

sql注入恢复数据吧。

## Q4

*medium*

简单看一下http,大量的404。然后看后面发现了

```
3860	14.985263	192.168.1.101	192.168.1.105	HTTP	226	HEAD /.caidao.php.swp HTTP/1.1 
```
菜刀

然后还看到了shell，backdoor之类的，应该是菜刀传马吧。
