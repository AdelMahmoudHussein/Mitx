# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 05:14:12 2018

@author: Adel13
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0 :
        gcd = a
        return gcd
    else:
        return gcdRecur(b,a%b)
    
print(gcdRecur(1071,462))
print(gcdRecur(462,1071))