# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 07:20:39 2018

@author: Adel13
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    
# Base case
    if len(aStr) == 0:
        return False
# Base case
    if len(aStr) == 1:
        return char == aStr

    midLen = len(aStr)//2
    midChar = aStr[midLen]

# Base case
    if char == midChar :
        return True
    
    # Recursive case

    if char > midChar:
        return isIn(char, aStr[midLen+1:])
        
    if char < midChar :
        return isIn(char, aStr[:midLen])