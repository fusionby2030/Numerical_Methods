import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift, rfft, fftfreq#FFT SHIFTS


SMALL_SIZE = 5
MEDIUM_SIZE = 22
BIGGER_SIZE = 10


plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=SMALL_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)

plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
inductive4p0 = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task4_S1/S04p0.dat', header=3, sep='\t',names=['Time', 'Voltage'])
inductive4p0f = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task4_S1/S04p0f.dat', header=3, sep='\t',names=['Frequency', 'dBu'])
inductive4p5 = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task4_S1/S04p5.dat', header=3, sep='\t',names=['Time', 'Voltage'])
inductive4p5f = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task4_S1/S04p5f.dat', header=3, sep='\t',names=['Frequency', 'dBu'])
"""
Determine for about eight distances between the coupling coils the frequenciesf+andf−;
determine the frequencyf0of the uncoupled resonant circuit.
Calculate the coupling factorkLas well asthe mutual inductanceM.
PlotMas a function of distancedbetween the coils and discuss the result.
Tothis end fit a general power lawM∝d−nto the data.
Is the exponentncompatible with the axial fielddistribution of a circular coil (experiment E7e)?
"""

#Frequencies f+ and f- are the two local maximums in each graph

#Coupling factor is
cache = amplitude1
max1 = np.max(cache)
cache[cache.argmax()] = -100
max2 = np.max(cache)
amplitude1 = inductive4p0f['dBu'].to_numpy()
trial = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task4_S1/S14p0f.dat', header=3, sep='\t',names=['Frequency', 'dBu'])
trial
from scipy.signal import find_peaks

def findfreqs(filename):
    if filename == 'S12p0f' or filename == 'S16p0f':
        df = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task4_S1/{}.dat'.format(filename), header=3, sep=',',names=['Frequency', 'dBu'])
    else:
        df = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task4_S1/{}.dat'.format(filename), header=3, sep='\t',names=['Frequency', 'dBu'])
    cache1 = df['dBu'].to_numpy()
    cache2 = df['Frequency'].to_numpy()
    f_p = f_n = 0
    rel_ex = find_peaks(cache1, height = -22)
    #print(rel_ex)
    if len(rel_ex[0]) == 1:
        f_p = f_n = cache2[rel_ex[0][0]]
    else:
        f_p, f_n = cache2[rel_ex[0][0]], cache2[rel_ex[0][1]]
    return f_p, f_n
#f_p, f_n = findfreqs('S04p0f')
#Frequency 0 is sqrt 1 + m/l all over sqrt c(L+M)
def findfreq_0(freq_p, C=1, L=1):
    f_0 = 0.0
    f_0 = 1/np.sqrt(L*C)
    return f_0
def find_kl(f_p, f_n, f_0):
    kl = 0.0
    kl = (f_n - f_p)/f_0
    return kl
def findM(kl, L=5):
    M = 0.0
    M = kl*L
    return M

#f_p, f_n = findfreqs('S04p0f')
D_array = [4, 4.5]
#filenamelist = ['S04p0f','S04p5f']
for i in range(5, 10):
    #filenamelist.append('S0{}p0f'.format(i))
    D_array.append(int(i))

for j in range(10, 31, 2):
    #filenamelist.append('S{}p0f'.format(j))
    D_array.append(int(j))
D_array

def plotMvsD(M_array, D_array):
    plt.plot(D_array, M_array)

M_array = []
print(filenamelist)
for file in filenamelist:
    f_p, f_n = findfreqs(file)
    f_0 = findfreq_0(f_p)
    kl = find_kl(f_p, f_n, f_0)
    M = findM(kl)
    M_array.append(M)
print(M_array)

import scipy as sci

def func(x, a, b, c):
    return a * np.exp(-b * np.asarray(x)) + c

popt, popc = sci.optimize.curve_fit(func, D_array, M_array)

func(D_array, *popt)
