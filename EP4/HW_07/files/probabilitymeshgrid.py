import numpy as np
import matplotlib.pyplot as plt # hartree atomic units
from scipy.special import genlaguerre, factorial, lpmv
import scipy as sci

plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
#https://www.google.com/search?client=ubuntu&channel=fs&q=hydrogen+probability+distribution+python&ie=utf-8&oe=utf-8

"""
r = np.linspace(-R,R,200)
phi = np.linspace(-2*np.pi,2*np.pi,200)
radius_matrix, theta_matrix = np.meshgrid(r,phi)
X = radius_matrix * np.cos(theta_matrix)
Y = radius_matrix * np.sin(theta_matrix)
#ax = plt.subplot(111, polar=True)
#ax.plot(theta_matrix, radius_matrix, color='r', ls='none', marker='.')
"""

""" Sample N """
n = 3
l = 1
m = 0
a_0 = 1
""" Radial Function and Plot """
def radial_wave_function(r, n):
    const1 = np.sqrt(((2/(n*a_0))**3)*(np.math.factorial(n-l-1)/(2*n*np.math.factorial(n+l))))
    const2 = genlaguerre(n-l-1, 2*l+1)(2*r/(n*a_0))
    expon = np.exp(-r/(n*a_0))
    other = ((2*r)/(n*1_0))**l
    return const1*expon*other*const2
def radial_wave_function_prob(r, theta = 0, phi = 0, n=3 ):
    const1 = np.sqrt(((2/(n*a_0))**3)*(np.math.factorial(n-l-1)/(2*n*np.math.factorial(n+l))))
    const2 = genlaguerre(n-l-1, 2*l+1)(2*r/(n*a_0))
    expon = np.exp(-r/(n*a_0))
    other = ((2*r)/(n*1_0))**l
    #f_lm = np.sqrt(np.math.factorial((2*l + 1)*(l-m))/(4*np.pi*np.math.factorial(l+m)))*lpmv(m, l, theta)
    #g_m = np.exp(m*phi)
    return ((4*np.pi*(r**2))*(const1*expon*other*const2)**2)
def radial_superposition(r, n1, n2):
    wfn1 = n1*radial_wave_function(r, n1)
    wfn2 = n2*radial_wave_function(r, n2)
    pn1 =radial_wave_function_prob(r, n = n1)
    pn2 = radial_wave_function_prob(r, n = n2)
    extra = wfn1*wfn2*(np.pi*4*r**2)*2
    return pn1 + pn2 + extra

"""
To DO: Seperate Probability and WF to respective graphs
Add Axes and Title

"""

""" Angular Probability Distribution """
tt = np.linspace(0, 2*np.pi, num = 400)
pp = np.linspace(-np.pi, np.pi, num = 400)

def angular_function(theta, phi):
    f_lm = np.sqrt(np.math.factorial((2*l + 1)*(l-m))/(4*np.pi*np.math.factorial(l+m)))*lpmv(m, l, np.cos(theta))
    g_m = np.exp(np.imag(m*phi))
    return f_lm, g_m
def angular_prob(the, pee):
    f_lm = np.sqrt(np.math.factorial((2*l + 1)*(l-m))/(4*np.pi*np.math.factorial(l+m)))*lpmv(m, l, np.cos(the))
    g_m = np.exp(np.imag(m*pee))
    Y_lm = np.outer(g_m, f_lm)
    return np.abs(Y_lm)**2
f, g = angular_function(theta, phi)
ft, gt = angular_function(tt, pp)

ang_prob =angular_prob(tt, pp)
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

""" Total Density """

R = 15
u = np.linspace(-15, 15, num = 200)
v = u
X, Y = np.meshgrid(u, v)
Z = np.zeros_like(X)
r = np.sqrt(X**2 + Y**2)
r[0].shape
theta = np.zeros_like(r[0])
phi = np.arctan(Y/X)

def angular_prob2(the, pee):
    f_lm = np.sqrt(np.math.factorial((2*l + 1)*(l-m))/(4*np.pi*np.math.factorial(l+m)))*lpmv(m, l, np.cos(the))
    g_m = np.exp(np.imag(m*pee))
    #print(g_m)
    Y_lm = np.outer(g_m, f_lm[0])
    return np.abs(Y_lm)**2
angular_prob2(theta, phi)[0][0]
probability = radial_wave_function_prob(r)*angular_prob2(theta, phi)[0][0]
def probability_spherical(r, theta, phi):
    raidial_component = radial_wave_function(r)
    f, g = angular_function(theta, phi)
    Y_lm2 = angular_prob(theta, phi)
    return Y_lm2
#probability = probability_spherical(r, theta, phi)

fig = plt.figure()
plt.imshow(probability.T, extent=[-15, 15, -15, 15], interpolation='none', origin='lower')
plt.xlabel('x')
