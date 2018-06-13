#!/usr/bin/env python
# coding=utf-8

s = input()
has_lower = False
for i in range(len(s)):
    if s[i] == 'H' or s[i] == 'Q' or s[i] == '9':
        has_lower = True
        break
if has_lower:
    print('YES')
else:
    print('NO')
