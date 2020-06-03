#!/usr/bin/env python3

from pwn import *
# pip install word2number
from word2number import w2n
import operator

context.log_level = "debug"
r = remote('chals20.cybercastors.com', 14429)

r.recvuntil('when ready.\n')
r.sendline()

ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "//": operator.floordiv }

while 1<2:
    problem = r.recvline().decode().strip().split()

    try:
        lhand = int(problem[-4])
    except ValueError:
        lhand = w2n.word_to_num(problem[-4])
    try:
        rhand = int(problem[-2])
    except ValueError:
        rhand = w2n.word_to_num(problem[-2])

    op = problem[-3]
    if op == "divided-by":
        op = "//"
    elif op == "multiplied-by":
        op = "*"
    elif op == "minus":
        op = "-"
    elif op == "plus":
        op = "+"

    r.sendline(str(ops[op](lhand, rhand)))
    r.recvline()

