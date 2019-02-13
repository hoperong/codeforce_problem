#!/usr/bin/env python
# coding=utf-8

input_s = int(input())
word_list = []
for i in range(32):
    word_list.append({})
result_list = []
for i in range(input_s):
    input_l = input()
    state = False
    for (word_key, word_num) in word_list[len(input_l) - 1].items():
        if word_key == input_l:
            word_list[len(input_l) - 1][word_key] += 1
            result_list.append('{}{}'.format(
                input_l, word_list[len(input_l) - 1][word_key]))
            state = True
            break
    if not state:
        word_list[len(input_l) - 1][input_l] = 0
        result_list.append('OK')
for result in result_list:
    print(result)
