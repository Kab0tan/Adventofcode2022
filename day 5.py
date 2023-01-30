# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 08:19:39 2022

@author: justi
"""
import re

f = open("input day 5 b.txt",'r')
lines=f.read()
input = [i for i in lines.split('\n')]

def formatage(g):
    last_col=0
    for i in range(len(g[-1])-1,0,-1): #parcourir la dernière ligne des stacks pour savoir cb de stacks
        if g[-1][i] != ' ':
            last_col = int(g[-1][i])
            break
    d={}
    for i in range(1,last_col+1) : #on crée dico pour avoir listes ordonnées de chaque stack
        d["{0}".format(i)] = [] #pourrait aussi juste mettre d[i]
    
    
    for line in range(len(g)-1):
        c=1
        for l in range(1,len(g[line]),4):
            d["{0}".format(c)].append(g[line][l])  
            c+=1
    
    for key in d:
        d[key] = d[key][::-1]
        d[key] = list(filter(lambda a:a != ' ', d[key]))
        
    return d
 
       
d1 = formatage(input)         
d2 = formatage(input)         

f2 = open("input day 5.txt",'r')
lines2 = f2.read()

input2 = [[ word for word in re.split('move | from | to ',i)] for i in lines2.split('\n')]
for line in input2:
    line.pop(0)


#----------------part 1--------------------

def move(dic,amount,src,dest):
    for it in range(amount):
        dic[dest].append(dic[src].pop())

for line in input2:
    move(d1,int(line[0]),line[1],line[2])

msg=[]
for key in d1:
    msg.append(d1[key][-1])

print(''.join(msg))

#----------------------part 2-----------------

def move2(dic,amount,src,dest):
    for i in range(amount,0,-1):
        dic[dest].append(dic[src][-i])
    del dic[src][-amount:]


for line in input2:
    move2(d2,int(line[0]),line[1],line[2])

msg2=[]
for key in d2:
    msg2.append(d2[key][-1])

print(''.join(msg2))