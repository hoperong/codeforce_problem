#!/usr/bin/env python
# coding=utf-8

input_s = input().split('+')
one = 0
two = 0
three = 0
result = ''
for i in input_s:
    if i == '1':
        one += 1
    elif i == '2':
        two += 1
    elif i == '3':
        three += 1
for i in range(one):
    result += '+1'
for i in range(two):
    result += '+2'
for i in range(three):
    result += '+3'
print(result[1:])