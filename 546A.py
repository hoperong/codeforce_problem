#!/usr/bin/env python
# coding=utf-8

input_s = input().split(' ')
k = int(input_s[0])
n = int(input_s[1])
w = int(input_s[2])
m = 0
if w % 2 == 0:
    m = (w + 1) * w / 2
else:
    m = w * (w - 1) / 2 + w
mk_n = m * k - n
if mk_n >= 0:
    print('%d' % mk_n)
else:
    print(0)
