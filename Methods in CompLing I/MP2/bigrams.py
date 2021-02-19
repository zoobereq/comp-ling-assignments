#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Sun Oct 13 16:47:46 2019

@author: zub
'''

from typing import List # imports whatever needs to be imported

def bigrams_assignment(sequence: List[str]) -> List[List[str]]: # defines a function that will return a list of lists of strings #inception. The function takes a variable 'sequence'
    sequence = sequence.split(" ") # the variable sequence is defined.  It's a string that we first need to split into a list of strings. We split whenever there's a space.
    bigram = [ ] # defines the variable 'bigram' and assigns it an empty list
    for word_in_sequence in range(len(sequence)): # len of sequence tells us how many objects a sequence counts.  Since a sequence is a list of unigram strings, it sould be equal to the number of words in a sequence.  The range is from 0 to the number of words in a sequence
        if word_in_sequence == 0:  # refers to the first position in the sequence. The program starts with the first posistion, because for-loop 
            continue # For one-word sequences, don't bother.
        else: # If there are more words in the sequence, read below:
            bigram.append([sequence[word_in_sequence-1],sequence[word_in_sequence]]) #this builds bigrams.  
# It takes the original bigram variable, which is an empty list and appends two elements to it.  The first element is decremented by 1, the second element is the first.  We need to phrase it this way because computer starts counting with 0.
    return bigram #returns the above in a list of lists until it runs through the whole sequence, at which point it terminates

print(bigrams_assignment("It is important to understand the logic behind each assignment."))

print(bigrams_assignment(""))

print(bigrams_assignment("Hi"))

print(bigrams_assignment("Four score and seven years."))

print(bigrams_assignment("Claudia is about to eat her eggs."))


  
        