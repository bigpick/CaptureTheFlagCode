#!/usr/bin/env python3

from pwn import *

from binascii import hexlify
from hexhamming import hamming_distance

context.log_level = "debug"

r = remote('chals20.cybercastors.com', 14431)
r.recvuntil('when ready.\n')
r.sendline()

while 1<2:
    r.recvline() # machine is currently XX% calibrated
    sentence = " ".join(r.recvline().decode().strip().split()[2:]).encode()
    received = r.recvline().decode().strip().split()[2]
    hex_sentence = hexlify(sentence).decode()
    print(received)
    print(hex_sentence)
    r.sendline(str(hamming_distance(hex_sentence, received)))
    r.recvline() # Correct answer!

