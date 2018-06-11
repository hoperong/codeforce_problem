#!/usr/bin/env python
# coding=utf-8

input_s = input()
input_list = input_s.split(' ')
mount = int(input_list[0])
pass_th = int(input_list[1])
input_result = input()
input_result_list = input_result.split(' ')
if int(input_result_list[pass_th - 1]) <= 0:
    x = 1
    while pass_th - x > 0:
        if int(input_result_list[pass_th - x - 1]) > 0:
            break
        x += 1
    print(pass_th - x)
else:
    x = 0
    while len(input_result_list) > pass_th + x:
        if int(input_result_list[pass_th + x - 1]) != int(
                input_result_list[pass_th + x]):
            break
        x += 1
    print(pass_th + x)
