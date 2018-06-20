#!/usr/bin/env python
# coding=utf-8

input_s = input()
input_l = input().split(' ')
before = 0
max_mount = 1
now_mount = 0
for l in input_l:
    if int(l) >= before:
        now_mount += 1
        max_mount = max(now_mount, max_mount)
    else:
        now_mount = 1
    before = int(l)
print(max_mount)
