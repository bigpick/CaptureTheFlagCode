#!/usr/bin/env python3.8
import string
import argparse

# To crack a 01248 password
# EXAMPLE:
#  ./01248_password.py 8842101220480224404014224202480122
#  (welldone)

alpha = string.ascii_lowercase

def parse_cmdline_args():
    parser = argparse.ArgumentParser(description='Process command line args.')
    parser.add_argument('strings', metavar='S', type=str, nargs=1,
                        help='One plaintext 01248 password string to decrypt')
    args = parser.parse_args()
    return args.strings[0]

if __name__=='__main__':
    to_decrypt = parse_cmdline_args()
    idx = 0
    chunk = []
    while 1<2:
        try:
            if to_decrypt[idx] == "0":
                val=alpha[sum(chunk)-1]
                print(val, end='')
                chunk = []
                idx+=1
            else:
                chunk.append(int(to_decrypt[idx]))
                idx+=1
        except IndexError:
            # End
            val=alpha[sum(chunk)-1]
            print(val, end='')
            break
    print()
