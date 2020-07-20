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
""" probability and wave functions for R and Y_lm   """
def radial_wave_function(r, n):
    const1 = np.sqrt(((2/(n*a_0))**3)*(np.math.factorial(n-l-1)/(2*n*np.math.factorial(n+l))))
    const2 = genlaguerre(n-l-1, 2*l+1)(2*r/(n*a_0))
    expon = np.exp(-r/(n*a_0))
    other = ((2*r)/(n*1_0))**l
    return const1*expon*other*const2
def hrwfp(r, n, l, m):
    const1 = np.sqrt(((2/(n*a_0))**3)*(np.math.factorial(n-l-1)/(2*n*np.math.factorial(n+l))))
    const2 = genlaguerre(n-l-1, 2*l+1)(2*r/(n*a_0))
    expon = np.exp(-r/(n*a_0))
    other = ((2*r)/(n*a_0))**l
    #f_lm = np.sqrt(np.math.factorial((2*l + 1)*(l-m))/(4*np.pi*np.math.factorial(l+m)))*lpmv(m, l, theta)
    #g_m = np.exp(m*phi*1j)
    #Y_lm = np.outer(g_m, f_lm)
    return ((4*np.pi*(r**2))*(const1*expon*other*const2)**2)
def angular_function(theta, phi):
    f_lm = np.sqrt(np.math.factorial((2*l + 1)*(l-m))/(4*np.pi*np.math.factorial(l+m)))*lpmv(m, l, np.cos(theta))
    g_m = np.exp(np.imag(m*phi))
    Y_lm = np.outer(g_m, f_lm)
    return Y_lm
def hydrogen_angular_prob(the, pee, n, l, m):
    f_lm = np.sqrt(np.math.factorial((2*l + 1)*(l-m))/(4*np.pi*np.math.factorial(l+m)))*lpmv(m, l, np.cos(the))
    g_m = np.exp((m*pee*1j))
    g_conjugate = np.exp((m*pee*(-1j)))
    Y_lm = np.outer(g_m, f_lm)
    Y_lmconj = np.outer(g_m, f_lm)
    #print(f_lm)
    #print(g_m)
    #print(np.abs(Y_lm)**2)
    return np.abs(Y_lm*Y_lmconj)

"""  Plotting """

""" Angular Probability Distribution"""
def plot_angular_surface(n, l, m):
    #Discritise Angle Vectors
    theta = np.linspace(-np.pi, np.pi, num=200)
    phi = np.linspace(0, 2*np.pi, num=200)
    #Create Probability Matrix
    rho = hydrogen_angular_prob(theta, phi, n, l, m)
    #Discritize x y and z values
    xs = rho*np.outer(np.cos(phi), np.sin(theta))
    ys = rho*np.outer(np.sin(theta), np.sin(phi))
    zs = rho*np.outer(np.ones(np.size(theta)), np.cos(theta))

    #plot
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm

    color_map = cm.magma #Can change colors here
    scalarMap = cm.ScalarMappable(norm=plt.Normalize(vmin=np.min(rho), vmax=np.max(rho)), cmap=color_map)
    C = scalarMap.to_rgba(rho)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xs, ys, zs, rstride=2, cstride=2, color='b', facecolors=C)
    ax.set(title='Hydrogen Atom, n={}, l={}, m={}'.format(n, l, m),
           xlabel='x',
           ylabel='y',
           zlabel='z')
    ax.view_init(40, 35)
    plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/EP4/HW_07/files/hangdist{}{}{}conj.png'.format(n, l, m))
    plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/hangdist{}{}{}conj.png'.format(n, l, m))


""" Radial plot """
def plot_radial_component(n, l, m):
    r = np.linspace(0, 25, num = 500)
    plt.plot(r, hrwfp(r, n, l, m))
    plt.xlabel('r')
    plt.ylabel('Probability Amplitude')
    plt.title('Hydrogen Radial Probability for n={}, l={}, m={}'.format(n, l, m))
    plt.savefig('hradial1d{}{}{}.png'.format(n,l,m))


def plot_radial_surface(n, l, m):
    x, y = np.linspace(-30, 30, num=500), np.linspace(-30, 30, num=500)
    X, Y = np.meshgrid(x, y)
    r_prob = hrwfp(r, n=3, l=1, m=0)
    ang_prob
    fig = plt.figure()
    plt.imshow(r_prob.T, extent=[-R, R, -R, R], interpolation='none', origin='lower')
    plt.xlabel('x')
    plt.ylabel('y')



def cartesian2spherical(x, y, z):
    """
    Convert cartesian coordinates to Spherical coordinates
    --------
    Parameters
    --------
    x, y, z: array of same size representing the position coorinates
    --------
    Output
    --------
    r, theta, phi: arrays representing the sphereical coordinates
    """
    r = np.sqrt(x*x + y*y + z*z)
    theta = np.arctan(np.sqrt(x*x + y*y)/z)
    phi = np.arctan(y/x)
    return r, theta[0][0], phi
if __name__ == "__main__": #https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    plot_angular_surface(3, 2, 0)
