#!/usr/bin/env python
# coding=utf-8

luck_list = [4, 7, 44, 77, 47, 74, 444, 447, 474, 477, 744, 747, 774, 777]
mount = int(input())
is_ok = False
for i in range(len(luck_list)):
    if mount % luck_list[i] == 0:
        is_ok = True
if is_ok:
    print('YES')
else:
    print('NO')
