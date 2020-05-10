import numpy as np
import matplotlib.pyplot as plt



SMALL_SIZE = 10
MEDIUM_SIZE = 12
BIGGER_SIZE = 20


plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)

plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'

""" Single Electron Orbit """

def radius_n(n, Z):
    a_0 = (0.0529e-9)
    return (a_0*((n**2)))/Z
def energy_n(n, Z):
    Z_1 = 13.6
    return -Z_1*(Z**2)/(n**2)
energy_n(5, 1)
energy_n(4, 1)
radius_n(100000000001, 1) - radius_n(100000000000, 1)
a_0*(2*100000000000 +1)

quant_r1n = np.arange(1, 21)
quant_r2n = np.arange(2, 22)


r1_rs = np.array([radius_n(r1, 1) for r1 in quant_r1n])
r2_rs = np.array([radius_n(r2, 1) for r2 in quant_r2n])

e1_hy = np.array([energy_n(n1, 1) for n1 in quant_r1n])
e2_hy = np.array([energy_n(n2, 1) for n2 in quant_r2n])
difference_energy = e2_hy - e1_hy
len(r2_rs)
len(r1_rs)
difference_r = r2_rs - r1_rs

def plot_varying_atoms_radius():
    atomic_numbers = np.arange(1, 9)
    quant_r1n = np.arange(1, 1001)
    quant_r2n = np.arange(2, 1002)
    for Z in atomic_numbers:
        r1_rs = np.array([radius_n(r1, Z) for r1 in quant_r1n])
        r2_rs = np.array([radius_n(r2, Z) for r2 in quant_r2n])
        difference = r2_rs - r1_rs
        plt.plot(quant_r1n, difference, label='Z: {}'.format(Z))
    plt.legend()
    plt.xlabel('Quantum Numbers N')
    plt.ylabel('detla R')
    plt.title('Distance between adjacent Electron Orbits for Z: 1-8')
    plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/radiustrans')
plot_varying_atoms_radius()
def plot_varying_atoms_energy():
    atomic_numbers = np.arange(1, 9)
    quant_r1n = np.arange(1, 30)
    quant_r2n = np.arange(2, 31)
    for Z in atomic_numbers:
        r1_rs = np.array([energy_n(r1, Z) for r1 in quant_r1n])
        r2_rs = np.array([energy_n(r2, Z) for r2 in quant_r2n])
        difference = r2_rs - r1_rs
        #logdiff = np.log(difference)
        plt.plot(quant_r1n, difference, label='Z: {}'.format(Z))
    plt.plot(quant_r1n, np.log(1/(quant_r1n**3)), label='n**-3', linewidth=4)
    plt.legend(loc='upper right')
    plt.xlabel('Quantum Numbers N')
    plt.ylabel('log(delta E)')
    plt.title('Energy of Transition between adjacent Electron Orbits for Z: 1-8')
    #plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/energytrans')
plot_varying_atoms_energy()
"""When an hydrogen electron absorbs ultriviolet light with lambda = 100e-9 """
"""
h = 6.626e-34 m2 kg/s
Change in energy = h/lambda = -13.6(n_final**2) - -13.6(n_initial**2)
Eph = h/
"""
c = 300000
h = 6.626e-34
h_in_evnm = 1240

lamb = 100e-9
lambnm = 100
freq = c/lamb
E_incoming = h_in_evnm/lambnm
ground = energy_n(1,1)
