# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 02:54:51 2018

@author: Adel13
"""

# 1st way by using try & except
def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('No Grades Data')
        return 0.0

# 2nd way by using assertion
def average(grades):
    assert len(grades) !=0, 'An Empty Grades'
    return sum(grades)/len(grades)


        
a = [1,2,3,4,5,6]
b = []
print('avg a =',avg(a))
print('avg b =',avg(b))
print('average a =',average(a))
print('average b =',average(b))
