#!/usr/bin/env python3.8

from PIL import Image
import numpy as np
from os import path, listdir
from Crypto.Util.number import long_to_bytes

filelist = listdir('satan')
filelist.sort(key=lambda f: int(f[:-4]))

coordinates = []
pixels = [[0 for x in range(300)] for y in range(300)]
for file in filelist:
    im = Image.open(path.join('satan', file))
    pix = im.load()
    if( im.size != (1, 1)):
        print("Found irregular size pic")
        print(f)
    coords = long_to_bytes(int(file[:-4])).decode().split()
    x = int(coords[0])
    y = int(coords[1])
    #print("X: ", x, " Y: ", y)
    pixels[x][y] = pix[0,0]
    #coordinates.append([x, y])

array = np.array(pixels, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('result.png')

# print("Max X: ", max(map(lambda x: x[0], coordinates)))
# print("Max Y: ", max(map(lambda x: x[1], coordinates)))
#   Max X:  299
#   Max Y:  299
