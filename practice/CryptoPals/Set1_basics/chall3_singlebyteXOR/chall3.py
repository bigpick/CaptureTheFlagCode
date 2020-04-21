#!/usr/bin/env python3.8

import argparse
from codecs import encode, decode
from typing import List
from string import printable
from collections import Counter
import operator


# Taken from https://laconicwolf.com/2018/05/29/cryptopals-challenge-3-single-byte-xor-cipher-in-python/
def get_english_score(input_bytes):
    """Compares each input byte to a character frequency
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language
    """
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


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
        result = b''
        for c in decoded:
            result+=bytes([int(c) ^ ord(maybe_key)])

        score = get_english_score(result)
        # Append score and plaintext for temporary history
        scores.append([result, score])

    scored = sorted(scores, key=operator.itemgetter(1), reverse=True)
    print("Possible entries, sorted by least-likely-gibberish to most-likely-gibberish:")
    for possible_entry in scored:
        print(possible_entry[0].decode("ascii"))


if __name__=='__main__':
    main()
