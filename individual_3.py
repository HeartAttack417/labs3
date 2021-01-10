#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# . Найти все трехзначные натуральные числа, сумма цифр которых равна их произведению.

if __name__ == '__main__':
    item = 100
    while item < 1000:
        if (item / 100 + (item / 10) % 10 + item % 10) == ((item / 100) * (item / 10 % 10) * (item % 10)):
            print(item)
