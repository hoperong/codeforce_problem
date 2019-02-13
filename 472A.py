#!/usr/bin/env python
# coding=utf-8


def is_primes(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    return is_prime


input_s = int(input())
for i in range(input_s // 2, 3, -1):
    if not is_primes(i) and not is_primes(input_s - i):
        print('{} {}'.format(i, input_s - i))
        break