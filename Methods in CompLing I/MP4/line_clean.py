#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:02:22 2019

@author: zub
"""

#this script removes empty lines in a file

def fclean():  
    with open('wordlist_empty.txt') as fin, open('wordlist.txt', 'w') as fout:
        for line in fin:
            if not line.strip():  #if the line is not, i.e. if it's empty
                continue  #skip the empty line
            fout.write(line) #if line non-empty, write it to fout
            
fclean()