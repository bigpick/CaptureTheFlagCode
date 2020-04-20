#!/usr/bin/env python3.8

import sys
import argparse
from codecs import encode, decode
import binascii
from typing import Tuple, List


def xor_pair(s):
    try:
        x, y = map(str, s.split(','))
        if len(x) != len(y):
            print("ERR - xor pairings need to have equal length")
            sys.exit(1)
        return x, y
    except:
        raise argparse.ArgumentTypeError("XOR pairing must be x,y")


def parse_cmdline_args() -> List[Tuple[str, str]]:
    parser = argparse.ArgumentParser(description='Process command line args.')
    parser.add_argument('--xor_pair', help="XOR string", dest="xor_pair", type=xor_pair, nargs="+")
    args = parser.parse_args()
    return args.xor_pair


def main():
    xor_pairings = parse_cmdline_args()
    for pairing in xor_pairings:
        left = decode(pairing[0], 'hex')
        right = decode(pairing[1], 'hex')
        result= ''
        for i, c in enumerate(left):
            result+=str(hex(c ^ right[i])[2:])
        print(result)

if __name__=='__main__':
    main()

