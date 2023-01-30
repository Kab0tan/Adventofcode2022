# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:03:58 2022

@author: justi
"""
import numpy as np
import sys

f = open("input day 7.txt",'r')
lines=f.read()
input = [i.split(' ') for i in lines.split('\n')]
# input = [i for i in lines.split('\n')]


#-----------part 1------------
def add(dic,ind):
    dic['somme'] = 0
    ind += 2
    while input[ind][0] != '$':
        # print(input[ind][0])
        if input[ind][0] == 'dir':
            dic[input[ind][1]] = {}
            ind_bis = input.index(['$','cd',input[ind][1]])
            add(dic[input[ind][1]],ind_bis)
        else:
            # dic[input[ind][1]] = input[ind][0]
            dic['somme'] += int(input[ind][0])
        ind+=1 

dicracine ={}
add(dicracine,0)


# def sommation(dico,res):
#     dico['somme']= dico.pop('somme')
#     # print("mon dico est mtn",dico)
#     for key,value in dico.items():
#         if type(value) == dict:
#             dico['somme']+= sommation(value,res)
#         else:
#             if dico['somme']<100000:
#                 res.append(dico['somme'])
#                 # print("mon res vaut",res)
#             # print("blabl",dico['somme'])
#             return dico['somme']
            
# first_somme= dicracine['somme']
# res=[]
# sommation(dicracine,res)
# print(sum(res))
            