#!/usr/bin/env python
# coding=utf-8

input_s = input()
mount = 0
for i in range(len(input_s)):
    if input_s[i] == '4' or input_s[i] == '7':
        mount += 1
if mount == 4 or mount == 7:
    print('YES')
else:
    print('NO')