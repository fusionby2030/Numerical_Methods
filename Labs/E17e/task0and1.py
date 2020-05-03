import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift, rfft, fftfreq#FFT SHIFTS
from scipy import signal
plt.style.use('dark_background')
pink = '#F08080'


df4 = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/sin4.dat', header = 4, sep='\t',names=['Time', 'Voltage'])
#print(df4['Time'])
df4FT = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/data/sin4f.dat', header = 4, sep='\t',names=['Frequency', 'dBu'])


x = df4['Time'].to_numpy()
y = df4['Voltage'].to_numpy()
print(y.size)



freq = df4FT['Frequency'].to_numpy()
spectrum = df4FT['dBu'].to_numpy()
spectrum.shape

"""
period is about every 20 samples
"""

sample_rate = 20000
sample_interval = 5e-5
no_samples = 10000


period = sample_interval*no_samples
df = 1/period
dw = 2*np.pi/(period)
print(period)
print(df)
print(dw)

sample_rate = 20000
sample_interval = 50e-5
no_samples = 100001
N = len(spectrum)
new_frequency = np.array([df*n for n in range(N)])*sample_interval


f2 = 2 #beat Freq
time_domain = np.linspace(-250, 250, no_samples)
f1 = f2
f1_wave = np.sin(f1*np.pi*2*time_domain)*np.cos(f2*np.pi*2*time_domain)
f1 = 10*f2
f2_wave = np.sin(f1*np.pi*2*time_domain)*np.cos(f2*np.pi*2*time_domain)
f2_wave
somey = (fft(f1_wave, 8189)[1:])
phasey = (fft(f2_wave, 8189)[1:])
f1 = f2
trial1 = np.sin(f1*np.pi*2*time_domain)*np.cos(f2*np.pi*2*time_domain)
trial2 = np.cos(f1*np.pi*2*time_domain)*np.sin(f2*np.pi*2*time_domain)
somey2 = (fft(trial1, 8189)[1:])
phasey2 = (fft(trial2, 8189)[1:])

N = len(somey)
new_frequency = np.array([df*n for n in range(N)])*sample_interval
somex = (new_frequency)

fig, axs = plt.subplots(2,2, sharey='row', gridspec_kw={'hspace': 0.3, 'wspace': 0}, figsize=(7,5))
axs[0,0].plot(somex, somey)
axs[0,0].set_ylabel('Amplitude')
axs[0,0].set_title('f1 = f2')
axs[0,0].set_xlim(0.1, 0.2)
axs[1,0].set_xlim(0.1, 0.2)
axs[0,1].plot(somex, phasey)
axs[0,1].set_title('f1 = 10f2 ')
axs[0,1].set_xlim(0.8, 1)

axs[1,1].set_xlim(0.1, 0.2)
axs[1,0].plot(somex, somey2)
axs[1,0].set_xlabel('Frequency (Hz)')
axs[1,0].set_ylabel('Amplitude')
axs[1,0].set_title('sin * cos ')
axs[1,1].plot(somex, phasey2)
axs[1,1].set_xlabel('Frequency (Hz)')
axs[1,1].set_title('cos * sin')

plt.tight_layout()
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E17e/freqsin.png')
plt.show()
