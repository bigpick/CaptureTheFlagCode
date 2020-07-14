#!/usr/bin/env python3

# For when you have a really large N, a _really_ small e, and can just find the pt by taking the e-th root of c

import gmpy2
from Crypto.Util.number import long_to_bytes as ltb
n = xxx
e = yyy # something really small, like 3, or 13
c = gmpy2.mpz(zzz)

gmpy2.get_context().precision=200
x = int(gmpy2.root(c,e))
assert pow(x,e,n) == c

print(ltb(x)[::-1])
