#!/usr/bin/env python
# coding=utf-8

s = int(input())
now_mount = 0
max_mount = 0
for i in range(s):
    list_l = input().split(' ')
    stop_l = int(list_l[0])
    enter_l = int(list_l[1])
    now_mount = now_mount - stop_l + enter_l
    max_mount = max(now_mount, max_mount)
print(max_mount)