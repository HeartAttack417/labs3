#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вводится число карандашей . Вывести фразу Я купил N карандашей , согласовав
# слово "карандаш" с числом .

if __name__ == '__main__':

    N = int(input("Введите кличество карандашей "))
    if N % 10 == 1 and not N == 11:
        print("Я купил {} карандаш".format(N))

    elif (N % 10 == 2 and N != 12)  or (N % 10 == 3 and N != 13) or (N % 10 == 4 and N != 14):
        print("Я купил {} карандаша".format(N))

    else:
        print("Я купил {} карандашей".format(N))
