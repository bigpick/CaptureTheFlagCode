#!/usr/bin/env python3.8

import argparse
from base64 import b64decode
from Crypto.Cipher import AES

KEY="YELLOW SUBMARINE"

def parse_cmdline_args() -> str:
    parser = argparse.ArgumentParser(description='Process command line args.')
    parser.add_argument('filename', metavar='f', type=str, nargs=1,
                        help='Path to file consisting of hex strings')
    args = parser.parse_args()
    return args.filename


def main():
    f = parse_cmdline_args()[0]
    with open(f, 'r') as infile:
        ciphertext = b64decode(infile.read())

    c = AES.new(KEY.encode(), AES.MODE_ECB)
    print("Decripted data:", c.decrypt(ciphertext).decode())


if __name__ == '__main__':
    main()
