#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 14:11:38 2020
This code is used to draw flowers as mentioned in the Exercise(Think Python)
@author: xu1361
"""
# import necessary modules 
import turtle
import math
bob = turtle.Turtle()

# draw the circles
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
        
# draw flowers
def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

# draw flower
def flower(t, r, n, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)
        
# move flower
def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()
    
# draw three flowers
move(bob, -100)
flower(bob, 60, 7, 60)

move(bob, 100)
flower(bob, 40, 10, 80)

move(bob, 100)
flower(bob, 150, 20, 20)
turtle.mainloop()
