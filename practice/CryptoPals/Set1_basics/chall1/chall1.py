#!/usr/bin/env python3.8

import argparse
from codecs import encode, decode
from typing import List


def parse_cmdline_args() -> List[str]:
    parser = argparse.ArgumentParser(description='Process command line args.')
    parser.add_argument('strings', metavar='S', type=str, nargs='+',
                        help='At least one plaintext hex string to be encoded to base64')
    args = parser.parse_args()
    return args.strings


def main():
    to_be_encoded = parse_cmdline_args()
    for entry in to_be_encoded:
        ## As bytes string
        # print(encode(decode(entry, 'hex'), 'base64').strip())
        print(encode(decode(entry, 'hex'), 'base64').decode().strip())


if __name__=='__main__':
    main()

