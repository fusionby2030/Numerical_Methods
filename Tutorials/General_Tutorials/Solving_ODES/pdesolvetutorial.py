import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'


x, dx = np.linspace(0, 2*np.pi, retstep=True)
u = lambda x: np.sin(x)
def finite_difference(x, dx, f):
    dudx = np.zeros(len(x))
    for i in range(0, len(x) - 1):
        #print(f(x[i+1]))
        dudx[i] = (f(x[i+1]) - f(x[i]))*(1/dx)
    return dudx
def finite2_difference(x, dx, f):
    d2udx2 = np.zeros(len(x))
    for i in range(1, len(x) -1):
        d2udx2[i] = (1/dx**2)*(f(x[i+1]) - 2*f(x[i]) + f(x[i-1]))
    return d2udx2
dudx = finite_difference(x, dx, u)
plt.plot(x, u(x), label='U(x)')
plt.plot(x, dudx, label='U`')
plt.plot(x, finite2_difference(x, dx, u), label='U``')
plt.legend()
