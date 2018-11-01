# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 09:36:02 2018

@author: Adel13
"""

import math

def polysum(n,s):

    area = (0.25*n*s**2)/(math.tan(math.pi/n)) 
    perimeter = n*s
    
    return round(area+perimeter**2,4)


