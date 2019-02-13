#!/usr/bin/env python
# coding=utf-8

input_s = input()
input_l = input().split(' ')
max_mount = -1
max_index = -1
min_mount = 999
min_index = -1
for i in range(len(input_l)):
    if int(input_l[i]) > max_mount:
        max_mount = int(input_l[i])
        max_index = i
    if int(input_l[i]) <= min_mount:
        min_mount = int(input_l[i])
        min_index = i
if max_index <= min_index:
    print(max_index + len(input_l) - 1 - min_index)
else:
    print(max_index + len(input_l) - 1 - min_index - 1)