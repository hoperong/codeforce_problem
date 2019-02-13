#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
list_l1 = [0] * 100
list_l2 = [0] * 100
for i in range(input_s):
    input_l = input().split(' ')
    list_l1[int(input_l[0]) - 1] += 1
    list_l2[int(input_l[1]) - 1] += 1
mount = 0
for i in range(100):
    mount += list_l1[i] * list_l2[i]
print(mount)