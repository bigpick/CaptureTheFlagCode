#!/usr/bin/env python3
# I've hidden two cool images by XOR with the same secret key so you can't see them!
#
# lemur.png
#
# flag.png
import numpy as np
from PIL import Image, ImageChops

def main():
    # Open images
    im1 = Image.open("goose_stole_the_key.png")
    im2 = Image.open("chal.png")

    assert(im1.size == im2.size)
    width, height = im1.size
    image3 = Image.new('RGB', (width, height))

    for row in range(0, height):
        for col in range(0, width):
            r1, g1, b1 = im1.getpixel((col, row))[:3]
            r2, g2, b2 = im2.getpixel((col, row))[:3]
            r3 = r1 ^ r2
            g3 = g1 ^ g2
            b3 = b1 ^ b2
            image3.putpixel((col, row), (r3, g3, b3))

    image3.save('result.png')
    image3.show()


if __name__ == '__main__':
    main()
