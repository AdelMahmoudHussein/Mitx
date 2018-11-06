# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 23:32:59 2018

@author: Adel13
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    out = ()
    for i in range(1,len(aTup)+1):
        if i%2 ==1 :
            out = out + (aTup[i-1],)
    return out    

def oddTuples2(aTup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    out = ()
    for i in range(len(aTup)):
        if i%2 ==0 :
            out = out + (aTup[i],)
    return out

# Test: Output: (4, 0, 15)
print(oddTuples((4, 18, 0, 8, 15, 13)))
# Test: Output: (4, 0, 15)
print(oddTuples2((4, 18, 0, 8, 15, 13)))