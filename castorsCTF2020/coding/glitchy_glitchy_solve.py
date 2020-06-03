#!/usr/bin/env python3

from pwn import *

from binascii import hexlify
from hexhamming import hamming_distance

context.log_level = "debug"

r = remote('chals20.cybercastors.com', 14432)
r.recvuntil('Choice: ')
r.sendline("6")

for _ in range(1001):
    r.recvuntil('Choice: ')
    r.sendline("0")
    r.recvuntil('Choice: ')
    r.sendline("1")

r.recvuntil('Choice: ')
r.sendline("5")
r.stream()
