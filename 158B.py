#!/usr/bin/env python
# coding=utf-8
import math

input_s = input()
list_l = input().split(' ')
mount = [0, 0, 0, 0]
for l in list_l:
    mount[int(l) - 1] += 1
sum = 0
# 4
sum += mount[3]
# 3
sum += mount[2]
if mount[2] >= mount[0]:
    mount[0] = 0
else:
    mount[0] -= mount[2]
# 1+2
if mount[1] * 2 >= mount[0]:
    sum += math.ceil(mount[0] / 2) + math.ceil(
        (mount[1] - math.ceil(mount[0] / 2)) / 2)
else:
    sum += mount[1] + math.ceil((mount[0] - 2 * mount[1]) / 4)

print(sum)