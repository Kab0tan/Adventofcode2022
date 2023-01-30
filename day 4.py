# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 09:36:37 2022

@author: justi
"""


f = open("input day 4.txt",'r')
lines=f.read()
group = [[list(map(int,groupsbis.split('-'))) for groupsbis in groups.split(',')] for groups in lines.split('\n')]

#------------------part 1---------------------
n=0
for g in group:
    if (g[0][0]<=g[1][0] and g[1][1]<=g[0][1]) or (g[1][0]<=g[0][0] and g[0][1]<=g[1][1]):
        n+=1
print(n)

#------------------part 2-----------------
def convert(x):
    L1=set(range(x[0][0],x[0][1]+1))
    L2=set(range(x[1][0],x[1][1]+1))
    inter = L1.intersection(L2)
    return len(inter)

n2=0
for g in group:
    if convert(g) != 0:
        n2+=1
print(n2)


    
