#!/usr/bin/env python
# coding=utf-8

input_s = input()
isUpper = True
result = ''
for i in range(len(input_s)):
    result += input_s[i].upper() if isUpper else input_s[i]
    isUpper = input_s[i] == ' '
print(result)