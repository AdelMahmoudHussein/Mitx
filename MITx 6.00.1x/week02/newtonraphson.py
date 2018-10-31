# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 23:15:52 2018

@author: Adel13
"""

epsilon = 0.01
y = 597320567810
guess = y/2.0
numGuesses = 0

while abs((guess**2)-y) >= epsilon :
    numGuesses += 1
    guess = guess - (((guess**2)-y)/(2*guess))
    
print('Num Guesses is '+ str(numGuesses))
print('Squar root of '+ str(y) + ' is about ' + str(guess))    