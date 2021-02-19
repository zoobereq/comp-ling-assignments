#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:54:03 2019

@author: zub
"""
import re

corpus = '''In the US, some phone numbers are reserved for fictitious purposes.
For instance, 555-0198 and 1-206-5555-0100 are example fictitious numbers.
There are similar ranges of numbers in the UK, Ireland, and Australia.
In the UK, 044-113-496-1234 is a fictitious number in the Leeds area.
In Ireland, the number 353-020-913-1234 is fictitious.
And in Australia, 061-900-654-321 is a fictitious toll-free number.
911 is a joke.'''

corpus2 = '''In the US, some phone numbers are reserved for fictitious purposes.
For instance, 000-0000 and 0-000-0000-0000 are example fictitious numbers.
There are similar ranges of numbers in the UK, Ireland, and Australia.
In the UK, 000-000-000-0000 is a fictitious number in the Leeds area.
In Ireland, the number 000-000-000-0000 is fictitious.
And in Australia, 000-000-000-000 is a fictitious toll-free number.
911 is a joke.'''


def exercise2():
    corpus1 = re.sub(r'\d{3}-\d{4}', '000-0000', corpus)
    corpus1 = re.sub(r'\d-\d{3}-\d{4}-\d{4}', '0-000-0000-0000', corpus1)
    corpus1 = re.sub(r'\d{3}-\d{3}-\d{3}-\d{4}', '000-000-000-0000', corpus1)
    corpus1 = re.sub(r'\d{3}-\d{3}-\d{3}-\d{3}', '000-000-000-000', corpus1)
    print(corpus1)
    return corpus1


def test():
    assert exercise2() == corpus2

test()
    
    

