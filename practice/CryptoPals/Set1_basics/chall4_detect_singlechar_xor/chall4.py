#!/usr/bin/env python3.8

#!/usr/bin/env python3.8

import argparse
from codecs import encode, decode
from typing import List
from string import printable
from collections import Counter
import operator


def get_english_score(input_bytes):
    """Compares each input byte to a character frequency
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language

    Taken from https://laconicwolf.com/2018/05/29/cryptopals-challenge-3-single-byte-xor-cipher-in-python/
    """

    # From https://en.wikipedia.org/wiki/Letter_frequency
    # with the exception of ' ', which I estimated.
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000, '\\x': -100
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def do_single_xor(input_val: bytes, single_key: int) -> bytes:
    result = b''
    for byte in input_val:
        result+=bytes([byte ^ single_key])
    return result


def parse_cmdline_args() -> str:
    parser = argparse.ArgumentParser(description='Process command line args.')
    parser.add_argument('filename', metavar='f', type=str, nargs=1,
                        help='Path to file consisting of hex strings')
    args = parser.parse_args()
    return args.filename


def main():
    # Fetch the file name and read lines to list
    f = parse_cmdline_args()[0]
    with open(f, 'r') as infile:
        to_be_decoded = infile.readlines()

    # Strip newlines and empty entries:
    to_be_decoded = [x.strip() for x in to_be_decoded if x != ""]

    # Iterate through each line in the file, and try xor'ing with every printable
    # value in ASCII. Score the frequency results, and add the top 5 results to the
    # running top scores list
    top_scores = []
    for line in to_be_decoded:
        # Hexstring to bytes
        cipher_bytes = decode(line, 'hex')
        scores = []
        # Try every printable char
        for maybe_key in printable:
            # XOR or now-in-bytes hexstring with the current char
            plaintext = do_single_xor(cipher_bytes, ord(maybe_key))
            # Score the resulting plaintext
            score = get_english_score(plaintext)
            # Append score and plaintext for temporary history
            scores.append([plaintext, score])
        # Sort the temporary history in reverse, so most likely to be valid based
        # on frequency is first
        scored = sorted(scores, key=operator.itemgetter(1), reverse=True)
        # Append the top 5 to the top prospects so far
        for i in range(5):
            top_scores.append(scored[i])

    # Sort top prospects in reverse, so most likely to be valid based
    # on frequency is first
    top_scored = sorted(top_scores, key=operator.itemgetter(1), reverse=True)
    # Loop through and try to convert to ASCII and print (helps weed out further
    # noise):
    for most_likely in top_scored:
        try:
            print(most_likely[0].decode('ascii'))
        except UnicodeDecodeError:
            pass


if __name__=='__main__':
    main()
