# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 06:37:40 2018

@author: Adel13
"""

def isPalindrom(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s :
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans
    
    def isPal(s):
        if len(s) <2:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))
