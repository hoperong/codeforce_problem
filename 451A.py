#!/usr/bin/env python
# coding=utf-8

input_s = input().split(' ')
a = int(input_s[0])
b = int(input_s[1])
c = min(a, b)
if c % 2 == 1:
    print('Akshat')
else:
    print('Malvika')