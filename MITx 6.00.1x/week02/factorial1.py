# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:21:44 2018

@author: Adel13
"""

def f(n):
    if n ==1 :
        return 1
    else:
        return (n*f(n-1))

print(f(9))    