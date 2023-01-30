# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:19:00 2022

@author: justi
"""


from numpy import loadtxt
import string

f = loadtxt('input day 3.txt',dtype=str)

values_lower = dict()
values_upper = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values_lower[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
    values_upper[letter] = index + 27

#--------------part 1------------------------------
s=0
for line in f: 
    L1 = int(len(line)/2)
    common = list(set(line[:L1]).intersection(line[L1:]))[0]
    if common in string.ascii_lowercase:
        priority = values_lower[common]
    else:
        priority = values_upper[common]
    s+= priority

print(s)

#------------part 2------------
L= len(f)
groups=[]
for i in range(0,L,3):
    groups.append([f[i],f[i+1],f[i+2]])

s2=0
for group in groups:
    common2 = list(set.intersection(*map(set,group)))[0]
    if common2 in string.ascii_lowercase:
        priority = values_lower[common2]
    else:
        priority = values_upper[common2]
    s2+= priority
    
print(s2)