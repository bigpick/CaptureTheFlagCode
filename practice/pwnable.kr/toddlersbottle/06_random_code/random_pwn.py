#!/usr/bin/python
from pwn import *

# Our payload to XOR with the "Random" value to get 0xdeadbeef
payload = '18021479654816648'

# Start a new ssh session to the box:
session = ssh(host='pwnable.kr', user='random', password='guest', port=2222)
assert session.connected()

# Execute ./random on the session:
process = session.process(executable='./random')

# Send our payload to it, since it'll expect us to enter the value to STDIN:
process.sendline(payload)
while 1<2:
    try:
        print(process.recvlineS())
    except EOFError as e:
        break

