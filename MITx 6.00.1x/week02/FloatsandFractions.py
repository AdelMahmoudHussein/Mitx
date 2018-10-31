# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 22:22:17 2018

@author: Adel13
"""

x = float(input('Enter a decimal number between 0 and 1 : '))
p = 0
while ((2**p)*x) %1 != 0 :
    print('remainder = ', ((2**p)*x) - int(((2**p)*x)))
    p += 1

num = int((2**p)*x)

binary = ''

if num == 0:
    binary = '0'
while num > 0 :
    binary = str(num%2) + binary
    num = num//2

while (p-len(binary)) > 0:
    binary = '0'+binary
    
binary = binary[0:-p] + '.' + binary[-p:]    
print('The binary representation of the decimal '+ str(x) + ' is ' + binary)    
        