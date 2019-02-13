#!/usr/bin/env python
# coding=utf-8

input_s = input()
upper = 0
lower = 0
for i in range(len(input_s)):
    if ord(input_s[i]) >= ord('A') and ord(input_s[i]) <= ord('Z'):
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(input_s.upper())
else:
    print(input_s.lower())