#!/usr/bin/python3
from ctypes import *
import datetime

libc = cdll.LoadLibrary('/usr/lib/libc.dylib')
waterings = [150, 2, 103, 102, 192, 216, 52, 128, 9, 144, 10, 201, 209, 226, 22, 10, 80, 5, 102, 195, 23, 71, 77, 63, 111, 116, 219, 22, 113, 89, 187, 232, 198, 53, 146, 112, 119, 209, 64, 79, 236, 179]

tree = 0

for day in range(len(waterings)):
    watering_amount = waterings[day]

    if day == 0:
        then_date = "29/05/2020-20:00:00"
        seed_then = datetime.datetime.strptime(then_date, "%d/%m/%Y-%H:%M:%S").replace(tzinfo=datetime.timezone.utc).timestamp()
    else:
        then_date = (datetime.datetime.strptime(then_date, "%d/%m/%Y-%H:%M:%S")+datetime.timedelta(days=1)).strftime("%d/%m/%Y-%H:%M:%S")
        seed_then = datetime.datetime.strptime(then_date, "%d/%m/%Y-%H:%M:%S").replace(tzinfo=datetime.timezone.utc).timestamp()

    print(f"day {day} seed: {int(seed_then)}")
    print(int(seed_then)^watering_amount)
    #libc.srand(int(seed_then))
    #for _ in range(watering_amount):
    #    tree += libc.rand()
    #    print(tree)
    #print("===")

#print(tree)
