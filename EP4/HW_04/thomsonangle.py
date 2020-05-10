import numpy as np
import matplotlib.pyplot as plt



SMALL_SIZE = 10
MEDIUM_SIZE = 12
BIGGER_SIZE = 20


plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)

plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'




"""
3D Random Walk


Create 3d lattice 20x20

Have Atom defined on lattice:
Atom:
Radius - 15 -> takes up 10x10
Particle enters on

Particle enters from

"""

dim = 2
N = 200
np.random.rand()
trials = 500
R = np.empty(trials)
for i in range(trials):
    for j in range(N):
        theta = np.random.rand()*np.pi*2
        x = np.cos(theta)
        y = np.sin(theta)
        r = np.sqrt(x**2 + y**2)
    R[i] = r
R = np.sum(R)
meansquared = R**2
