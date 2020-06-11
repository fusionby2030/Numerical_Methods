import numpy as np
import matplotlib.pyplot as plt # hartree atomic units
from scipy.special import genlaguerre, factorial, lpmv
import scipy as sci

plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'


n = 3
l = 1
m = 0
a_0 = 1
def radial_wave_function_prob(r, theta = 0, phi = 0, n=3 ):
    const1 = np.sqrt(((2/(n*a_0))**3)*(np.math.factorial(n-l-1)/(2*n*np.math.factorial(n+l))))
    const2 = genlaguerre(n-l-1, 2*l+1)(2*r/(n*a_0))
    expon = np.exp(-r/(n*a_0))
    other = ((2*r)/(n*1_0))**l
    #f_lm = np.sqrt(np.math.factorial((2*l + 1)*(l-m))/(4*np.pi*np.math.factorial(l+m)))*lpmv(m, l, theta)
    #g_m = np.exp(m*phi)
    return ((4*np.pi*(r**2))*(const1*expon*other*const2)**2)



""" Angular Probability Distribution """

def angular_function(theta, phi):
    f_lm = np.sqrt(np.math.factorial((2*l + 1)*(l-m))/(4*np.pi*np.math.factorial(l+m)))*lpmv(m, l, np.cos(theta))
    g_m = np.exp(np.imag(m*phi))
    Y_lm = np.outer(g_m, f_lm)
    return Y_lm
def angular_prob(the, pee):
    f_lm = np.sqrt(np.math.factorial((2*l + 1)*(l-m))/(4*np.pi*np.math.factorial(l+m)))*lpmv(m, l, np.cos(the))
    g_m = np.exp(np.imag(m*pee))
    Y_lm = np.outer(g_m, f_lm)
    return np.abs(Y_lm)**2
tt = np.linspace(0, 2*np.pi, num = 400)
pp = np.linspace(-np.pi, np.pi, num = 400)
Y_lm = angular_function(tt, pp)[0]



"""
ang_prob = angular_prob(tt, pp)
xs = ang_prob*np.outer(np.cos(tt), np.sin(pp))
ys = ang_prob*np.outer(np.sin(pp), np.sin(pp))
zs = ang_prob*np.outer(np.ones(np.size(pp)), np.cos(pp))
xs1 = np.outer(np.cos(tt), np.sin(pp))
ys1 = np.outer(np.sin(pp), np.sin(pp))
zs1 = np.outer(np.ones(np.size(pp)), np.cos(pp))

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
color_map = cm.jet
scalarMap = cm.ScalarMappable(norm=plt.Normalize(vmin=np.min(ang_prob), vmax=np.max(ang_prob)), cmap=color_map)
C = scalarMap.to_rgba(ang_prob)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xs, ys, zs, rstride=2, cstride=2, color='b', facecolors=C)
#ax1 = fig.add_subplot(111, projection='3d')
#ax1.plot_surface(xs1, ys1, zs1, rstride=2, cstride=2, color='b', facecolors=C)
"""
