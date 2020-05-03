import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift, rfft, fftfreq#FFT SHIFTS


plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
dfpre1 = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task2_pre/pre11.dat', header=3, sep='\t',names=['Time', 'Voltage'])
dfpre2 = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task2_pre/pre12.dat', header=3, sep='\t',names=['Time', 'Voltage'])
dfpre1f = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task2_pre/pre11f.dat', header=3, sep='\t',names=['Frequency', 'dBu'])
dfpre1f = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task2_pre/pre12f.dat', header=3, sep='\t',names=['Frequency', 'dBu'])

"""
Coil and Capacitor:C  are in series
Voltage(Ua) measured accross capacitor

U_c = 1/2 q_0^2 C
"""
voltage1 = dfpre1['Voltage'].to_numpy()
time1 = dfpre1['Time'].to_numpy()
voltage2 = dfpre2['Voltage'].to_numpy()
time2 = dfpre2['Time'].to_numpy()
freq1 = dfpre1f['Frequency'].to_numpy()
dBu1 = dfpre1f['dBu'].to_numpy()
#freq2 = dfpre2f['Frequency'].to_numpy()
#dBu2 = dfpre2f['dBu'].to_numpy()

time1[1]-time1[0]
time1[2]-time1[1]
time1[3] - time1[2]


somex1 = time1
somey1 = voltage1
somex2 = time2
somey2 = voltage2
""" exponential modeling """
dx = time1[5] - time1[4]
dy = np.diff((1 -voltage1), prepend=0)/dx
threshold = 0.00005
indexes = np.where(dy == 0)

B = (voltage1[indexes[0][0]])/(voltage1[indexes[0][1]])
delta = np.log(B)
P = (time1[indexes[0][1]]) - (time1[indexes[0][0]])
damping = (delta)/(np.sqrt(4*np.pi**2 + delta**2))
natural = (delta)/(period*damping)
of = (2*np.pi)/(P)
equation1 = -12*np.exp(-damping*natural*time1)*np.sin(of*time1)

dx = time2[5] - time2[4]
dy = np.diff((1 -voltage2), prepend=0)/dx

indexes = np.where(dy == 0)
delta = np.log(B)
B = (voltage1[indexes[0][0]])/(voltage1[indexes[0][1]])
P = (time1[indexes[0][1]]) - (time1[indexes[0][0]])
damping = (delta)/(np.sqrt(4*np.pi**2 + delta**2))
natural = (delta)/(period*damping)
of = (2*np.pi)/(P)
equation2 = -12*np.exp(-damping*natural*time1)*np.sin(of*time1)
