# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 05:05:01 2018

@author: Adel13
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a > b:
        gcd = b
    else:    
        gcd = a
        
    while a % gcd != 0 or b % gcd != 0 :
        gcd -= 1
    
    return gcd    

print(gcdIter(1000000, 20))