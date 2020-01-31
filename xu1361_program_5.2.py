#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:34:34 2020
This code is used to check the Fermat's function
@author: xu1361
"""
# function for checking Fermat's theorem
def check_fermat(a , b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        return 'Holy smokes, Fermat was wrong!'
    else:
        return "No, that doesn't work."
    
abcn = input().split()
a = int(abcn[0])
b = int(abcn[1])
c = int(abcn[2])
n = int(abcn[3])
results = check_fermat(a, b, c, n)
print(results)
