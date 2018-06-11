#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
s = 0
for i in range(input_s):
    item_s = input()
    if item_s == '++X' or item_s == 'X++':
        s += 1
    elif item_s == '--X' or item_s == 'X--':
        s -= 1
print(s)