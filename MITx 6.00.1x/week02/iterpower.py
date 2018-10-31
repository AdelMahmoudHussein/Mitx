# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:33:16 2018

@author: Adel13
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    r = 1
    while exp>0:
        r *= base
        exp -= 1
    return r 