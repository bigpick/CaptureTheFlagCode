#!/usr/bin/env python3.8
from Crypto.PublicKey import RSA
from sympy.ntheory import factorint
# pip3.8 install factordb-pycli
from factordb.factordb import FactorDB

def load_pubkey(filename):
    f = open(filename,'r')
    key = RSA.import_key(f.read())
    N = key.n
    e = key.e
    return N, e


def check_factordb(N):
    factorized = FactorDB(N)
    factorized.connect()
    factor_list = factorized.get_factor_list()
    assert(len(factor_list) == 2)
    p, q = factor_list[0], factor_list[1]
    return p, q


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():
    N, e = load_pubkey('pubkey.pem')
    print("N: ", N)
    print("e: ", e)

    p, q = check_factordb(N)
    print("p: ", p)
    print("q: ", q)
    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    gcd, a, b = egcd(e, phi)
    d = a
    print("d:  " + str(d) );

    # Decrypt
    pt = pow(ct, d, N)
    print("Plaintext: ", pt)


if __name__=='__main__':
    main()
