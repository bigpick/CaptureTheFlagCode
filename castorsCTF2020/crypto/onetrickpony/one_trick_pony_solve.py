#!/usr/bin/env python
from pwn import *

ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ#{}_-+[,.=!@$%&0123456789 "

# Initially, we know starts with F#{
key_so_far="castorsCTF{"

while 1<2:
    conn = remote('chals20.cybercastors.com', 14422)
    i = 0
    for _ in range(100):
        conn.sendline(key_so_far+ALPHABET[i])
        response = conn.recvline().split()[-1].decode("utf-8")
        size = len(key_so_far+ALPHABET[i])
        if response == ("b''"):
            # Found next char
            key_so_far+=ALPHABET[i]
            print(key_so_far)
            i=0
            continue
        # Try lower case
        if ALPHABET[i].isalpha():
            conn.sendline(key_so_far+(ALPHABET[i].lower()))
            response = conn.recvline().split()[-1].decode("utf-8")
            if response == ("b''"):
                # Found next char
                key_so_far+=ALPHABET[i].lower()
                print(key_so_far)
                i=0
        i+=1
