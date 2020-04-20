#!/usr/bin/env python3.8

import argparse
from codecs import encode, decode
from typing import List
from string import printable
from collections import Counter
import operator

import gibberishclassifier


def parse_cmdline_args() -> List[str]:
    parser = argparse.ArgumentParser(description='Process command line args.')
    parser.add_argument('strings', metavar='S', type=str, nargs='+',
                        help='At least one plaintext hex string to be encoded to base64')
    args = parser.parse_args()
    return args.strings[0]


def main():
    to_be_decoded = parse_cmdline_args()
    decoded = decode(to_be_decoded, 'hex')
    scores = []
    for maybe_key in printable:
        result = ''
        for c in decoded:
            result+=chr(int(c) ^ ord(maybe_key))
        score = gibberishclassifier.classify(result)
        scores.append([result, score])

    scored = sorted(scores, key=operator.itemgetter(1))
    print("Possible entries, sorted by least-likely-gibberish to most-likely-gibberish:")
    for possible_entry in scored:
        print(possible_entry[0])


if __name__=='__main__':
    main()
