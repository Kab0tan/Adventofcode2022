# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:51:38 2022

@author: justi
"""

import numpy as np

f = open("input day 8.txt",'r')
lines=f.read()
input = np.array([list(map(int,i)) for i in lines.split()])

#----------------part 1-------------

# def visible(neigh,i,j):
#     c=0
#     for l in neigh:
#         # print(l)
#         if np.any(l >= input[i,j]):
#             c+=1
#     # print("mon c vaut",c)
#     if c==4:
#         return False
#     return True
    
# n=0
# for i in range(1,input.shape[0]-1):
#     for j in range(1,input.shape[1]-1):
#         neigh = [input[:i,j],input[i,:j],input[i+1:,j],input[i,j+1:]]
#         if visible(neigh,i,j):
#             # print(input[i,j])
#             n+=1

# ext = input.shape[0]*2+(input.shape[1]-2)*2
# print(ext)
# print(n+ext)

#----------------part 2---------------

def visible2(i,j):
    c=[]
    current = input[i,j] #current tree
    neigh = [input[:i,j],input[i,:j],input[i+1:,j],input[i,j+1:]] #je récup les lignes des voisins de current tree
    neigh = [i.tolist() for i in neigh] 
    for i in range(2): #je mets les lignes de voisins dans le bon ordre (les arbres de gauche et en haut)
        neigh[i].reverse()
    for d in neigh: #je parcours les 4 directions de voisins
        count=0 #pour chaque direction je compte le nombre d'arbres observables
        for i in range(len(d)): 
            if d[i] >= current : 
                count+=1
                c.append(count) #j'ajoute le nombre d'arbres observable dans la direction d, à ma liste c
                break
            else:
                count+=1
                if count == len(d):
                    c.append(count)
                    break
    return c #je récup la liste de taille 4 du nombre d'arbre que je vois dans chaque directions pour mon current tree

views = [] 
for i in range(1,input.shape[0]-1): #on prend pas en comptes les bords
    for j in range(1,input.shape[1]-1):
        views.append(np.prod(visible2(i,j)))
        
print(max(views))



