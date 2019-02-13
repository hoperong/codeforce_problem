#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
s = 0
b = 0
i = 0
while s <= input_s:
    i += 1
    b += i
    s += b
print(i - 1)
