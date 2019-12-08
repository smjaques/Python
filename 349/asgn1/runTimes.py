#!/usr/bin/env python3
import os

for i in range(5000,10000,10):
    os.system("python3 longList.py " + str(i))
    os.system("TIMEFORMAT=%R")
    time = os.system("time java SortsRunner list.txt")
    f = open("selection.txt", "a+")
    f.write(str(time))
    if i == 5020:
        break

