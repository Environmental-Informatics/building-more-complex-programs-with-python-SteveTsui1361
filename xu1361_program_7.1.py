#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:45:28 2020

@author: xu1361
"""
import math
# my sprt function
def mysqrt(a):
    x = a / 2
    while True:
        # another method
        # epsilon = 1e-7
        # if abs(y - x) < epsilon:
        y = (x + (a / x)) / 2
        if y == x:
            return y
            break
        x = y
# output the table comparing mysqrt and math.sqrt
def test_square_root(num_col):
    for a in range(1, num_col):
        col1 = float(a)
        col2 = mysqrt(a)
        col3 = math.sqrt(a)
        col4 = abs(mysqrt(a) - math.sqrt(a))
        print(col1, '{:<13f}'.format(col2),'{:<13f}'.format(col3), col4)
        
# header of the table
print('a   mysqrt(a)     math.sqrt(a)  diff')
print('-   ---------     ------------  ----')
test_square_root(10)
