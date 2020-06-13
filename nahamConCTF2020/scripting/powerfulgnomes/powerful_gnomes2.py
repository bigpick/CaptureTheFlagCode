#!/usr/bin/env python3

#1. Defeat the gnomes (level 10)
#2. Fight a dragon (level 7)
#3. Raid the cyclops (level 5)
#4. Plunder the pirates (level 3)
#5. Go on a journey (level 1)
#6. Browse the shop
#    1. sword (100 gold) (level 1)
#    2. bow (1000 gold) (level 3)
#    3. axe (2000 gold) (level 5)
#    4. missle launcher (10000 gold) (level 7)
#    5. tank (100000 gold) (level 10)
#7. End journey

from pwn import *
#context.log_level = "debug"

r = remote('jh2i.com', 50031)

def get_level_get_gold_next(buy_level, journey, amount):
    # Get level buy_level
    output = r.recvuntil('> ').decode().strip()
    r.sendline("6")
    output = r.recvuntil('exit the shop): ').decode().strip()
    r.sendline(buy_level)

    output = r.recvuntil('> ').decode().strip()
    r.sendline(journey)

    # Get gold till levelX
    gold_amt = 0
    while gold_amt < amount:
        output = r.recvuntil('> ').decode().strip()
        r.sendline(journey)
        gold = output.split()[16]
        gold_amt = int(output.split()[17])

get_level_get_gold_next("1", "5", 1000)
get_level_get_gold_next("2", "4", 2000)
get_level_get_gold_next("3", "3", 10000)
get_level_get_gold_next("4", "2", 100000)


output = r.recvuntil('> ').decode().strip()
r.sendline("6")
output = r.recvuntil('exit the shop): ').decode().strip()
# buy the tank
r.sendline("5")
output = r.recvuntil('> ').decode().strip()
# fuck those gnomes
r.sendline("1")
# get flag
print(r.stream())
