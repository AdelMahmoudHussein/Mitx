# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:17:27 2018

@author: Adel13
"""

"""
    Problem Set 2
    Problem 2 - minimum fixed monthly payment needed 
    in order pay off a credit card balance within 12 months
"""

balance = 3329
annualInterestRate = 0.2

ub = balance
r = annualInterestRate
# mr is monthly Interest Rate
mr = r/12
# fixed is minimum fixed monthly payment needed starts with -10
fixed = -10

# while loop stop when unpaid balance <= 0
while ub >0:
    ub = balance
    r = annualInterestRate
    fixed +=10
    for i in range(1,13):
        ub = ub - fixed
        ub = ub + ub*mr

print('Lowest Payment:', fixed)    
   