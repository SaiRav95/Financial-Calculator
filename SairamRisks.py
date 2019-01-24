#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import scipy.stats as st


def ExpectedLoss(PD, EA, LR):
    ## PD is the probability of default or Expected Default frequency (EDF) ##
    ## EA is the Exposure Amount (Total loan amount) ##
    ## LR is the loss rate (severity of default) ##
    
    EL = EA*PD*LR
    
    return EL

def RecoveryRate(LR):
    RR = 1 - LR
    
    return RR

def UnexpectedLoss(EA, PD, LR, stdLR):
    ## Assuming 2 state model ##
    
    VarPD = PD*(1 - PD)
    
    UL = EA*math.sqrt(PD*(stdLR**2) + (LR**2)*VarPD)
    
    return UL
    
def PortfolioExpectedLoss(PD1, EA1, LR1, PD2, EA2, LR2):
    EL1 = ExpectedLoss(PD1, EA1, LR1)
    EL2 = ExpectedLoss(PD2, EA2, LR2)
    
    ELp = EL1 + EL2
    
    return ELp

def PortfolioUnexpectedLoss(EA1, PD1, LR1, stdLR1, EA2, PD2, LR2, stdLR2, rho):
    ## rho is the correlation between the assets ##
    
    UL1 = UnexpectedLoss(EA1, PD1, LR1, stdLR1)
    UL2 = UnexpectedLoss(EA2, PD2, LR2, stdLR2)
    
    ULp = math.sqrt((UL1**2) + (UL2**2) + 2*rho*UL1*UL2)
    
    return ULp

def RiskContribution(EA1, PD1, LR1, stdLR1, EA2, PD2, LR2, stdLR2, rho):
    
    ## Enter x as 1 or 2 for risk contribution of those assets ##
    x = int(input('Enter a number: '))
    UL1 = UnexpectedLoss(EA1, PD1, LR1, stdLR1)
    UL2 = UnexpectedLoss(EA2, PD2, LR2, stdLR2)
    ULp = PortfolioUnexpectedLoss(EA1, PD1, LR1, stdLR1, EA2, PD2, LR2, stdLR2, rho)
    
    if x == 1:
        
        RC1 = UL1*(UL1 + (rho*UL2))/ULp
        
        return RC1
    
    elif x == 2:
        
        RC2 = UL2*(UL2 + (rho*UL1))/ULp
        
        return RC2
    
def FirmSizeScaleAdjustement(Xr, Yl, Yr):
    
    ## Operational Risk ##
    ## This is a formula when you want to see your scale of severity by viewing data from others banks ##
    ## Xr is the Bank X revenue ##
    ## Yl is the Bank Y loss from that event ##
    ## Yr is the Bank Y revenue ##
    ## We want to calculate the Bank X loss from that event by readjusting the scale ##
    
    Xl = Yl*((Xr/Yr)**0.23)
    
    return Xl

def ValueAtRisk(V, alpha, mu, sigma):
    ## Assuming VAR as Normal Distribution ##
    ## V is portfolio value ##
    ## mu is the Expected Portfolio return ##
    ## alpha is the significance level ## 
    
    z = st.norm.ppf(alpha)
    
    var = (mu - z*sigma)*V
    
    return var

def ExpectedShortFall(V, alpha, mu, sigma):
    ES = (-mu + sigma * stats.norm.pdf(stats.norm.ppf(alpha))/(1-(alpha)))*V
    
    return ES

def LognormalValueAtRisk(V, alpha, mu, sigma):
    Lvar = V*(1 - math.exp(mu - (st.norm.ppf(alpha))*sigma ))
    
    return Lvar

