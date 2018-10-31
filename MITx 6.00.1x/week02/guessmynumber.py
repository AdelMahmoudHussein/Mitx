# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:57:56 2018

@author: Adel13
"""

high = 100
low = 0
guess = (high+low)//2
print('Please think of a number between 0 and 100!')

while True:
    print('Is your secret number',guess,'?')
    r = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if r == 'h':
        high = guess
    elif r == 'l':
        low = guess
    elif r == 'c':
        print('Game over. Your secret number was:',guess)
        break
    else:
        print('Sorry, I did not understand your input.')
        
    guess = (high+low)//2    