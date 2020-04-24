#!/usr/bin/env python3.8

import argparse
from codecs import encode, decode
from typing import Tuple


def parse_cmdline_args() -> Tuple[str, int]:
    parser = argparse.ArgumentParser(description='Process command line args.')
    parser.add_argument('string', metavar='S', type=str, nargs=1,
                        help='The plaintext string to be padded')
    parser.add_argument('block_size', metavar='BS', type=int, nargs=1,
                        help='The block/chunk size to be padded to')
    args = parser.parse_args()
    return args.string[0], args.block_size[0]


def pkcs7_pad(input_str: bytes, block_size: int) -> bytes:
    """
    Pad a given input byte string to a certain block size.

    :param input_str: The byte string to be padded.
    :param block_size: The size of block/chunk to pad to.
    :returns: The padded byte string.
    """
    to_pad = block_size - (len(input_str) % block_size)
    return input_str + ''.join([chr(to_pad) for _ in range(to_pad)])


def main():
    to_be_padded, block_size = parse_cmdline_args()
    padded = pkcs7_pad(to_be_padded, block_size)
    print(repr(padded))


if __name__=='__main__':
    main()

