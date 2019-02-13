#!/usr/bin/env python
# coding=utf-8

input_s = input()[1:][:-1]
list_s = list([x.strip() for x in input_s.split(',') if len(x.strip()) > 0])
print(len(list(set(list_s))))