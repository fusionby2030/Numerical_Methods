import numpy as np



"""
Trapezoidal Rule
partition domain [a,b] into N equally spaced (h) points
sum from 1st point to N then multiply by h/2
"""
func = lambda x: np.sin(x)

def traprule(f, a, b, n):
    partition, h = np.linspace(a, b, num=n, retstep=True)
    sum = 0
    for i in range(1, len(partition)):
        sum += h*(func(partition[i-1]) + func(partition[i-1]))/2.0
    return sum

def simpsonrule(f, a, b, n):
    partition= np.linspace(a, b, n+1)
    h = (b-a)/n
    y = f(partition)
    S = h/3.0*np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S
simpsonrule(func, 0, np.pi, 8)

error = np.abs(2 - simpsonrule(func, 0, np.pi, 8))
relative = error/2
