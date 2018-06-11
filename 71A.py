#!/usr/bin/env python
# coding=utf-8

num = input()
item_list = []
for i in range(int(num)):
    item = input()
    item_list.append(item)
for item in item_list:
    if len(item) > 10:
        print('{}{}{}'.format(item[0], len(item) - 2, item[-1]))
    else:
        print(item)