#!/usr/bin/env python
# coding=utf-8

import math

input_s = input()
list_v = input_s.split(' ')
n = int(list_v[0])
m = int(list_v[1])
a = int(list_v[2])
s = math.ceil(n / a) * math.ceil(m / a)
print(s)