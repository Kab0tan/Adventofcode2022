# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:15:23 2022

@author: justi
"""



f = open("input day 6.txt",'r')
lines=f.read()

#---------part 1----------
p = list(lines[0:4])

c=4
while len(set(p))<len(p):
    p.pop(0)
    p.append(lines[c])
    c+=1

print(c)

#---------part 2----------
p = list(lines[0:14])

c2=14
while len(set(p))<len(p):
    p.pop(0)
    p.append(lines[c2])
    c2+=1

print(c2)
