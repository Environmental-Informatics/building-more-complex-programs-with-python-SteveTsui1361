#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:41:38 2020

@author: xu1361
"""
# find the greatest common divisor of parameters a and b
def gcd(a, b):
    if b ==0:
        return a
    return gcd(b, a % b)

ab = input().split()
a = int(ab[0])
b = int(ab[1])

results = gcd(a ,b)
print(results)12
