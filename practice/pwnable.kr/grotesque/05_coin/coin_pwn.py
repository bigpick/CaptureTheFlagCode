#!/usr/bin/env python3.8
from pwn import *
from typing import Tuple

def get_challenge(conn: pwnlib.tubes.remote.remote) -> Tuple[int, int]:
    round = conn.recvline_regex("N=[0-9]+ C=[0-9]+").decode("utf-8").split()
    coins = round[0][2:]
    attempts = round[1][2:]
    return (int(coins), int(attempts))


def weigh(start: int, stop: int, conn: pwnlib.tubes.remote.remote) -> int:
    to_be_weighed = " ".join([str(x) for x in range(start, stop)])
    conn.sendline(to_be_weighed)
    weight = int(conn.recvline_regex("[0-9]+").decode("utf-8"))
    return weight


def search_coin(start: int, stop: int, end: int, conn: pwnlib.tubes.remote.remote) -> Tuple[int, int, int]:
    # We need to weigh from start to stop
    weight = weigh(start, stop, conn)
    if weight % 10 == 0:
        # coin not in here
        start = stop
        stop = (end+start) // 2
    else:
        # coin somewhere in here
        end = stop
        stop = (end+start) // 2
    return (start, stop, end)


def main():
    conn = remote('pwnable.kr', 9008)
    conn.recvuntil("Ready? starting in 3 sec ... -\n")

    for round_ in range(100):
        (coins, attempts) = get_challenge(conn)
        print(f"Round: {round_}")
        for attempt in range(attempts):
            if attempt == 0:
                start = 0
                if coins%2==0: end=coins else end=coins-1
                midpoint = end // 2
            (start, midpoint, end) = search_coin(start, stop, end, conn)
        conn.sendline(str(start))

    # Get flag
    while 1<2:
        try:
            print(conn.recvline().decode("utf-8"))
        except EOFError as e:
            break

if __name__ == '__main__':
    main()
