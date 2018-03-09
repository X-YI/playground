from mpmath import *
mp.pretty = True
import numpy as np
import random as rd

file = open("data.txt", "a")

for i in range(0, 10000):
    co = [(rd.randint(0, 999999) * power(10, rd.randint(-4, 4))) / 10000 for i in range(3)]
    try:
        a = co[0]
        b = co[1]
        c = co[2]
        if b * b - 4 * a * c < 0:
            continue
        if i % 1000 == 0:
            print(i)
        mp.dps = 7
        # print(co)
        x11 = (-b + sqrt(b * b - 4 * a * c)) / 2 / a
        x12 = (-b - sqrt(b * b - 4 * a * c)) / 2 / a
        # print(x11)
        # print(x12)
        mp.dps = 25
        # print(co)
        x21 = (-b + sqrt(b * b - 4 * a * c)) / 2 / a
        x22 = (-b - sqrt(b * b - 4 * a * c)) / 2 / a
        # print(x21)
        # print(x22)
        re1 = (abs(x22 - x12) / x22)
        re2 = (abs(x21 - x11) / x21)
        # print(re1)
        # print(re2)
        file.write("{}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(a, b, c, re1, re2, x11, x12, x21, x22))
        
    except Exception as e:
        continue
        # print(str(e))

file.close()
