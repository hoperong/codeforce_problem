#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
input_p = input().split(' ')[1:]
input_q = input().split(' ')[1:]
a = []
for i in input_p:
    a.append(i)
for i in input_q:
    a.append(i)
b = list(set(a))
if len(b) == input_s:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
