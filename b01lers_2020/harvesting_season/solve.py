#!/usr/bin/env python
import binascii

# From exiftool fr3sh_h4rv3st.jpg
# Could try a python wrapper for it, but meh downloads
artist = "1921754512366910363569105a73727c592c5e5701715e571b76304d3625317c1b72744d0d1d354d0d1d73131c2c655e"

# Hint is that the key is 4 bytes, can play around with first 8 bytes of the input
# in the python interpreter to try to find out the key used, since we know the
# beginning of the output has to be pctf and XOR is it's own inverse
KEY = "69420123"

# Set our byte size for the sliding window
chunk=8
index = 0
thelaunchcode = []

# Slide through the artist string and XOR each group with our key
for window in range(int(len(artist)/chunk)):
    if index == 0:
        window_bytes = artist[index:index+chunk]
        thelaunchcode.append(binascii.unhexlify(''.join(format(int(a, 16) ^ int(b, 16), 'x') for a,b in zip(window_bytes, KEY))))
    else:
        window_bytes = artist[index*chunk:index*chunk+chunk]
        thelaunchcode.append(binascii.unhexlify(''.join(format(int(a, 16) ^ int(b, 16), 'x') for a,b in zip(window_bytes, KEY))))
    # Increment index for our next window
    index += 1

# Look door, get key
print(b''.join(thelaunchcode))
