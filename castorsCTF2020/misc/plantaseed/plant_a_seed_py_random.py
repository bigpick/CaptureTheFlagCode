#!/usr/bin/python3
import datetime
import random

waterings = [150, 2, 103, 102, 192, 216, 52, 128, 9, 144, 10, 201, 209, 226, 22, 10, 80, 5, 102, 195, 23, 71, 77, 63, 111, 116, 219, 22, 113, 89, 187, 232, 198, 53, 146, 112, 119, 209, 64, 79, 236, 179]

then_date = "29/05/2020-20:00:00"
seed_then = datetime.datetime.strptime(then_date, "%d/%m/%Y-%H:%M:%S").replace(tzinfo=datetime.timezone.utc).timestamp()
random.seed(seed_then)

for day in range(len(waterings)):
    char = waterings[day] ^ random.randint(0, 255)
    print(chr(char), end='')
print()
