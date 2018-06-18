#!/usr/bin/env python
# coding=utf-8

input_s = input().split(' ')
input_l = input()
t = int(input_s[1])
i = 0
while i < t:
    i += 1
    j = 0
    input_l_2 = ''
    while j < len(input_l):
        if j == len(input_l) - 1:
            input_l_2 += input_l[j]
            j += 1
        else:
            if input_l[j] == 'G':
                input_l_2 += 'G'
                j += 1
            else:
                if input_l[j + 1] == 'G':
                    input_l_2 += 'GB'
                    j += 2
                else:
                    input_l_2 += 'B'
                    j += 1
    input_l = input_l_2
print(input_l)
