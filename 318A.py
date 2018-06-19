#!/usr/bin/env python
# coding=utf-8

input_s = input().split(' ')
a = int(input_s[0])
b = int(input_s[1])
half_a = a // 2 + a % 2
if b <= half_a:
    print(b * 2 - 1)
else:
    print((b - half_a) * 2)
