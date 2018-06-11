#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
s = 0
for i in range(input_s):
    item_s = input().split(' ')
    s_item = 0
    for item in item_s:
        s_item += int(item)
    if s_item >= 2:
s += 1
print(s)