#!/usr/bin/env python3
from pwn import *

# https://eddmann.com/posts/implementing-rot13-and-rot-n-caesar-ciphers-in-python/
def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)


r = remote('jh2i.com', 50034)
flag = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
flag = list(flag)

sendthisback = r.recvline().decode().strip()
r.sendline(sendthisback)

i = 0
while 1<2:
    if i % 25 == 0:
        print(''.join(flag))

    to_rot = r.recvline().decode().strip()

    for i in range(26):
        decoded = rot_alpha(-i)(to_rot)
        if decoded.startswith("send back this line exactly."):
            if "no flag here" in decoded:
                r.sendline(decoded)
                i += 1
                break
            else:
                clue = decoded.split('exactly.')[-1]
                index = clue.split()[1]
                char = clue.split()[-1][1]
                flag[int(index)] = char
                r.sendline(decoded)
                i += 1
                break


