# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:33:45 2022

@author: justi
"""

import open3d as o3d
import typing
import PIL
import numpy as np
from numpy import loadtxt


#------------part 1 -------------
f = open("input day 1.txt",'r')
lines=f.read()
group = [list(map(int,groups.split('\n'))) for groups in lines.split('\n\n')]
sommes = [sum(groups) for groups in group]
print(max(sommes))


#-----------part 2-----------

tri = sorted(sommes)
top_three = tri[-3:]

print(sum(top_three))

