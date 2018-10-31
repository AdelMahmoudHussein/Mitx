# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 03:57:04 2018

@author: Adel13
"""
countMoves = 0

def PrintMove(fr,to):
    print('Move From '+ str(fr)+ ' to '+ str(to))
    global countMoves 
    countMoves +=1
    
def Towers(n, fr, to, spare):
    if n == 1:
        PrintMove(fr, to)
        
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

Towers(5, 'P1', 'P2', 'P3')
print('count Moves = '+ str(countMoves))    