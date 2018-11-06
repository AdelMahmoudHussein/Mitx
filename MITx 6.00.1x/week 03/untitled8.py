# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 13:15:48 2018

@author: Adel13
"""
import pyqrcode

def createQr(text,name):
    
    qr = pyqrcode.create(str(text))
    qr.png(str(name)+'.png',scale=7)
    

for i in range(1,11):
    createQr(i,i)
    print(i,'Done')
