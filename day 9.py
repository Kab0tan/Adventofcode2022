# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 23:11:33 2022

@author: justi
"""
import numpy as np

f = open("input day 9.txt",'r')
lines=f.read()
input = [i.split(' ') for i in lines.split('\n')]

#---------------------------part 1 ---------------
s, H, T = [0,0] , [0,0], [0,0]
T_path=[T]

for deplacement in input:
    direction = deplacement[0]
    distance = int(deplacement[1])
    for pas in range(distance):
        H_last_pos = [H[0],H[1]]
        if direction == 'R':
            H[1]+=1
        elif direction == 'L':
            H[1]-=1
        elif direction == 'U':
            H[0]+=1
        elif direction == 'D':
            H[0]-=1
        if np.abs(T[0]-H[0])==2 or np.abs(T[1]-H[1])==2:
            T = H_last_pos
            if T not in T_path:
                T_path.append(T)
print(len(T_path))        
#----------------part 2------------------
Head =[0,0]
A,B,C,D,E,F,G,H,I = [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]

rope=[Head,A,B,C,D,E,F,G,H,I]

def checking_around(x,y):
    if y[1]-x[1]==2 and y[0]>x[0]:
        x[0]+=1
        x[1]+=1
    elif y[0]-x[0]==2 and y[1]>x[1]:
        x[0]+=1
        x[1]+=1
    elif y[1]-x[1]==-2 and y[0]>x[0]:
        x[0]+=1
        x[1]-=1
    elif y[0]-x[0]==2 and y[1]<x[1]:
        x[0]+=1
        x[1]-=1
    elif y[1]-x[1]==2 and y[0]<x[0]:
        x[0]-=1
        x[1]+=1
    elif y[0]-x[0]==-2 and y[1]>x[1]:
        x[0]-=1
        x[1]+=1
    elif y[1]-x[1]==-2 and y[0]<x[0]:
        x[0]-=1
        x[1]-=1
    elif y[0]-x[0]==-2 and y[1]<x[1]:
        x[0]-=1
        x[1]-=1
    elif y[0]-x[0] == 2 and y[1] == x[1]:
        x[0]+=1
    elif y[0]-x[0] == -2 and y[1] == x[1]:
        x[0]-=1
    elif y[1]-x[1] == 2 and y[0] == x[0]:
        x[1]+=1
    elif y[1]-x[1] == -2 and y[0] == x[0]:
        x[1]-=1
        
tail_path=[I[:]]

for deplacement in input:
    direction = deplacement[0]
    distance = int(deplacement[1])
    for pas in range(distance):
        if direction == 'R':
            Head[1]+=1
        elif direction == 'L':
            Head[1]-=1
        elif direction == 'U':
            Head[0]+=1
        elif direction == 'D':
            Head[0]-=1
        for i in range(len(rope)-1):
            checking_around(rope[i+1], rope[i])
        if rope[9] not in tail_path:
            tail_path.append(rope[9][:])
print(len(tail_path))
            