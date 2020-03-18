#!/usr/bin/env python
import random
import re
import time
import subprocess
from subprocess import PIPE

from pwn import *

context.bits= '64'
context.endian= 'little'
context.log_level = 'debug'

conn = remote('pwn.ctf.b01lers.com', 1003)

generated_randoms = []
delta = 0
seed = int(time.time()) + 2

stdout = conn.recvuntil("would you like to buy? ")
model = re.compile(b'Meshuggah-[0-9]+')
first_three_rands = [int(x[10:].decode("utf-8")) for x in model.findall(stdout)]
print(first_three_rands)

while len([i for i, j in zip(first_three_rands, generated_randoms[:3]) if i == j]) != 3:
    # Try new seeds, +1 -1, +2 -2, +3 -3, etc...
    if delta == 0:
        print(f"LD_LIBRARY_PATH=/root/meshuggah2 ./rng {seed}")
        generated_randoms = subprocess.run([f"./rng {seed}"], shell=True, stdout=PIPE).stdout.decode("utf-8").split()
        generated_randoms = list(map(int, generated_randoms))
        print(len([i for i, j in zip(first_three_rands, generated_randoms[:3]) if i == j]))
    else:
        generated_randoms = subprocess.run([f"./rng {seed+delta}"], shell=True, stdout=PIPE).stdout.decode("utf-8").split()
        generated_randoms = list(map(int, generated_randoms))
        print(len([i for i, j in zip(first_three_rands, generated_randoms[:3]) if i == j]))
        if len([i for i, j in zip(first_three_rands, generated_randoms[:3]) if i == j]) == 3:
            break
        generated_randoms = subprocess.run([f"./rng {seed-delta}"], shell=True, stdout=PIPE).stdout.decode("utf-8").split()
        generated_randoms = list(map(int, generated_randoms))
    delta += 1

# Send our data now that we have found one that matches the first 3 entries
for i in range(3, 95):
    conn.sendline(str(generated_randoms[i]))
    if i != 94:
        conn.recvuntil("would you like to buy? ")

# Pwntools way to just receive arbitrary amount of lines
while 1<2:
    try:
        print(conn.recvlineS())
    except EOFError as e:
        print()
        break
