# bugku web


<!-- vim-markdown-toc GFM -->

* [web2](#web2)
* [计算器](#计算器)
* [web基础$_GET](#web基础_get)
* [web基础$_POST](#web基础_post)
* [矛盾](#矛盾)
* [web3](#web3)
* [域名解析](#域名解析)
* [你必须让他停下](#你必须让他停下)
* [变量1](#变量1)
* [web5](#web5)
* [头等舱](#头等舱)
* [网站被黑](#网站被黑)

<!-- vim-markdown-toc -->

## web2

F12 就可以看到

## 计算器

前端修改 `<input type="text" class="input" maxlength="100">`, 提交验证码即可

## web基础$_GET

`?what=flag`

## web基础$_POST

POST 提交 what=flag

## 矛盾

== 是弱相等，这里用1+字母的话，比较的时候会去掉字母。
`?num=1a`

## web3

F12 看源码， 看到注释`<!--&#75;&#69;&#89;&#123;&#74;&#50;&#115;&#97;&#52;&#50;&#97;&#104;&#74;&#75;&#45;&#72;&#83;&#49;&#49;&#73;&#73;&#73;&#125;-->`

html解码得到flag

## 域名解析

修改 /etc/hosts, 添加一行`ip domain`，然后访问这个domain即可

## 你必须让他停下

bp抓包后在repeater不停重放，在img为10.jpg时得到flag

## 变量1

审计代码，args必须是字符串，`/^`是开头，`\w+`字符串，`$/`结尾

var_dump — Dumps information about a variable
$$: Variable variables. 

```
$a = 'hello';
$$a = 'world';
```

$a with contents "hello" and $hello with contents "world".

$GLOBALS — References all variables available in global scope

flag在变量里, $args=GLOBALS, 则$$args就是$GLOBALS

`?args=GLOBALS`

## web5

jsfuck, decode.

## 头等舱

F12 view source, nothing. As the hint goes, it should be in Response Header.

## 网站被黑




