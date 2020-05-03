import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftshift, rfft #FFT SHIFTS
from scipy import signal
plt.style.use('dark_background')
pink = '#F08080'

df4 = pd.read_csv('./data/sin4.dat', header = 4, sep='\t',names=['Time', 'Voltage'])
#print(df4['Time'])
df4FT = pd.read_csv('./data/sin4f.dat', header = 4, sep='\t',names=['Time', 'Voltage'])


def sine_wave(f,overSampRate,phase,nCyl):
    """
    Generate sine wave signal with the following parameters
    Parameters:
    f : frequency of sine wave in Hertz
    overSampRate : oversampling rate (integer)
    phase : desired phase shift in radians
    nCyl : number of cycles of sine wave to generate
    Returns:
    (t,g) : time base (t) and the signal g(t) as tuple
    Example:
    f=10; overSampRate=30;
    phase = 1/3*np.pi;nCyl = 5;
    (t,g) = sine_wave(f,overSampRate,phase,nCyl)
    """
    fs = overSampRate*f # sampling frequency
    t = np.arange(0,nCyl*1/f-1/fs,1/fs) # time base
    g = np.sin(2*np.pi*f*t+phase) # replace with cos if a cosine wave is desired
    return (t,g) # return time base and signal g(t) as tuple

f = 44.5e3 #frequency = 10 Hz
overSampRate = 30 #oversammpling rate
fs = f*overSampRate #sampling frequency
phase = 0 #phase shift in radians
nCyl = 5 # desired number of cycles of the sine wave
t= df4['Time'].to_numpy()

g = [np.sin(2*np.pi*f*time) for time in t]

print((df4FT['Voltage']))
#Plot for Sin vs FFT Sin
NFFT=df4FT['Time'].size
X=(rfft(g,NFFT))
print(abs(X))
fig4, ax = plt.subplots(nrows=2, ncols=1) #create figure handle
fVals=np.arange(start = 0,stop = NFFT)/819



ax[1].plot(df4FT['Time'],df4FT['Voltage'])
ax[1].set_title('sin4f.dat')
ax[1].set_xlabel('Frequency (Hz)')
ax[1].set_ylabel('dBu')
ax[0].plot(fVals,(X), linewidth = 2, color=pink) # plot using pyplot library from matplotlib package
ax[0].set_title('Sine wave f='+str(f)+' Hz') # plot title
ax[0].set_xlabel('Frequency (HZ)') # x-axis label
ax[0].set_ylabel('Amplitude') # y-axis label
plt.tight_layout()
#plt.savefig('../Reports/data/sinewaveFFT.png')
plt.show()
