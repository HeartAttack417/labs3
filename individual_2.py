#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Симметричны ли точки M1(x1,y1) и M1(x2,y2) относительно оси О X или относительно оси
# О Y ?

import math

if __name__ == '__main__':
    print(22%23+1)
    x1 = int(input("Введите координату x1 первой точки "))
    y1 = int(input("Введите координату y1 первой точки "))
    x2 = int(input("Введите координату x2 второй точки "))
    y2 = int(input("Введите координату y2 второй точки "))

    if abs(x1) == abs(x2) and y1 == y2:
        print("Эти точки симметричны относительно оси OY")

    elif abs(y1) == abs(y2) and x1 == x2:
        print("Эти точки симметричны относительно оси OX")

    else:
        print("Они не симметричны")