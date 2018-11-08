# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 02:32:40 2018

@author: Adel13
"""

def getRatios(L1,L2):
    ratios = []
    for i in range(len(L1)):
        try:
            ratios.append(L1[i]/float(L2[i]))
        except ZeroDivisionError :
            ratios.append(float('NaN'))
        except :
            raise ValueError('get_ratios called with bad arg')
    
    return ratios

L1 = [3,5,7,9,0,1]
L2 = [2,7,0,-3,2,2]

print(getRatios(L1,L2))