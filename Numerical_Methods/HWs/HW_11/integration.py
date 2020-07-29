import numpy as np
"""
Trapezoidal Rule
partition domain [a,b] into N equally spaced (h) points
sum from 1st point to N then multiply by h/2
"""
func = lambda x: np.sin(x)
f1 = lambda x: 1.0/x
def traprule(f, a, b, n):
    partition, h = np.linspace(a, b, num=n+1, retstep=True)
    sum = 0
    for i in range(1, len(partition)):
        sum += h*(f(partition[i-1]) + f(partition[i]))/2.0
    return sum
def trapezoidal(f, a, b, h):
    partition = np.arange(a, b+h, step=h)
    sum = 0.0
    for i in range(1, len(partition)):
        sum += h*(f(partition[i-1]) + f(partition[i]))/2.0
    return sum

real = 0.18232155679
#i
wosi = trapezoidal(f1, 1, 1.2, 0.2)
error = np.abs(real - wosi)
relative = error/real
#ii
wsi = traprule(f1, 1, 1.2, 2)
error1 = np.abs(real - wsi)
realtive = error1/real
#iii
error3 = real - (0.54696/3)
realative = error3/real
"""
Simpson Rule
"""
f2 = lambda x: np.exp(-x*x)
real1 = 0.535188258

def simpsonrule(f, a, b, n):
    partition= np.linspace(a, b, n+1) #Create Sub intervals
    h = (b-a)/n #Compute step
    y = f(partition)
    S = h/3.0*np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return S


seven = simpsonrule(f2, 0, 0.6, 6)
error2 = np.abs(real1 - seven)

fourty = simpsonrule(f2, 0, 0.6, 48)
error3 = np.abs(real1 - fourty)
