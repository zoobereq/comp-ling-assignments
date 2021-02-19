#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:38:01 2019

@author: zub
"""

class Rectangle:
    #defines the variables
    def __init__(self, x0, y0, x1, y1, x, y):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x = x
        self.y = y
    #defines the method that calculates the area
    def area(self):
        return abs((self.x1 - self.x0) * (self.y1 - self.y0))
    #defines the method that checks if the point is within the rectangle
    def contains(self):
        if (self.x >= self.x0 and self.x <= self.x1 and self.y >= self.y0 and self.y <= self.y1):
            return("The point is inside the rectangle")
        else:
            return("The point is outside the rectangle")

#defines the function that runs an instance of the class 'Rectangle'
def main():
    rec1 = Rectangle(0, 0, 2, 4, 1, 3) #creates an instance of a class and stores it in rec1
    print(f"The area of this rectangle is {rec1.area()}") #prints a message including the values stored in rec1, passed through the 'area' method
    print(rec1.contains()) #prints a message including same values, this time passed through the 'contains' method
    assert rec1.area() == 8 #having definded the variable that is an instance of the class, you use the method as the attribute
    
main() #calls the function 'main'
    
'''
Kyle's solution

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
    
 
# Sample assertion tests.
r = Rectangle(-2, 0, 3, 4)
assert r.area() == 20
assert not r.contains(-2, 0)
assert r.contains(0, 1)
'''