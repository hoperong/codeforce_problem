#!/usr/bin/env python
# coding=utf-8

s = input()
t = 'hello'
t_i = 0
for i in range(len(s)):
    if t_i >= 5:
        break
    if s[i] == t[t_i]:
        t_i += 1
if t_i >= 5:
    print('YES')
else:
    print('NO')