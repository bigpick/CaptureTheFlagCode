#!/usr/bin/env python3
import binascii

with open('big_bird_tweets.txt', 'r') as infile:
    tweets = infile.readlines()

tweets.sort(key = lambda x: int(x.split()[1][1:]))
flag = ""
for tweet in tweets:
    hex_ = hex(int(tweet.strip().split()[-1]))[2:]

    if len(hex_) == 2:
        flag += hex_
    else:
        flag += "0" + hex_

data = binascii.a2b_hex(flag)
with open('image.png', 'wb') as file:
    file.write(data)
