#!/usr/bin/env python
# coding=utf-8

input_s = input()
input_l = input().split(' ')
list_l = [0] * len(input_l)
for (index, l) in enumerate(input_l):
    list_l[int(l) - 1] = index + 1
s = ''
for l in list_l:
    s += '{} '.format(l)
print(s.strip())
