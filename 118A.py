#!/usr/bin/env python
# coding=utf-8

vowels_list = ['A', 'a', 'O', 'o', 'Y', 'y', 'E', 'e', 'U', 'u', 'I', 'i']
result = ''
input_s = input()
for i in range(len(input_s)):
    if input_s[i] not in vowels_list:
        result += '.{}'.format(input_s[i].lower())
print(result)