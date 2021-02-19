#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:42:21 2019

@author: zub
"""

"""
def fibonacci(number: int) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)
    
print(fibonacci(100))

The above was the first attempt, which worked oonlhy for the first handful of numbers, and didn't finish computing the 100th position.

"""

def fibonacci(number: int) -> int:
    first_number_in_sequence = 0
    second_number_in_sequence = 1
    if number <= 0:
        return("Enter a positive integer.")
    elif number == 1:
        return first_number_in_sequence
    elif number == 2:
        return second_number_in_sequence
    for number in range(2, number+1):
        next_number_in_sequence = first_number_in_sequence + second_number_in_sequence
        first_number_in_sequence = second_number_in_sequence
        second_number_in_sequence = next_number_in_sequence
    return(next_number_in_sequence)
    
print(fibonacci(100))

assert fibonacci(1) == 0
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(100) == 354224848179261915075
