#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# . Найти все трехзначные натуральные числа, сумма цифр которых равна их произведению.

if __name__ == '__main__':
    item = 100
    while item < 1000:
        num1 = int(item / 100)
        num2 = int((item / 10) % 10)
        num3 = int(item % 10)
        if num1 + num2 + num3 == num1 * num2 * num3:
            print(item)
        item += 1
