import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift, rfft, fftfreq#FFT SHIFTS


SMALL_SIZE = 20
MEDIUM_SIZE = 22
BIGGER_SIZE = 35

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
beat1 = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task3_Beat1/B0001p4.dat', header=3, sep='\t',names=['Time', 'Voltage'])
beat1f = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task3_Beat1/B0001p4f.dat', header=3, sep='\t',names=['Frequency', 'dBu'])
beat2 = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task3_Beat1/B0002.dat', header=3, sep='\t',names=['Time', 'Voltage'])
beat2f = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/Task3_Beat1/B0002f.dat', header=3, sep='\t',names=['Frequency', 'dBu'])


"""

Determine Beat Period from:
time trace
spectrum
and compare


"""

time1 = beat1['Time'].to_numpy()
volt1 = beat1['Voltage'].to_numpy()
freq1 = beat1f['Frequency'].to_numpy()
amplitude1 = beat1f['dBu'].to_numpy()
n = volt1.size
dx = time1[6] - time1[5]
max_amplitude = np.max(amplitude1)
frequency_at_max = freq1[np.where(amplitude1 == max_amplitude)]

""" Autocorrelation R(k)=1N∑nxnxn+k """
def serial_corr(wave, lag=1):
    n = len(wave)
    y1 = wave[lag:]
    y2 = wave[:n-lag]
    corr = np.corrcoef(y1, y2, ddof=0)[0, 1]
    return corr
serial_corr(volt1)
def autocorr(wave):
    lags = range(len(wave)//2)
    corrs = [serial_corr(wave, lag) for lag in lags]
    return lags, corrs
lags, corrs = autocorr(volt1)


timeshift = 3742
shifts = range(n//2)
shift1 = volt1
len(lags)
top_values = [max for max in corrs[3000:] if max > 0.99 ]
index = np.where(corrs == np.max(corrs[3000:]))[0]
lags[index[0]]*dx
period = time1[3742]
location = volt1[3742]
(2*np.pi)/frequency_at_max[0]

fig, axs = plt.subplots(3, figsize=(12,9))

axs[0].plot(time1, shift1, color=pink, linewidth=1)
axs[0].set_xlabel('Time (ms)')
axs[0].annotate('{0:8.4f} ms'.format(period), xy=(period, location), xytext=(period + 0.5, 1.5),
            arrowprops=dict(facecolor=green, shrink=0.0005),)
axs[0].set_title('BB=0001p4')
axs[1].plot(lags, corrs, color=green)
axs[1].set_xlabel('Lag (timestep)')
axs[1].set_title('Autocorrelation')
axs[2].plot(freq1, amplitude1)
axs[2].set_xlim(0, 50)
axs[2].annotate('{0:8.4f} kHz'.format(frequency_at_max[0]), xy=(frequency_at_max, max_amplitude), xytext=(frequency_at_max + 10, max_amplitude-15),
            arrowprops=dict(facecolor=pink, shrink=0.05),)
axs[2].set_xlabel('Freq (kHz)')
axs[2].set_title('Spectrum')

plt.tight_layout()
plt.savefig('Beat Analysis')
