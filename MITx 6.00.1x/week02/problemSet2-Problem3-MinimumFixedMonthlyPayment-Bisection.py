# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 12:03:05 2018

@author: Adel13
"""

"""
    Problem Set 2
    Problem 3 - minimum fixed monthly payment needed 
    in order pay off a credit card balance within 12 months
    with Bisection algorithm
"""
#    test case
balance = 999999
annualInterestRate = 0.18
#    answer must be 90325.03

ub = balance
r = annualInterestRate
# mr is monthly Interest Rate
mr = r/12
# fixed is minimum fixed monthly payment needed starts with -10
fixed = 0
low = balance/12
high = (balance*(1+r))/12

# while loop stop when unpaid balance <= 0
while abs(ub - 0) > 0.01:
    ub = balance
    r = annualInterestRate
    fixed = (low + high)/2
    for i in range(1,13):
        ub = ub - fixed
        ub = ub + ub*mr
 
    if ub > 0 :
        low = fixed
    if ub < 0 :
        high = fixed

print('Lowest Payment:', round(fixed,2))