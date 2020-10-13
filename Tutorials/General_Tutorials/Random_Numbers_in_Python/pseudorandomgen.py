import numpy as np
"""
Linear Congruential Generator
"""

def lcg(x, a=5, b=3, c=8):
    return (a*x + b)%c


"""
Downfalls of Randu
They all fall into 3 catagories (spectrums)
"""
import matplotlib.pyplot as plt
def randu(x, a=65539, b=0, c=2E31):
    return (a*x +b)%c
