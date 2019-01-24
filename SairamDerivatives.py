#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
from scipy.stats import norm


def d1(S, K, r, q, sigma, T):
    
    ## S is the asset Price ##
    ## K is the strike Price ##
    ## r is the risk free interest rate ##
    ## q is the dividend rate ##
    ## sigma is volatility ##
    ## T is Time to Maturity ##
    
    d1 = (math.log(S/K) + (r - q + 0.5*(sigma)**2)*T)/(sigma*(math.sqrt(T)))
    return d1
    
def d2(S, K, r, q, sigma, T):
    
    d2 = d1(S, K, r, q, sigma, T) - (sigma*(math.sqrt(T)))

    return d2

def DeltaCallOption(S, K, r, q, sigma, T):
    a = d1(S, K, r, q, sigma, T)
    D = norm.cdf(a)
    
    return D*math.exp(-(q*T))

def DeltaPutOption(S, K, r, q, sigma, T):
    a = DeltaCallOptions(S, K, r, q, sigma, T) - math.exp(-(q*T))
    return a

def CallOption(S, K, r, q, sigma, T):
    a = d1(S, K, r, q, sigma, T)
    b = d2(S, K, r, q, sigma, T)
    
    c = S*(math.exp(-(q*T)))*(norm.cdf(a)) - K*(math.exp(-(r*T)))*norm.cdf(b)
    
    return c

def PutOption(S, K, r, q, sigma, T):
    
    a = d1(S, K, r, q, sigma, T)
    b = d2(S, K, r, q, sigma, T)
    
    p = K*(math.exp(-(r*T)))*norm.cdf(-b) - S*(math.exp(-(q*T)))*(norm.cdf(-a))
    
    return p

def ForwardDelta(q, T):
    FD = math.exp(-(q*T))
    
    return FD

def FuturesDelta(r, q, T):
    FD = math.exp((r - q)*T)
    
    return FD

################
def Nddash(x):
    
    a = (1/math.sqrt(2*math.pi))*math.exp(-(x**2)/2)
    
    return a
################

def ThetaCall(S, K, r, q, sigma, T):
    ## Theta is measured in Trading days in this formulas ##
    
    a = d1(S, K, r, q, sigma, T)
    b = d2(S, K, r, q, sigma, T)
    c = Nddash(a)
    
    T = -(math.exp(-(q*T)))*((S*c*sigma)/2*math.sqrt(T)) - r*K*(math.exp(-(r*T)))*norm.cdf(b) + q*S*math.exp(-(q*T))*norm.cdf(a)
    
    return T/252

def ThetaPut(S, K, r, q, sigma, T):
    
    a = d1(S, K, r, q, sigma, T)
    b = d2(S, K, r, q, sigma, T)
    c = Nddash(a)
    
    T = -(math.exp(-(q*T)))*((S*c*sigma)/2*math.sqrt(T)) + r*K*(math.exp(-(r*T)))*norm.cdf(-b) - q*S*math.exp(-(q*T))*norm.cdf(-a)
    
    return T/252

def GammaEuro(S, K, r, q, sigma, T):
    
    a = d1(S, K, r, q, sigma, T)
    
    G = (math.exp(-(q*T)))*Nddash(a)/(S*sigma*math.sqrt(T))
    
    return G

def VegaEuro(S, K, r, q, sigma, T):
    
    a = d1(S, K, r, q, sigma, T)
    v = S*(math.exp(-(q*T)))*(math.sqrt(T))*Nddash(a)
    
    V = v/100
    
    return V

def RhoCall(S, K, r, q, sigma, T):
    
    b = d2(S, K, r, q, sigma, T)
    rc = K*T*(norm.cdf(b))*(math.exp(-(r*T)))
    
    return rc/100

def RhoPut(S, K, r, q, sigma, T):
    
    b = d2(S, K, r, q, sigma, T)
    
    rp = -K*T*(norm.cdf(-b))*(math.exp(-(r*T))) 
    
    return rp/100


def ForwardPrice(S, r, q, t):
    
    ## S is the asset price ##
    ## r is the continously compunded interest rate ##
    ## q is the dividend rate or foreign currency rate ##
    ## t is the time to maturity ##
    ## Basically this has no cash flows ##
    
    F = S*(math.exp((r-q)*t))
    return F
    
def ForwardPriceCarryingCost(S, r, q, t, I):
    ## I is the carrying cost (cash flow for example) ##
    
    F = (S - I)*(math.exp((r - q)*t))
    return F

def ForwardPriceConvenienceYield(S, r, q, t, u, y):
    ## U is the storage cost this is for Consumption assets ##
    ## y is the convenience Yield ##
    
    F = (S + U)*(math.exp((r - q + u - y)*t))
    return F


    


