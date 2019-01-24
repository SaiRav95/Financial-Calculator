#!/usr/bin/env python
# coding: utf-8

# In[2]:


def BondPrice(F, c, y, T, frequency):
    ## F is the Face Value of the Bond ##
    ## c is the coupon rate of the bond (not in percentage)##
    ## y is the yield to Maturity (YTM) in decimal##
    ## T is the time to maturity (T > 1) ##
    ## frequency is the number of times the coupon is being paid a year ##
    
    N = T*frequency
    N = int(N)
    P = 0
    for i in range(1, N + 1):
        P = P + c/((1 + y)**i)
        
    P = P + (F/((1 + y)**N))
    
    return P

def ZeroCouponBondPrice(F, y, t):
    
    return F/((1 + y)**t)
    

def AccruedInterest(c, x, y):
    ## c is the coupon payment (amount) ##
    ## x is the number of days from last coupon to the settlement date ## 
    ## y is the total number of days in the coupon period ##
    AI = (c*x)/y
    return AI

def DirtyPrice(c, y, n, F, x, l):
    ## c is the semi annual coupon payment ##
    ## y is the yield (decimal) (convert to the required one when given annual) ##
    ## F is the face value of the bond ##
    ## w is the x/l in the Accured Interest ##
    
    w = x/l
    P = 0
    
    for i in range(n):
        P = P + c/((1 + y)**(i + w))  
        
    P = P + F/((1 + y)**(n - 1 + w))
    
    return P

def CleanPrice(c, y, n, F, x, l):
    
    CP = DirtyPrice(c, y, n, F, x, l) - AccruedInterest(c, x, l)
    
    return CP

def HoldingPeriodReturn(FV, PV, m, n):
    
    r = m*(((FV/PV)**(1/(m*n))) - 1)
    
    return r

def SpotRate(d, t):
    ## Spot Rate in percentage ##
    
    ## d is the discount factor d(t) ##
    
    z = 2*(((1/d)**(1/(2*t))) - 1)
    
    return z*100

def ForwardRate(r1, r2, T1, T2):
    FR = ((r2*T2) - (r1*T1))/(T2 - T1)
    
    return FR


def Duration(B1, B2, y1, y2):
    delB = B2 - B1
    dely = y2 - y1
    
    D = -(delB/dely)*(1/B1)
    return D*100


def ModifiedDuration(B1, B2, y1, y2, m):
    ## m is the number of times it is compounded per year ##
    
    MD = Duration(B1, B2, y1, y2)/(1 + (y1/m))
    
    return MD*100

## Duration is the same as ModifiedDuration if m tends to infinity ##

def DollarDuration(B1, B2, y1, y2, m):
    
    DD = B1*ModifiedDuration(B1, B2, y1, y2, m)
    
    return DD

def EffectiveDuration(F, c, y, T, frequency, dy):
    BVplus = BondPrice(F, c, y + dy, T, frequency)
    BVminus = BondPrice(F, c, y - dy, T, frequency)
    
    EffDu = (BVminus - BVplus)/(2*dy*BondPrice(F, c, y, T, frequency))
    
    return EffDu

def Convexity(F, c, y, T, frequency, dy):
    BVplus = BondPrice(F, c, y + dy, T, frequency)
    BVminus = BondPrice(F, c, y - dy, T, frequency)
    
    N = BVplus + BVminus - 2*BondPrice(F, c, y, T, frequency)
    D = (dy**2)*BondPrice(F, c, y, T, frequency)
    
    C = N/D
    
    return C

def BondPercentageChange(F, c, y, T, frequency, dy):
    PC = -100*dy*EffectiveDuration(F, c, y, T, frequency, dy) + 0.5*100*(dy**2)*Convexity(F, c, y, T, frequency, dy)
    
    return PC

def DV01(F, c, y, T, frequency, dy):
    
    DV = 0.0001*EffectiveDuration(F, c, y, T, frequency, dy)*BondPrice(F, c, y, T, frequency)
    
    return DV

def GrossRealizedReturns(P, F, c):
    ## P is present value of the bond time t##
    ## F is the price of the bond purchased ##
    ## c is the coupon received on at time t ##
    R = ((P + c - F)/F)*100
    
    return R

def NetRealizedReturns(P, F, c, r, n):
    ## r is the annual rate at which the borrowing was made to buy the bond ##
    ## n will be used just to convert annual to whatever is desired ##
        
    NR = GrossRealizedReturns(P, F, c) - r/n
    
    return NR
    
    
    

