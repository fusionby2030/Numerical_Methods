"""
Find Volume of Sphere

Utelize the symmetry: find one quarter of hemisphere and multiply by 4
"""

from random import random
from math import sqrt, pi
#radius = 1
N = 1000000 #Number of points in the unit cube
count = 0 # Number of points within sphere
for j in range(N):
    point = (random(), random(), random())
    if point[0]*point[0] + point[1]*point[1] + point[2]*point[2] < 1:
        count += 1
Volume = float(count)/float(N)*4

print("The volume of a sphere of radius 1 is {:.4} +/- {:.4}".format(Volume, 4*sqrt(N)/float(N)))
print("Known value of sphere of radius 1: {:.4}".format(2.0/3*pi))


"""
Integral of sin(x) from 0 -> pi

"""
from math import sin
import numpy as np
from random import uniform
N = 1000000
count = 0
for j in range(N):
    point = (uniform(0, pi), random())
    if np.abs(point[1]) > sin(point[0]):
        count += 0
    else:
        count += 1
Area = float(count)/float(N)*pi
print("The approximated area of sinx from 0 to pi  is {:.6} +/- {:.4}".format(Area, pi*sqrt(N)/float(N)))
print("Known value of sphere of radius 1: {}".format(2))
"""
4D Sphere 
"""
