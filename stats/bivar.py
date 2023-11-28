# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:48:15 2022

@author: William_W
"""

from stats.basefunc.xsum import *
from scipy.stats import t
def covariance(x,y):
    summ=0
    meanx=xsum(x)/len(x)
    meany=xsum(y)/len(y)
    if len(x) != len(y):
        print("warning:imcompatible data,size x != size y")
    else:
        for i in range(len(x)):
            summ+=(x[i]-meanx)*(y[i]-meany)
    covar=summ/(len(x)-1)
    return covar

def pearsons(x,y):
    covarxx=covariance(x,x)
    covarxy=covariance(x,y)
    covaryy=covariance(y,y)
    pearsons=covarxy/(covarxx*covaryy)**(1/2)
    return pearsons
    
def spearmans(x,y):
    xranked=rank(x)
    yranked=rank(y)
    spearmans=pearsons(xranked,yranked)
    return spearmans

def gradient(x,y):
    r=pearsons(x,y)
    sx=(covariance(x,x))**(1/2)
    sy=(covariance(y,y))**(1/2)
    gradient=r*sy/sx
    return gradient
    
def intercept(x,y):
    meanx=xsum(x)/len(x)
    meany=xsum(y)/len(y)
    grad=gradient(x,y)
    intercept=meany-grad*meanx
    return intercept

def ppmc2pval(r,n):
    tval=r*((n-2)/(1-r**2))**(1/2)
    pval=t.sf(abs(tval),n-2)
    return pval
    

    