#!/usr/bin/env python3

from pwn import *
from chepy import Chepy
from base64 import b64decode
context.log_level = "debug"

r = remote('chals20.cybercastors.com', 14430)
r.recvuntil('when ready.\n')
r.sendline()

while 1<2:
    problem = r.recvline()
    problem = problem.decode().strip().split()

    octal_ = ""
    hex_ = ""
    for term in problem:
        n = int(term, 2)
        octal_ += (n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
    for term in octal_.split():
        n = int(term, 8)
        hex_ += (n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
    b64 = bytearray.fromhex(hex_.replace(" ", "")).decode()
    r.sendline(b64decode(b64))
    r.recvline() # Correct answer!

