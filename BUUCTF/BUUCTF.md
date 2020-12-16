# BUUCTF


<!-- vim-markdown-toc GFM -->

* [PWN](#pwn)
* [WEB](#web)
	* [](#)
* [REAL](#real)
* [CRYPTO](#crypto)
	* [变异凯撒](#变异凯撒)
* [BASIC](#basic)
* [MISC](#misc)
	* [金三胖](#金三胖)
	* [二维码](#二维码)

<!-- vim-markdown-toc -->

## PWN

## WEB

### 
f12查看找到`source.php`,审计
`/hint.php`中看到`flag not here, and flag in ffffllllaaaagggg`

```php
    if (! empty($_REQUEST['file'])
        && is_string($_REQUEST['file'])
        && emmm::checkFile($_REQUEST['file'])
```
`/?file=`

```php
            $_page = mb_substr(
                $_page,
                0,
                mb_strpos($_page . '?', '?')
            );
```

mb_substr — Get part of string
`mb_substr ( string $string , int $start [, int|null $length = null [, string|null $encoding = null ]] ) : string`

mb_strpos — Find position of first occurrence of string in a string
`mb_strpos ( string $haystack , string $needle [, int $offset = 0 [, string|null $encoding = null ]] ) : int|false`

`/?file=hint.php?../../../../../ffffllllaaaagggg`

## REAL

## CRYPTO

### 变异凯撒

加密密文：afZ_r9VYfScOeO_UL^RWUc
格式：flag{ }

```
>>> print(ord("f")-ord("a"))
5
>>> print(ord("l")-ord("f"))
6
>>> print(ord("a")-ord("Z"))
7
```

```python
str = "afZ_r9VYfScOeO_UL^RWUc"
index = 5

for char in str:
    print(chr(ord(char)+index),end="")
    index += 1
```

## BASIC

## MISC

### 金三胖

gif中flag一闪而过，使用stegsolve>frame browser逐帧查看
`flag{he11ohongke}`

### 二维码

https://zxing.org/w/decode.jspx 扫描二维码`secret is here`
binwalk查看发现有zip,`-Me`提取，zip需要pw.
`fcrackzip`暴力破解
`fcrackzip -c "aA1" -b -l 4-6 -u 1D7.zip`
`-c "aA1"`字符集大小写字母和数字
`-b`暴力
`-l`len
`-u`只显示爆破出来的
找到密码7639
得到flag
