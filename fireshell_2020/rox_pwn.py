#!/usr/bin/env python
from pwn import *

ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ#{}_-+[,.=!@$%&0123456789 "

# Initially, we know starts with F#{
key_so_far="F#{"
# key_so_far="F#{us"
# key_so_far="F#{us1n"
# key_so_far="F#{us1ng"
# key_so_far="F#{us1ng-"
# key_so_far="F#{us1ng-X"
# key_so_far="F#{us1ng-X0"
# key_so_far="F#{us1ng-X0r-"
# key_so_far="F#{us1ng-X0r-is"
# key_so_far="F#{us1ng-X0r-is-R"
# key_so_far="F#{us1ng-X0r-is-ROx"
# key_so_far="F#{us1ng-X0r-is-ROx-"
# key_so_far="F#{us1ng-X0r-is-ROx-4"
# key_so_far="F#{us1ng-X0r-is-ROx-4-l"
# key_so_far="F#{us1ng-X0r-is-ROx-4-l0"
# key_so_far="F#{us1ng-X0r-is-ROx-4-l0t}"

while 1<2:
    conn = remote('142.93.113.55', 31087)
    conn.recvuntil("to start: ")
    conn.sendline('start')
    i = 0
    for _ in range(100):
        try:
            conn.recvuntil('Input: ')
        except EOFError:
            break
        print("Trying: ", ALPHABET[i])
        print("Trying: ", key_so_far+ALPHABET[i])
        conn.sendline(key_so_far+ALPHABET[i])
        response = conn.recvline().split()[-1]
        print("RESPONSE: ", response)
        size = len(key_so_far+ALPHABET[i])
        print(size)
        if response == (b'\x00'*size):
            # Found next char
            key_so_far+=ALPHABET[i]
            i=0
            continue

        # Try lower case
        if ALPHABET[i].isalpha():
            try:
                conn.recvuntil('Input: ')
            except EOFError:
                break
            print("Trying: ", ALPHABET[i].lower())
            conn.sendline(key_so_far+(ALPHABET[i].lower()))
            response = conn.recvline().split()[-1]
            print("RESPONSE: ", response)
            if response == (b'\x00'*size):
                # Found next char
                key_so_far+=ALPHABET[i].lower()
                i=0
        i+=1
