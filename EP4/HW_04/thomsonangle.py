import numpy as np
import matplotlib.pyplot as plt

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
