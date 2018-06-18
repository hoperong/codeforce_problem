#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
while 1 == 1:
    input_s += 1
    s = set(list(str(input_s)))
    if len(str(input_s)) == len(s):
        print(input_s)
        break
