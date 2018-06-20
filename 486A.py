#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
if input_s % 2 > 0:
    print(int(-(input_s // 2 + 1)))
else:
    print(int(input_s / 2))
