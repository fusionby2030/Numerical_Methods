import numpy as np


def derivative_approx(f, x, h=.00000001):
    return (f(x+h) - f(x)) / h

def newton_raphson(f, x, tolerance=.001):
    steps_taken = 0
    tangentline = []
    x_values = []
    while abs(f(x)) > tolerance:
        x_values.append(x)
        df = derivative_approx(f, x)
        x = x - f(x)/df
        steps_taken += 1
        tangentline.append(df)
    return x, steps_taken, tangentline, x_values

g = lambda y: y*np.log(y) -1.3 #Problem 2
root, steps, tangentline, tangentx = newton_raphson(g, 4)
p = lambda x: x**2 - 1/15.0 #Problem 3
root2, steps2, tangentline2, tangentx2 = newton_raphson(p, 2)

import matplotlib.pyplot as plt

SMALL_SIZE = 12
MEDIUM_SIZE = 15
BIGGER_SIZE = 20


plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=SMALL_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)

plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'

x_values = np.linspace(0,3.5)
plt.title("Newton Raphson for xlogx = 1.3")
plt.hlines(0, xmin=0, xmax=3.5, color=green)
plt.plot(x_values, g(x_values))
plt.scatter(root, g(root), color=pink, label='Root at {0:8.4f}'.format(root))
plt.legend()
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Numerical_Methods/HW_04')
