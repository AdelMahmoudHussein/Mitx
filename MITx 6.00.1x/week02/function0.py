# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 09:02:26 2018

@author: Adel13
"""

x = 12
def g(x):
    print(x)    
    x = x + 1
    print(x)
    def h(y):
        print(x)
        return x + y
    print(x)    
    return h(6)
print(g(x))
