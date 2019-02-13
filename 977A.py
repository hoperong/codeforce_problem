#!/usr/bin/env python
# coding=utf-8

input_s = input().split(' ')
n = int(input_s[0])
k = int(input_s[1])
for i in range(k):
    if n % 10 != 0:
        n -= 1
    else:
        n = n // 10
print(n)
