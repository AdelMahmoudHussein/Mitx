# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 06:26:19 2018

@author: Adel13
"""

def fib(n):
    if n ==0 or n ==1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)