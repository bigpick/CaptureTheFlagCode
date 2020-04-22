#!/usr/bin/env python3.8

import argparse
import sys
import operator
from string import printable
from codecs import encode, decode
from base64 import b64decode
from typing import Tuple, List
from statistics import mean


def parse_cmdline_args() -> str:
    """
    Parse single command line argument as path to a file

    :returns: Passed in file name/path as string
    """
    parser = argparse.ArgumentParser(description='Process command line args.')
    parser.add_argument('filename', metavar='f', type=str, nargs=1,
                        help='Path to file consisting of base64 encoded data and encrypted with repeating key XOR')
    args = parser.parse_args()
    return args.filename


def find_hamming_distance(string1: bytes, string2: bytes) -> int:
    """
    Find hamming distance between two strings.
    The Hamming distance is just the number of differing bits.

    :param string1: The first string to be compared, as bytes
    :param string2: The second string to be compared, as bytes
    :returns: The hamming distance between the two params as an int
    """
    distance = 0
    for bit1, bit2 in zip(string1, string2):
        diff = bit1 ^ bit2
        # XOR only returns 1 if bits are different
        distance += sum([1 for bit in bin(diff) if bit == '1'])
    return distance


def find_average_keysize_distance(keysize: int, ciphertext: bytes, num_chunks:int) -> float:
    """
    Find the keysize difference between two chunks of size keysize.
    Start at index 0 and iterate through adjacent neighbors num_chunks times.
    This is done with a sliding window approach, i.e
        [0:2] vs [2:4]
        [2:4] vs [4:6]
        [4:6] vs [6-8]
        ... num chunks times

    :param keysize: The expected keysize, as an integer.
    :param ciphertext: The ciphertext string, as bytes
    :param num_chunks: The number of chunk iterations to try
    :returns: A float representing the mean distance of all distances for that keysize
    """
    distances = []

    for iteration in range(num_chunks):
        try:
            start1 = 0 + (iteration * keysize)
            end1   = start1 + keysize
            start2 = end1
            end2   = start2 + keysize
            distance = find_hamming_distance(ciphertext[start1:end1], ciphertext[start2:end2])
            distances.append(distance / keysize)
        except IndexError:
            continue

    return mean(distances)


def find_most_likely_keysize(start_size: int, end_size: int, iterations: int, ciphertext: bytes) -> int:
    """
    Finds the most likely key's length of repeating key XOR encrypted data.

    :param start_size: The lower bound, inclusive, of key size to try, as in int.
    :param end_size: The upper bound, exclusive, of key size to try, as in int.
    :param iterations: The number of sliding window neighbors iterations to attempt, as an int.
    :param ciphertext: The input ciphertext, as bytes
    :returns: An integer representing the most likely key length.
    """
    keysize_distances = {}
    for keysize in range(start_size, end_size):
        # Try up to 50 sliding window neighbors
        # ie. compare ciphertext[0:2] vs ciphertext[2:4]
        #             ciphertext[2:4] vs ciphertext[4:6]
        #             ... 48 more times, where the start/stop ranges match the keysize
        avg_distance = find_average_keysize_distance(keysize, ciphertext, iterations)
        keysize_distances[keysize] = avg_distance

    most_likely_keysize = sorted(keysize_distances.items(), key=lambda x: x[1])[0][0]
    return most_likely_keysize


def transpose_ciphertext_to_chunks(ciphertext_chunked: List[bytes], most_likely_keysize: int) -> List[bytes]:
    """
    Transpose the blocks: make a block that is the first byte of every block,
    and a block that is the second byte of every block, and so on.

    :param ciphertext_chunked: List of bytes of ciphertext were each index is
                               of an ordered chunk of original ciphertext, in
                               size most_likely_keysize.
    :param most_likely_keysize: The most likely length of repeating XOR key,
                                as an int.
    :returns: A list of transposed chunksm were each index is the Nth set of
              bytes from the original ciphertext_chunked list.
    """
    transposed_chunks = []
    for idx in range(most_likely_keysize):
        # Create a block made up of each nth byte, where n
        # is the keysize
        result_chunk = b""
        for og_chunk in ciphertext_chunked:
            result_chunk += og_chunk[idx:idx+1]
        transposed_chunks.append(result_chunk)
    return transposed_chunks


