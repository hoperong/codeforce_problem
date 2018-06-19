#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
input_l = input().split(' ')
list_l = []
for i in input_l:
    list_l.append(int(i))
for i in range(input_s):
    for j in range(i + 1, input_s):
        if list_l[i] < list_l[j]:
            list_l[i], list_l[j] = list_l[j], list_l[i]
is_ok = False
for i in range(1, input_s):
    a = sum(list_l[0:i])
    b = sum(list_l[i:input_s])
    if a > b:
        print(i)
        is_ok = True
        break
if not is_ok:
    print(input_s)
