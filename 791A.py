#!/usr/bin/env python
# coding=utf-8

import math

input_l = input().split(' ')
a = int(input_l[0])
b = int(input_l[1])
i = 0
while a / b <= math.pow(2 / 3, i):
    i += 1
print(i)
