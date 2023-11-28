# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 22:45:47 2022

@author: William_W
"""
from collections import Counter
def xsum(x):
    summ=0
    for i in x:
        summ+=i
    return(summ)
    
def xysum(x,y):
    summ=0
    if len(x) != len(y):
        print("warning:imcompatible data,size x != size y")
        for i in range(0,min(len(x),len(y))):
            summ+=x[i]*y[i]
    else:
        for i in range(0,len(x)):
            summ+=x[i]*y[i]
    return(summ)
        
def x2sum(x):
    summ=0
    for i in x:
        summ+=(i**2)
    return(summ)

def rank(x):
    c=Counter(x)
    temp=x[:] #have to shallow copy otherwise removes from both lists
    ranked=[0]*len(x)
    for i in range(len(x)):
        mini=temp.index(min(temp))
        temp[mini]=float("inf")
        ranked[mini]=i+1
    for i in c.keys():
        if c[i]>1:
            temp2=x[:]
            dupe=[]
            a=0
            for j in range(0,len(x)):
                if temp2[j]==i:
                    dupe.append(j)
            a=ranked[dupe[0]]+((c[i]-1)/2)
            for k in dupe:
                ranked[k]=a   
    return ranked

def rank2(x):
    temp=x[:] #have to shallow copy otherwise removes from both lists
    rank=[0]*len(x)
    for i in range(len(x)):
        mini=temp.index(min(temp))
        temp[mini]=float("inf")
        rank[mini]=i+1
    return rank