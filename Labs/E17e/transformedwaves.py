import numpy as np


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

def triangle_wave(f,overSampRate,phase,nCyl, num_coef):
    fs = overSampRate*f
    t = np.arange(0,nCyl*1/f-1/fs,1/fs)
    g = []
    for i in range(num_coef):
        n = 2*i +1
        pass
    return Shit

"""
Simulate a sinusoidal signal with given sampling rate
"""
import numpy as np
import matplotlib.pyplot as plt # library for plotting
from scipy.fftpack import fft, ifft, fftshift #FFT SHIFTS
from scipy import signal
plt.style.use('dark_background')
pink = '#F08080'


f = 10 #frequency = 10 Hz
overSampRate = 30 #oversammpling rate
fs = f*overSampRate #sampling frequency
phase = 1/3*np.pi #phase shift in radians
nCyl = 5 # desired number of cycles of the sine wave

t = np.arange(0,nCyl*1/f-1/fs,1/fs)

g = np.sin(2*np.pi*f*t+phase) -(np.sin(3*2*np.pi*fs*t+phase))/9.0 + (np.sin(5*2*np.pi*fs*t+phase))/25.0 - (np.sin(7*2*np.pi*fs*t+phase))/49.0


#Plot for Sawtooth Wave
x = signal.sawtooth(2*np.pi*f*t, 0.5)
print(x.size)
NFFT=1024

