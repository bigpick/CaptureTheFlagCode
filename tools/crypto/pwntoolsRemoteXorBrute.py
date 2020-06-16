#!/usr/bin/env python3.8
from pwn import *
import argparse
import string

ALPHABET = string.printable

def parse_cmdline_args() -> List[Tuple[str, str]]:
    parser = argparse.ArgumentParser(description='Process command line args.')
    parser.add_argument('--key_prefix', help="Expected key prefix", dest="key_prefix", type=str, nargs=1)
    parser.add_argument('--endpoint', help="Remote endpoint host to nc to", dest="endpoint", type=str, nargs=1)
    parser.add_argument('--port', help="Remote ednpoint port to nc to", dest="port", type=int, nargs=1)
    args = parser.parse_args()
    return args.xor_pair

def main(key_so_far: str, endpoint: str, port: int):
    while 1<2:
        conn = remote(endpoint, port)
        i = 0
        for _ in range(len(ALPHABET)):
            conn.sendline(key_so_far+ALPHABET[i])
            response = conn.recvline().split()[-1].decode("utf-8")
            if response == ("b''"):
                # Found next char
                key_so_far+=ALPHABET[i]
                print(key_so_far)
                i=0
                continue
            i+=1

if __name__=='__main__':
    args = parse_cmdline_args()
    # python3.8 pwntoolsRemoteXorBrute.py --key_prefix <flag{> --endpoint some.host.here --port 6969
    main(args.key_so_far, args.endpoint, args.port)
