#!/usr/bin/env python
# coding=utf-8

input_s = input().split(' ')
s_m = int(input_s[0])
input_l = input().split(' ')
list_l = []
for l in input_l:
    list_l.append(int(l))
for i in range(len(list_l)):
    for j in range(i + 1, len(list_l)):
        if list_l[i] > list_l[j]:
            list_l[i], list_l[j] = list_l[j], list_l[i]
min_AB = 9999
for i in range(len(list_l) - s_m + 1):
    min_AB = min(list_l[i + s_m - 1] - list_l[i], min_AB)
print(min_AB)
