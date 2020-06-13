#!/usr/bin/env python3.8
# pip3.8 install factordb-pycli
from factordb.factordb import FactorDB

def check_factordb(N):
    factorized = FactorDB(N)
    factorized.connect()
    factor_list = factorized.get_factor_list()
    print(factor_list)
    return factor_list

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():
    N = 31378393096163
    e = 65537
    ct = 26169559602561
    print("N: ", N)

    p, q = check_factordb(N)
    print("p: ", p)
    print("q: ", q)
    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    gcd, d, b = egcd(e, phi)
    print("d:  " + str(d) );

    # Decrypt
    pt = pow(ct, d, N)
    print("pt: ", pt)

if __name__=='__main__':
    main()
