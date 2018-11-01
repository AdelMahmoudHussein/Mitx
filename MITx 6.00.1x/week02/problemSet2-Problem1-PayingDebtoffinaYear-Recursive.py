# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:00:43 2018

@author: Adel13
"""
"""
    Problem Set 2
    Problem 1 - Paying Debt off in a Year (Recursively)
"""
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def evaluate_year(bal, interest, pay, months):
    if months <= 0 :
        return bal 
    else :
        # unpaid balance = ((bal * (1 - pay)) * (1 + interest))
        return round(evaluate_year(((bal * (1 - pay)) * (1 + interest)), interest, pay, months-1),2)

print('Remaining balance:', evaluate_year(balance, annualInterestRate/12, monthlyPaymentRate, 12))