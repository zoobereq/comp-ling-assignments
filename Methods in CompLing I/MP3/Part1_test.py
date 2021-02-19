#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:10:54 2019

@author: zub
"""

class Rectangle:
    
    def __init__(self, x0: float, y0: float, x1: float, y1: float):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    
    def area(self) -> float:
        width = self.x1 - self.x0
        height = self.y1 - self.y0
        return width * height
    
    def contains(self, x: float, y: float) -> bool:
        # If right on the line, this returns False.
        return (self.x0 < x and x < self.x1 and
                self.y0 < y and y < self.y1)

r = Rectangle(0, 0, 2, 5)
print(r.area())
assert not r.contains(1,2)

''' 
# Sample assertion tests.
r = Rectangle(-2, 0, 3, 4)
assert r.area() == 20
assert not r.contains(-2, 0)
assert r.contains(0, 1)
'''