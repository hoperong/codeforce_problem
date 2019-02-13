#!/usr/bin/env python
# coding=utf-8

input_s = input()
input_l = input()
a = 0
d = 0
for i in range(len(input_l)):
    if input_l[i] == 'A':
        a += 1
    else:
        d += 1
if a > d:
    print('Anton')
elif a < d:
    print('Danik')
else:
    print('Friendship')