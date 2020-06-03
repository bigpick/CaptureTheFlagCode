#!/usr/bin/env python3
import re

# From Wikipedia:
character_frequencies = {
    'a': .08497, 'b': .01492, 'c': .02202, 'd': .04253,
    'e': .11162, 'f': .02228, 'g': .02015, 'h': .06094,
    'i': .07546, 'j': .00153, 'k': .01292, 'l': .04025,
    'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
    'q': .00095, 'r': .07587, 's': .06327, 't': .09356,
    'u': .02758, 'v': .00978, 'w': .02560, 'x': .00150,
    'y': .01994, 'z': .00077
}
# Load Cipher text
with open('decode_this.txt', 'r') as infile:
    emoji_text = infile.read()
# Strip HTML stuff, already had removed the <p> tags
emoji_codes = [x.strip() for x in emoji_text.split('&#') if x != ""]
code_frequencies = {}
emoji_text = emoji_text.replace("&", "").replace("#", "")
# We don't care about the _ { }, only want the emoji codes
for x in emoji_codes:
    code = re.sub("[^0-9]", "", x)
    try:
        code_frequencies[code] += 1
    except KeyError:
        code_frequencies[code] = 1
# Now Sort the emoji code, most frequent first
sorted_code_frequencies = {k: v for k, v in sorted(code_frequencies.items(), key=lambda item: item[1], reverse=True)}
# Also sort the letter frequencies, most frequent first
sorted_letter_frequencies = {k: v for k, v in sorted(character_frequencies.items(), key=lambda item: item[1], reverse=True)}
# Make the sorted letter keys to a list for easier indexing
most_frequent_letters = list(sorted_letter_frequencies)
# We need to be able to replace a-z
assert len(sorted_code_frequencies) == 26

# Do the replacing
i = 0
for k, v in sorted_code_frequencies.items():
    print(f"Replacing {k} (occurences: {v}) with {most_frequent_letters[i]}")
    emoji_text = emoji_text.replace(k, most_frequent_letters[i])
    i +=1

# Scrambled text
print(emoji_text)

# From quipqup, just manually copied the results
emoji_text = emoji_text.upper()
emoji_text = emoji_text.replace("A", "e")
emoji_text = emoji_text.replace("B", "l")
emoji_text = emoji_text.replace("C", "y")
emoji_text = emoji_text.replace("D", "p")
emoji_text = emoji_text.replace("E", "o")
emoji_text = emoji_text.replace("F", "c")
emoji_text = emoji_text.replace("G", "g")
emoji_text = emoji_text.replace("H", "x")
emoji_text = emoji_text.replace("I", "h")
emoji_text = emoji_text.replace("J", "q")
emoji_text = emoji_text.replace("K", "d")
emoji_text = emoji_text.replace("L", "s")
emoji_text = emoji_text.replace("M", "a")
emoji_text = emoji_text.replace("N", "f")
emoji_text = emoji_text.replace("O", "r")
emoji_text = emoji_text.replace("P", "b")
emoji_text = emoji_text.replace("Q", "v")
emoji_text = emoji_text.replace("R", "n")
emoji_text = emoji_text.replace("S", "j")
emoji_text = emoji_text.replace("T", "t")
emoji_text = emoji_text.replace("U", "u")
emoji_text = emoji_text.replace("V", "w")
emoji_text = emoji_text.replace("W", "z")
emoji_text = emoji_text.replace("X", "i")
emoji_text = emoji_text.replace("Y", "k")
emoji_text = emoji_text.replace("Z", "m")

# Look for castorsctf{ in the bottom output
print(emoji_text)
