#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
result_l = [0, 0, 0]
for i in range(input_s):
    input_l = input().split(' ')
    result_l[0] += int(input_l[0])
    result_l[1] += int(input_l[1])
    result_l[2] += int(input_l[2])
is_ok = True
for i in result_l:
    if i != 0:
        is_ok = False
        break
if is_ok:
    print('YES')
else:
    print('NO')
