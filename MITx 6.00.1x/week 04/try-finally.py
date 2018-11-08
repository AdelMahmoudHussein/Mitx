# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 02:47:30 2018

@author: Adel13
"""

f = None
try:
    f = open('test.txt')
except:
    print('Can not open a File')
else :
    print('good openning')
finally:
    if f is not None:
        f.close()    
