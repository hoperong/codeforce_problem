#!/usr/bin/env python
# coding=utf-8

s = input()
has_lower = False
for i in range(1, len(s)):
    if ord(s[i]) >= 97 and ord(s[i]) <= 122:
        has_lower = True
        break
if has_lower:
    print(s)
else:
    if ord(s[0]) >= 97 and ord(s[0]) <= 122:
        print('{}{}'.format(s[0].upper(), s[1:].lower()))
    else:
        print('{}'.format(s.lower()))
