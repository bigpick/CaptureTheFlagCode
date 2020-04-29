#!/usr/bin/env python3.8

from intercepted import *

print(n)
print(e)
print(ct)

out = ''
for l in ct:
    for j in range(32, 127):
        if pow(j, e, n) == l:
            out += chr(j)
            break
print(out)
