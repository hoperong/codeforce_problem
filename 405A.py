#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
input_l = input().split(' ')
list_l = []
for i in input_l:
    list_l.append(int(i))
for i in range(len(list_l) - 1):
    for j in range(i + 1, len(list_l)):
        if list_l[i] > list_l[j]:
            list_l[i], list_l[j] = list_l[j], list_l[i]
s = ''
for i in range(len(list_l)):
    s += '{} '.format(list_l[i])
print(s.strip())F