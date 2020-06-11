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
    return pn1 + pn2 + wfn1

radial_prob_super = radial_superposition(np.linspace(0,40,200), 3, 4)
radial_porb_array = radial_wave_function_prob(np.linspace(0,40,200), n = 3)
radial_1d = radial_wave_function(np.linspace(0,40,200), n=3)
radial_4 = radial_wave_function(np.linspace(0,40,200), n = 4)
n4_prob = radial_wave_function_prob(np.linspace(0,40,200), n = 4)
superposition = radial_1d + radial_4
fig, axs = plt.subplots(1,2)
axs[0].plot(np.linspace(0,40,200), radial_1d, label='n = 3')
axs[1].plot(np.linspace(0,40,200), radial_porb_array, label='n = 3')
axs[0].plot(np.linspace(0, 40, 200), radial_4, label='n = 4')
axs[1].plot(np.linspace(0,40,200), n4_prob, label='n = 4')
axs[0].plot(np.linspace(0, 40, 200), superposition, label='Superposition')
axs[1].plot(np.linspace(0,40,200), radial_prob_super, label='Superposition')
axs[1].legend()
axs[1].set_title('Probability Density vs R')
axs[0].set_xlabel('R (radius)')
axs[1].set_xlabel('R (radius)')
axs[0].legend()
axs[0].set_title('Wavefunction vs R')
axs[0].set_ylabel('Amplitude')
fig.tight_layout()
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/superposition1.png')
