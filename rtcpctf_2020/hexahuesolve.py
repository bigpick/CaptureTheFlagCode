#!/usr/bin/env python3.8

from PIL import Image
import numpy
from webcolors import rgb_to_name

# magenta is purple
# lime is green
alpha = {}
alpha["A"] = [["magenta","red"],["lime","yellow"], ["blue", "cyan"]]
alpha["B"] = [["red","magenta"],["lime","yellow"], ["blue", "cyan"]]
alpha["C"] = [["red","lime"],["magenta","yellow"], ["blue", "cyan"]]
alpha["D"] = [["red","lime"],["yellow","magenta"], ["blue", "cyan"]]
alpha["E"] = [["red","lime"],["yellow","blue"], ["magenta", "cyan"]]
alpha["F"] = [["red","lime"],["yellow","blue"], ["cyan", "magenta"]]
alpha["G"] = [["lime","red"],["yellow","blue"], ["cyan", "magenta"]]
alpha["H"] = [["lime","yellow"],["red","blue"], ["cyan", "magenta"]]
alpha["I"] = [["lime","yellow"],["blue","red"], ["cyan", "magenta"]]
alpha["J"] = [["lime","yellow"],["blue","cyan"], ["red", "magenta"]]
alpha["K"] = [["lime","yellow"],["blue","cyan"], ["magenta", "red"]]
alpha["L"] = [["yellow","lime"],["blue","cyan"], ["magenta", "red"]]
alpha["M"] = [["yellow","blue"],["lime","cyan"], ["magenta", "red"]]
alpha["N"] = [["yellow","blue"],["cyan","lime"], ["magenta", "red"]]
alpha["O"] = [["yellow","blue"],["cyan","magenta"], ["lime", "red"]]
alpha["P"] = [["yellow","blue"],["cyan","magenta"], ["red", "lime"]]
alpha["Q"] = [["blue","yellow"],["cyan","magenta"], ["red", "lime"]]
alpha["R"] = [["blue","cyan"],["yellow","magenta"], ["red", "lime"]]
alpha["S"] = [["blue","cyan"],["magenta","yellow"], ["red", "lime"]]
alpha["T"] = [["blue","cyan"],["magenta","red"], ["yellow", "lime"]]
alpha["U"] = [["blue","cyan"],["magenta","red"], ["lime", "yellow"]]
alpha["V"] = [["cyan","blue"],["magenta","red"], ["lime", "yellow"]]
alpha["W"] = [["cyan","magenta"],["blue","red"], ["lime", "yellow"]]
alpha["X"] = [["cyan","magenta"],["red","blue"], ["lime", "yellow"]]
alpha["Y"] = [["cyan","magenta"],["red","lime"], ["blue", "yellow"]]
alpha["Z"] = [["cyan","magenta"],["red","lime"], ["yellow", "blue"]]
alpha[" "] = [["white","white"],["white","white"], ["white", "white"]]
alpha["."] = [["black", "white"],["white","black"],["black","white"]]
alpha[","] = [["white", "black"],["black","white"],["white","black"]]
alpha["0"] = [["black", "gray"],["white","black"],["gray","white"]]
alpha["1"] = [["gray", "black"],["white","black"],["gray","white"]]
alpha["2"] = [["gray", "white"],["black","black"],["gray","white"]]
alpha["3"] = [["gray", "white"],["black","gray"],["black","white"]]
alpha["4"] = [["gray", "white"],["black","gray"],["white","black"]]
alpha["5"] = [["white", "gray"],["black","gray"],["white","black"]]
alpha["6"] = [["white", "black"],["gray","gray"],["white","black"]]
alpha["7"] = [["white", "black"],["gray","white"],["gray","black"]]
alpha["8"] = [["white", "black"],["gray","white"],["black","black"]]
alpha["9"] = [["black", "white"],["gray","white"],["black","gray"]]


im_array = numpy.asarray(Image.open('chall.png'))

rows, cols, depth = im_array.shape
flag = ""

# image is padded 2x2 with whitespace
for row in range(2, rows-2, 3):
    for col in range(2, cols-2, 2):
        print(row+2)
        tl = rgb_to_name(im_array[row][col])
        tr = rgb_to_name(im_array[row][col+1])
        ml = rgb_to_name(im_array[row+1][col])
        mr = rgb_to_name(im_array[row+1][col+1])
        ll = rgb_to_name(im_array[row+2][col])
        lr = rgb_to_name(im_array[row+2][col+1])
        letter = [[tl, tr], [ml, mr], [ll, lr]]
        for k in alpha:
            if alpha[k] == letter:
                flag += k
print(flag)
