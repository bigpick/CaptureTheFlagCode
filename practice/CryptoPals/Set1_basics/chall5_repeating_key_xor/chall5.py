#!/usr/bin/env python3.8

import sys
import argparse
from codecs import encode, decode
import binascii
from typing import Tuple, List

KEY = "ICE"

def repeating_key_xor(input_str: bytes, key: bytes) -> bytes:
    cipher = b''
    idx = 0
    for byte in input_str:
        cipher+=bytes([byte ^ key[idx]])
        idx = (idx+1) % len(key)
    return cipher


def parse_cmdline_args() -> str:
    parser = argparse.ArgumentParser(description='Process command line args.')
    parser.add_argument('filename', metavar='f', type=str, nargs=1,
                        help='Path to file consisting of plain strings to be encrypted with repeating key XOR')
    args = parser.parse_args()
    return args.filename


def main():
    f = parse_cmdline_args()[0]
    with open(f, 'r') as infile:
        to_be_encrypted = infile.readlines()

    plaintext = '\n'.join([x.strip() for x in to_be_encrypted if x != ""])
    cipher = repeating_key_xor(plaintext.encode(), KEY.encode())
    print(cipher.hex())

    expected = ("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
                "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")
    assert(cipher.hex() == expected)


if __name__=='__main__':
    main()

