#!/usr/bin/env python
# coding=utf-8

input_s = input()
input_l = input()
mount = 0
pre = ''
for i in input_l:
    if i == pre:
        mount += 1
    else:
        pre = i
print(mount)