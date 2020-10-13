"""
The Random Walk
A drunk man is standing outside of a bar, he can take a step east or west.
An even probability of each (0.5), and step lengths are all the same.
How fast on average does this random walk move the man away from the bar?
"""
from random import choice
import numpy as np
import matplotlib.pyplot as plt
N = 200

x = np.zeros(N)
t = np.arange(0, N)

for i in range(1, N):
    if choice(['east','west']) == 'west':
        x[i] = x[i-1] - 1
    else:
        x[i] = x[i]+1
RMS = np.array([np.sqrt(i*i) for i in x])

plt.plot(t, x, 'b')
plt.plot(t, RMS, 'g')
"""
Multiple Men
"""

"""
Diffusion and Entropy
"""
