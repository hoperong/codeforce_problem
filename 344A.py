#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
before = ''
mount = 0
for i in range(input_s):
    input_l = input()
    if before != input_l:
        before = input_l
        mount += 1
print(mount)