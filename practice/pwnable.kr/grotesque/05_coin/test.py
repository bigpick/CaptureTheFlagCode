#!/usr/bin/env python3.8
from pwn import *
from typing import Tuple

def main():
    conn = remote('pwnable.kr', 9008)
    conn.recvuntil("Ready? starting in 3 sec ... -\n")
    conn.sendline("0 1-1 2")
    # Get flag
    while 1<2:
        try:
            print(conn.recvline().decode("utf-8"))
        except EOFError as e:
            break

if __name__ == '__main__':
    main()
