#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np


def FixedMortgage(P, r, n):
    ## Convert to Monthly ##
    ## n is the number of months ##
    ## P is the principal loan ##
    ## r is the annual interest rate (decimal) ##
    
    r = r/12
    if r != 0:
        FM = (r*P*((1 + r)**n))/(((1 + r)**n) - 1)
    else:
        FM = P/n
        
    return FM    

def AmountAtEachTime(P, r, n, t):
    
    ## To know how much is still the outstanding loan ## 
    ## t is the month desired to find the outstanding principal at that time ##
    
    if t >= n:
        return 0
    
    else:
        a = FixedMortgage(P, r, n)
        r = r/12
    
        A = ((1 + r)**t)*P - (((1 + r)**t) - 1)*(a/r)
        
        return A
            
    
    
def RatePerPeriod(i, n, p):
    ## i is the interest ##
    ## n is the number of compounding per year ##
    ## p is the number of payments per year ##
    r = ((1 + i/n)**(n/p)) - 1
    
    if n < p:
        print('Negative Ammortization with a Rate of Period of:')
        print(r)
    else:
        print(r)
        
def AdjustableRateMortgage(P, r):
    ## I will be assuming 5/1 ARM for 30 years of maturity. By definition of 5/1 ARM interest rate is random after 5 years ##
    ## and the interest rate ranges from (r - 000.2) to (r + 000.3) for each year. Interest rate is random each year as ##
    ## denominator of 5/1 is 1 ##
    
    lists = []
    
    for i in range(0, 60):
        k = AmountAtEachTime(P, r, 360, i)
        lists.append(k)
    
    a = AmountAtEachTime(P, r, 360, 60)
    lists.append(a)

    R = np.random.uniform(abs((r) - (0.002)), abs((r) + (0.003)), 25)
    
    b = FixedMortgage(a, R[0], 300)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[0], 300, i)
        lists.append(a)  
  
    b = FixedMortgage(a, R[1], 288)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[1], 288, i)
        lists.append(a)  
  
    b = FixedMortgage(a, R[2], 276)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[2], 276, i)
        lists.append(a)  

    b = FixedMortgage(a, R[3], 264)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[3], 264, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[4], 252)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[4], 252, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[5], 240)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[5], 240, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[6], 228)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[6], 228, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[7], 216)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[7], 216, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[8], 204)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[8], 204, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[9], 192)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[9], 192, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[10], 180)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[10], 180, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[11], 168)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[11], 168, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[12], 156)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[12], 156, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[13], 144)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[13], 144, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[14], 132)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[14], 132, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[15], 120)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[15], 120, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[16], 108)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[16], 108, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[17], 96)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[17], 96, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[18], 84)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[18], 84, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[19], 72)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[19], 72, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[20], 60)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[20], 60, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[21], 48)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[21], 48, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[22], 36)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[22], 36, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[23], 24)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[23], 24, i)
        lists.append(a)  
        
    b = FixedMortgage(a, R[24], 12)

    for i in range(1, 13):
        a = AmountAtEachTime(a, R[24], 12, i)
        lists.append(a)  

    return lists   
        
    
def InterestOnlyMortgage(P, r, n, x, k):
    ## x is the number of months Interest only payments ##
    ## k is the extra amount paid during the interest only payments and will be reduced ##
    ## from the Pricipal when the Fixed Mortgage starts. ##
    ## n is the same total months of the mortgage ##
    r = r/12
    a = P*r*x 
    r = r*12
    

        
    ax = FixedMortgage(P - k, r, n - x)
    b = ax*(n - x)
    c = a + b
    d = FixedMortgage(P, r, n)
    e = d*n
        
    print('Total amount if Interest only + Fixed is: ', c)
    print('Total amount paid if only Fixed Mortgage is: ', e)
        
        
def BalloonMortgage(P, r, n):
    ## Only for 2 years ##
    ## Will be deducting 0.25% of the original Loan amount every month and the new tax which occurs ##
    ## pay the entire sum at the end ##
    ## Will return the payments during the period ##
    
    r = r/12
    lists = []
    
    for i in range(1, n):
        I = r*P
        A = 0.0025*P + I
        P = P - A
        lists.append(A)
    lists.append(P)
    
    return lists


def PriceLevelAdjustedMortgage(P, r, n):
    
    ## I will be assuming the inflation rates change from (-0.1, 0.4) ##
    ## This definition will return 2 lists 1 which contains the remaining Outstanding Principal every month ##
    ## The second list contains the Amortization every month ##
    ## It will also return the randomly taken inflation rates ##
    
    p = np.random.uniform(-0.1, 0.4, n)
    listA = []
    listB = []
    listA.append('Remaining Outstanding Principal starting from month 0:')
    listA.append(P)
    listB.append('Amortization Every Month:')
    
    for i in range(1, n + 1):
        c = FixedMortgage(P, r, n)
        a = AmountAtEachTime(P, r, n, i)
        P = a*(1 + p[i - 1])
        listA.append(a)
        listB.append(c)
    print('Inflation rates taken were: ')    
    print(p)
    print('----------------------------------------------------------------------------------------------------------------')
    print(listB)
    print('----------------------------------------------------------------------------------------------------------------')
    print(listA)
        
    
def SingleMortalityRate(P1, P2, AP, SP):
    ## P1 is the amount of Principal left on month x ##
    ## P2 is the amount of Principal left on month x + 1 ##
    ## AP is the amount paid on month x + 1 ##
    ## SP is the Scheduled Payment which has to be paid on the month x + 1 ##
    
    ## TP is the amount of principal paid on month x + 1 ##
    ## EP is the extra principal paid on month x + 1 ##
    
    TP = P2 - P1
    
    EP = TP - SP
    
    if EP <= 0:
        return 0
    else:
        SMM = EP/(P1 - SP)

        return SMM
    
    
def ConditionalPrepaymentRate(SMM):
    ## This program will calculate CPR1, CPR3, CPR6 ##
    ## Enter 1 or 3 or 6 ##
    ## SMM in percentage ##
    
    z = int(input('Enter a number 1 for CPR1, 3 for CPR3 and 6 for CPR6: '))
    
    if z == 1:
        CPR1 = 1 - ((1 - SMM)**12)
        
        return CPR1
    
    elif z == 3:
        CPR3 = 1 - ((1 - SMM)**4)
        
        return CPR3
    
    elif z == 6:
        CPR6 = 1 - ((1 - SMM)**2)
        
        return CPR6
    
    else:
        
        return 'Invalid Entry'  
    
    
def PSA(a, t):
    ## a is the number required like if 100 then PSA100 will be computed ##
    
    if t >= 30:
        PSA = (a/100)*(0.06)
        return PSA
    
    else:
        CPR = (0.002)*t
        PSA = (a/100)*CPR
        return PSA
        
    
    