def get_english_score(input_bytes: bytes) -> int:
    """
    Compares each input byte to a character frequency
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language

    Taken from https://laconicwolf.com/2018/05/29/cryptopals-challenge-3-single-byte-xor-cipher-in-python/

    :param input_bytes: The input string of bytes to have it's character's
                        frequencies analyzed.
    :returns: And integer representing the total sum of encountered character frequencies.
              Higher means a more-likely-valid english string.
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
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def do_single_xor(input_val: bytes, single_key: int) -> bytes:
    """
    Do single byte/key XOR against an input byte string.

    :param input_val: The input string of bytes to be encrypted.
    :param single_key: The single byte key to be used for the XOR.
    :returns: A bytes string representing the encrypted data.
    """
    result = b''
    for byte in input_val:
        result+=bytes([byte ^ single_key])
    return result


def brute_single_printable_xor(ciphertext_transposed: List[bytes]) -> str:
    """
    Try to find the most likely key for a single byte XOR given only the ciphertext.

    Takes as input a list of ciphertext chunks, where each index is the original
    ciphertext's chunks Nth set of bytes. That is, for each keysize length chunk
    from the original ciphertext, the first item in the passed in argument list
    is the each original ciphertext's chunks 0th byte.

    Scoring is based on the resulting plaintext's letter frequency. The highest
    scored result is returned.

    :param ciphertext_transposed: A list of chunks of ciphertext where each index
                                  is the original keysize chunked ciphertext's
                                  Nth set of bytes.
    :returns: The byte most likely to be the key.
    """
    top_scores = []
    for block in ciphertext_transposed:
        scores = []
        # Try every printable char
        for maybe_key in printable:
            #print("Trying key: ", maybe_key)
            plaintext = do_single_xor(block, ord(maybe_key))
            # Score the resulting plaintext
            score = get_english_score(plaintext)
            # Append score and plaintext for temporary history
            scores.append([plaintext, score, maybe_key])
        # Sort the temporary history in reverse, so most likely to be valid based
        # on frequency is first
        scored = sorted(scores, key=operator.itemgetter(1), reverse=True)
        top_scores.append(scored[0][2])

    return ''.join(top_scores)


def repeating_key_xor(input_str: bytes, key: bytes) -> bytes:
    """
    Execute repeating key XOR against a given byte string.

    :param input_str: The input text as bytes to be XORed.
    :param key: The set of bytes to be used as the XOR key.
    :returns: A string of bytes representing the XOR'ed data.
    """
    cipher = b''
    idx = 0
    for byte in input_str:
        cipher+=bytes([byte ^ key[idx]])
        idx = (idx+1) % len(key)
    return cipher

def main():
    f = parse_cmdline_args()[0]
    with open(f, 'r') as infile:
        b64_encoded = infile.readlines()

    # Test our hamming distance calulcator with the given values
    test1 = "this is a test".encode()
    test2 = "wokka wokka!!!".encode()
    assert(find_hamming_distance(test1, test2) == 37)

    # load given ciphertext file and un-base64 it
    ciphertext = b64decode('\n'.join([x.strip() for x in b64_encoded if x != ""]))

    most_likely_keysize = find_most_likely_keysize(2, 41, 50, ciphertext)
    print("== Most likely keysize: ", most_likely_keysize)
    # Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length
    ciphertext_broken = [ciphertext[x:x+most_likely_keysize] for x in range(0, len(ciphertext), most_likely_keysize)]
    # Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on
    ciphertext_transposed = transpose_ciphertext_to_chunks(ciphertext_broken, most_likely_keysize)
    # Solve each block as if it was single-character XOR. You already have code to do this.
    most_likely_key = brute_single_printable_xor(ciphertext_transposed)
    print("== Most likely key: \"" + most_likely_key + "\"")

    print("== Results after repeating XOR decrypt with most likely key: ")
    cipher = repeating_key_xor(ciphertext, most_likely_key.encode())
    print(cipher.decode("ascii"))


if __name__=='__main__':
    main()

