# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:16:17 2018

@author: Adel13
"""

"""
    Problem Set 2
    Problem 1 - Paying Debt off in a Year
"""

# define new function
def calcRemaningBalance(b,r,mp):
    
    """
        b- balance
        r- annualInterestRate
        mp-monthlyPaymentRate
        ub-unpaid balance
        mr-monthlyInterestRate
    """    
    # create variables
    ub = b
    r=r
    mp=mp
    mr=r/12
    
    # loop for 12 monthes
    for i in range(1,13):
        # paid monthly = unpaid balance * monthlyPaymentRate
        p = ub*mp
        # unpaid balance = unpaid balance - paid monthly
        ub = ub-p
        # unpaid balance = 
        # unpaid balance + monthlyInterestRate *unpaid balance 
        ub = ub + mr*ub
        # print Monthly Remaining balance round by 2 decimal
        print('Month:', i, 'Remaining balance:', round(ub,2))
    
    # print Remaining balance round by 2 decimal
    print('Remaining balance:', round(ub,2))    
