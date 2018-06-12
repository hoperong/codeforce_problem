#!/usr/bin/env python
# coding=utf-8

x = 0
y = 0
for i in range(5):
    list_l = input().split(' ')
    for j in range(5):
        if list_l[j] == '1':
            x = i
            y = j
mount = abs(x - 2) + abs(y - 2)
print(mount)