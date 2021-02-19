#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:18:14 2019

@author: zub
"""
import re

def exercise1():
    with open('wordlist_empty.txt') as fin, open('wordlist.txt', 'w') as fout:
        for line in fin:
            if not line.strip():  #if the line is not, i.e. if it's empty
                continue  #skip the empty line
            fout.write(line) #if line non-empty, write it to fout
    
    path = 'wordlist.txt'
    
    with open(path, 'r') as source:  #opens the file and stores it in 'source'
        lines = source.readlines()  #reads the whole file line by line, and stores the contents as a list in 'lines'.  The file is small enough for .readlines.
        
        double_letter_word = re.compile(r'\w*(\w)\1\w*')  #creates a regex object that we'll later use for searching. This is the preferred practice.
        double_letter_list = []  #creates an empty list to store the double-letter words
        
        for word in lines: #starts the loop
            match = double_letter_word.search(word) #goes through the 'lines' list and searches for 'word's' that contain 'double_letter's
            if match: #if it finds a matching 'word'
                double_letter_list.append(match.group()) # .group method returns the 'match'ed string and appends it to the list
        
        print(double_letter_list) #prints the list
        
            
exercise1() #calls the function


'''
Notes on regEx used:
    r'regEx' makes raw string which makes the regular expression more readable
    \w* matches zero or more word characters (here, letters)
    (\w)a group of zero or more word characters
    \1 this repeats one preceding character, i.e. the (\w)
    \w* zero or more word characters

zero or more letters, then a letter that's repeated once, followed by zero or more letters
    
'''
