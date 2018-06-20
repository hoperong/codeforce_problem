#/usr/bin/env python
# coding=utf-8

input_s = int(input())
mount = input_s // 5
if input_s % 5 > 0:
    print(mount + 1)
else:
    print(mount)
