#!/usr/bin/env python3.8

import operator
import argparse

def parse_cmdline_args() -> str:
    parser = argparse.ArgumentParser(description='Process command line args.')
    parser.add_argument('filename', metavar='f', type=str, nargs=1,
                        help='Path to file consisting of hex strings')
    args = parser.parse_args()
    return args.filename


def main():
    f = parse_cmdline_args()[0]

    with open(f, 'r') as infile:
        data = [x.strip() for x in infile.readlines()]

    lens = {}
    for line in data:
        try:
            lens[len(set(list(line[i:i+16] for i in range(0, len(line), 16))))] += 1
        except KeyError:
            lens[len(set(list(line[i:i+16] for i in range(0, len(line), 16))))] = 1

    (most_likely_encrypted_size, occurences) = sorted(lens.items(), key=operator.itemgetter(0))[0]
    print("Most likely encrypted line unique chunk size: ", most_likely_encrypted_size)
    print("Number of occurences: ", occurences)
    # Find any possible one with unique size
    for line in data:
        if len(set(list(line[i:i+16] for i in range(0, len(line), 16)))) == most_likely_encrypted_size:
            print(line)


if __name__ == '__main__':
    main()
