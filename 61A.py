#!/usr/bin/env python
# coding=utf-8

input_s = input()
input_l = input()
m = ''
for i in range(len(input_s)):
    if input_s[i] == input_l[i]:
        m += '0'
    else:
        m += '1'
print(m)