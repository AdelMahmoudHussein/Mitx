# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:41:14 2018

@author: Adel13
"""

x = int(input('Enter a number : '))
if x < 0:
    x_neg = True
    r = abs(x)
else:
    x_neg = False
    r = x
binary = ''
while r > 0 :
    binary = str(r%2) + binary
    r = r//2

if x_neg:
    binary = '-'+binary
print('Binary number of ', str(x) , 'is :', binary)    