X=fftshift(fft(x,NFFT))
fig2, ax = plt.subplots(nrows=1, ncols=1) #create figure handle
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*fs/NFFT
ax.plot(fVals,np.abs(X))
ax.set_title('FFT of Sawtooth wave')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('|DFT Values|')
ax.set_xlim(-50,50)
ax.set_xticks(np.arange(-50, 50+10,10))
ax.plot(t, fVals, color=pink)
plt.tight_layout()
#plt.savefig('../Reports/data/squarewaveFFT.png')
plt.show()
"""
#PLOT ALL
fig2, ax = plt.subplots(nrows=2, ncols=3) #create figure handle
#Plot Sawtooth
x = signal.sawtooth(2*np.pi*f*t, 0.5)
NFFT=1024
X=fftshift(fft(x,NFFT))
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*fs/NFFT
ax[0,0].plot(t,x, linewidth = 2, color=pink) # plot using pyplot library from matplotlib package
ax[0,0].set_title('Sawtooth wave f='+str(f)+' Hz') # plot title
ax[0,0].set_xlabel('Time (s)') # x-axis label
ax[0,0].set_ylabel('Amplitude') # y-axis label
ax[1,0].plot(fVals,np.abs(X))
ax[1,0].set_title('FFT of Sawtooth wave')
ax[1,0].set_xlabel('Frequency (Hz)')
ax[1,0].set_ylabel('|DFT Values|')
ax[1,0].set_xlim(-50,50)
ax[1,0].set_xticks(np.arange(-50, 50+10,10))


#Plot for Square Wave
x = signal.square(2*np.pi*f*t)
X=fftshift(fft(x,NFFT))
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*fs/NFFT

ax[0,1].plot(t,x, linewidth = 2, color=pink) # plot using pyplot library from matplotlib package
ax[0,1].set_title('Square wave f='+str(f)+' Hz') # plot title
ax[0,1].set_xlabel('Time (s)') # x-axis label
ax[0,1].set_ylabel('Amplitude') # y-axis label
ax[1,1].plot(fVals,np.abs(X))
ax[1,1].set_title('FFT of Square wave')
ax[1,1].set_xlabel('Frequency (Hz)')
ax[1,1].set_ylabel('|DFT Values|')
ax[1,1].set_xlim(-50,50)
ax[1,1].set_xticks(np.arange(-50, 50+10,10))
#Plot for Sin vs FFT Sin
(t,x) = sine_wave(f,overSampRate,phase,nCyl) #function call
NFFT=1024
X=fftshift(fft(x,NFFT))
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*fs/NFFT

ax[0,2].plot(t,x, linewidth = 2, color=pink) # plot using pyplot library from matplotlib package
ax[0,2].set_title('Sine wave f='+str(f)+' Hz') # plot title
ax[0,2].set_xlabel('Time (s)') # x-axis label
ax[0,2].set_ylabel('Amplitude') # y-axis label
ax[1,2].plot(fVals,np.abs(X))
ax[1,2].set_title('FFT of Sine wave')
ax[1,2].set_xlabel('Frequency (Hz)')
ax[1,2].set_ylabel('|DFT Values|')
ax[1,2].set_xlim(-50,50)
ax[1,2].set_xticks(np.arange(-50, 50+10,10))
plt.tight_layout()
plt.savefig('../Reports/data/allFTT.png')
plt.show()

"""
"""
#Plot for Sawtooth Wave
x = signal.sawtooth(2*np.pi*f*t)
NFFT=1024
X=fftshift(fft(x,NFFT))
fig2, ax = plt.subplots(nrows=2, ncols=1) #create figure handle
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*fs/NFFT
ax[1].plot(fVals,np.abs(X))
ax[1].set_title('FFT of Sawtooth wave')
ax[1].set_xlabel('Frequency (Hz)')
ax[1].set_ylabel('|DFT Values|')
ax[1].set_xlim(-50,50)
ax[1].set_xticks(np.arange(-50, 50+10,10))
ax[0].plot(t,x, linewidth = 2, color=pink) # plot using pyplot library from matplotlib package
ax[0].set_title('Sawtooth wave f='+str(f)+' Hz') # plot title
ax[0].set_xlabel('Time (s)') # x-axis label
ax[0].set_ylabel('Amplitude') # y-axis label
plt.tight_layout()
#plt.savefig('../Reports/data/squarewaveFFT.png')
plt.show()

#Plot for Square Wave
x = signal.square(2*np.pi*f*t)
NFFT=1024
X=fftshift(fft(x,NFFT))
fig3, ax = plt.subplots(nrows=2, ncols=1) #create figure handle
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*fs/NFFT
ax[1].plot(fVals,np.abs(X))
ax[1].set_title('FFT of Square wave')
ax[1].set_xlabel('Frequency (Hz)')
ax[1].set_ylabel('|DFT Values|')
ax[1].set_xlim(-50,50)
ax[1].set_xticks(np.arange(-50, 50+10,10))
ax[0].plot(t,x, linewidth = 2, color=pink) # plot using pyplot library from matplotlib package
ax[0].set_title('Square wave f='+str(f)+' Hz') # plot title
ax[0].set_xlabel('Time (s)') # x-axis label
ax[0].set_ylabel('Amplitude') # y-axis label
plt.tight_layout()
plt.savefig('../Reports/data/squarewaveFFT.png')
plt.show()

#Plot for Sin vs FFT Sin
(t,x) = sine_wave(f,overSampRate,phase,nCyl) #function call
NFFT=1024
X=fftshift(fft(x,NFFT))
fig4, ax = plt.subplots(nrows=2, ncols=1) #create figure handle
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*fs/NFFT
ax[1].plot(fVals,np.abs(X))
ax[1].set_title('FFT of Sine wave')
ax[1].set_xlabel('Frequency (Hz)')
ax[1].set_ylabel('|DFT Values|')
ax[1].set_xlim(-50,50)
ax[1].set_xticks(np.arange(-50, 50+10,10))
ax[0].plot(t,x, linewidth = 2, color=pink) # plot using pyplot library from matplotlib package
ax[0].set_title('Sine wave f='+str(f)+' Hz') # plot title
ax[0].set_xlabel('Time (s)') # x-axis label
ax[0].set_ylabel('Amplitude') # y-axis label
plt.tight_layout()
plt.savefig('../Reports/data/sinewaveFFT.png')
plt.show()

"""
