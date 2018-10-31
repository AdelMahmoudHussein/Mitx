# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:35:38 2018

@author: Adel13
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp >= 0:
        if exp == 0 :
            return 1
        else:
            return base*recurPower(base,exp-1)
    else:
        print('Error ; exp must be more than 0')