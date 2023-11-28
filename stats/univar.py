# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:26:54 2022

@author: William_W
"""
from collections import Counter
import math
from stats.basefunc.xsum import *
def mean(x):
    mean=xsum(x)/len(x)
    return mean 

def Sstddev(x):
    summ=0
    mean=xsum(x)/len(x)
    for i in x:
        summ+=(i-mean)**2
    var=summ/(len(x)-1)
    Sstddev=math.sqrt(var)
    return Sstddev

def Pstddev(x):
    summ=0
    mean=xsum(x)/len(x)
    for i in x:
        summ+=(i-mean)**2
    var=summ/(len(x))
    Pstddev=math.sqrt(var)
    return Pstddev
        
def median(x):
    median=0
    y=sorted(x)
    if (len(x) % 2) ==0:
        median = (y[int(len(x)/2)]+y[int((len(x)/2)-1)])/2
    else:
        median = y[int((len(x)-1)/2)]
    return median

def mode(x):
    c=Counter(x)
    mode=[k for k, v in c.items() if v == c.most_common(1)[0][1]]
    if len(mode)<5:
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
    else:
        return "n/a"

def srange(x):
    y=sorted(x)
    srange=y[len(x)-1]-y[0]
    return srange

    
     
    
        
