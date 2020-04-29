#!/usr/bin/env python3.8
import numpy
import string
alpha=string.ascii_lowercase
alpha=" "+alpha
keyMatrix = numpy.array([
                          [1.6,  -1.4,  1.8],
                          [2.2,  -1.8,  1.6],
                          [-1,     1,    -1]
                         ])
#String
#37 36 -1 34 27 -7 160 237 56 58 110 44 66 93 22 143 210 49 11 33 22
cipherMatrix = numpy.array([
                [37, 237, 22],
                [36, 56, 143],
                [-1, 58, 210],
                [34, 110, 49],
                [27, 44, 11],
                [-7, 66, 33],
                [160, 93, 22]
               ])

cipherMatrix2 = numpy.array([[37, 34, 160, 58, 66, 143, 11],
                             [36, 27, 237, 110, 93, 210, 33],
                             [-1, -7, 56, 44, 22, 49, 22]
                            ])

for row in range(3):
    for col in range(7):
      print(cipherMatrix2[row][col], end=' ')
    print()

product = numpy.matmul(keyMatrix, cipherMatrix2)
flag = ""
digits = []
for col in range(7):
    for row in range(3):
        flag+=alpha[int(round(product[row][col]))]
        digits.append(int(round(product[row][col])))
print(flag)
print(digits)
