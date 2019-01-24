#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def SimpleInterest(PV, r, t):
    ## Before input r is converted to decimal from percentage ##
    ## t is the number of years ##
    FV = PV*((1 + r)**t)
    return FV

def Compoundinterest(PV, r, n, t):
    ## n is the number of times compounded ##
    FV = PV*((1 + (r/n))**nt)
    return FV

def ContinouoslyCompounded(PV, r, n):
    FV = PV*math.exp(r*n)
    return FV

def EffectiveInterestRate(r, m):
    ## r is the nominal interest rate ##
    ## m is the number of times compounded per year ##
    
    EIR = ((1 + (r/m))**m) - 1
    
    return EIR

def Annuity(c, y, n):
    ## c is the fixed payment received each time ##
    ## y is the YTM (in decimal) ##
    ## n is the number of payments ##
    
    PV = 0
    for i in range(1, n + 1):
        PV = PV + c/((1 + y)**i) 
        
    return PV

def Perpetuity(c, y):
    ## Calculation of price of the perpetuity ##
    PV = c/y
    return PV

