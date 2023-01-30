# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:28:19 2022

@author: justi
"""

import numpy as np
from numpy import loadtxt
f = loadtxt('input day 2.txt',dtype=str, delimiter=",")

#-----------------part 1----------
comb = {'A X':4,'A Y':8,'A Z':3,'B X':1,'B Y':5,'B Z':9,'C X':7,'C Y':2,'C Z':6}
s=0
for round_ in f:
    s+= comb[round_]
    
print(s)
#--------------part 2-------------
comb2 = {'A X':3,'A Y':4,'A Z':8,'B X':1,'B Y':5,'B Z':9,'C X':2,'C Y':6,'C Z':7}
s2=0
for round_ in f:
    s2+= comb2[round_]
    
print(s2)