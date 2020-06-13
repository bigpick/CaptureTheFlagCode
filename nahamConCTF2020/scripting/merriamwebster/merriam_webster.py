#!/usr/bin/env python3

from pwn import *
import json

# pip install pattern
import pattern
from pattern.en import lemma, lexeme

import enchant
enchant_dict = enchant.Dict("en_US")

from nltk.corpus import words as nltk_words

#context.log_level = "debug"

r = remote('jh2i.com', 50012)

#with open('WebstersEnglishDictionary/dictionary.json', 'r') as infile:
#    dictionary = json.load(infile)

with open('english-words/words_dictionary.json', 'r') as infile:
    dictionary = json.load(infile)

for round_ in range(500):
    fake = 0
    fake_words = []
    # Can you tell me which words here are NOT real words IN CHRONOLOGICAL ORDER? Separate each by a space
    # Can you tell me which words here ARE real words IN CHRONOLOGICAL ORDER? Separate each by a space
    # Can you tell me which words here are NOT real words IN ALPHABETICAL ORDER? Separate each by a space
    # Can you tell me which words here ARE real words IN ALPHABETICAL ORDER? Separate each by a space.
    # Can you tell me how many words here ARE real words
    # Can you tell me how many words here are NOT real words
    chall = r.recvline().decode().strip()
    words = r.recvline().decode().strip().split()
    for word in words:
        valid = False
        if word in dictionary: valid = True
        if enchant_dict.check(word): valid = True
        #if word in nltk_words.words(): valid = True
        try:
            if "".join([lemma(word)]) in dictionary: valid = True
        except RuntimeError:
            if "".join([lemma(word)]) in dictionary: valid = True

        if not valid:
            #print("FAKE: ", word)
            fake_words.append(word)
            fake += 1

    #print("CHAL: ", chall)
    if "CHRONOLOGICAL ORDER" in chall:
        if "NOT" in chall:
            r.sendline(" ".join(fake_words).strip())
        else:
            r.sendline(" ".join([word for word in words if word not in fake_words]).strip())

    elif "ALPHABETICAL ORDER" in chall:
        if "NOT" in chall:
            r.sendline(" ".join(sorted(fake_words)).strip())
        else:
            r.sendline(" ".join(sorted([word for word in words if word not in fake_words])).strip())

    elif "ARE real words" in chall:
        r.sendline(str(len(words) - fake))
    else:
        r.sendline(str(fake))

    print(round_)
    if round_ == 499:
        print(r.stream())
    else:
        r.recvline() # correct!
