#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
input_l = input().split(' ')
number_max = -1
number_min = 999999
s = 0
for l in input_l:
    ll = int(l)
    if ll > number_max:
        s += (1 if number_max != -1 else 0)
        number_max = ll
    if ll < number_min:
        s += (1 if number_min != 999999 else 0)
        number_min = ll
print(s)
