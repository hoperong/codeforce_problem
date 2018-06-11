#!/usr/bin/env python
# coding=utf-8

input_a = input().lower()
input_b = input().lower()
result = 0
for i in range(len(input_a)):
    if ord(input_a[i]) > ord(input_b[i]):
        result = 1
        break
    elif ord(input_a[i]) < ord(input_b[i]):
        result = -1
        break
print(result)