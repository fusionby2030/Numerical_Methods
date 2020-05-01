import pandas as pd
import matplotlib.pyplot as plt
from fastfouriertransform import FFT()
from matplotlib.ticker import FormatStrFormatter
import numpy as np 
plt.style.use('dark_background')
plt.rcParams['image.cmap'] = 'plasma'


# Create a sinc function to operate on numpy arrays
def sinc(x):
    if (x != 0):
        # Prevent divide-by-zero
        return np.sin(np.pi * x) / (np. pi * x)
    else:
        return 1
sinc = np.vectorize(sinc)

amplitude    = 1   # Volt / sqrt(micron)
slitWidth    = 2.5   # microns
wavelength   = 0.532 # microns
propDistance = 3017 # microns

x = np.arange(-10000, 10000, 1)
F = sinc(slitWidth * x / wavelength / propDistance)
I = amplitude / (wavelength * propDistance) * (slitWidth * F)**2
"""
Single Slit: Before FFT
plt.plot(x, I, linewidth = 2)
plt.xlim((-5000, 5000))
plt.xlabel(r'Position in observation plane, $\mu m$')
plt.ylabel('Power density, $V^2 / \mu m$')
plt.grid(True)
plt.show()
"""

x     = np.linspace(-50, 50, num = 1024)
field = np.zeros(x.size, dtype='complex128') # Ensure the field is complex

field[np.logical_and(x > -slitWidth / 2, x <= slitWidth / 2)] = amplitude + 0j

dx = x[1] - x[0] # Spatial sampling period, microns
fS = 1 / dx      # Spatial sampling frequency, units are inverse microns
f  = (fS / x.size) * np.arange(0, x.size, step = 1) # inverse microns

diffractedField = dx * FFT(FFT(np.roll(field+len(field)/2)) # The field must be rescaled by dx to get the correct units
fisze = int(f.size/2)
xPrime   = np.hstack((f[-fisze:] - fS, f[0:fisze])) * wavelength * propDistance

IrradTheory = amplitude / (wavelength * propDistance) * \
    (slitWidth * sinc(xPrime * slitWidth / wavelength / propDistance))**2
IrradFFT    = FFT(np.roll(diffractedField * np.conj(diffractedField))) / wavelength / propDistance


""" Singel Slit FFT VS THEORY
ax3 = plt.subplot(212)
ax3.plot(xPrime, np.abs(IrradFFT), '.', label = 'FFT')
ax3.plot(xPrime, IrradTheory, label = 'Theory')
ax3.set_xlim((-2000, 2000))
ax3.set_xlabel(r'x-position, $\mu m$')
ax3.set_ylabel(r'Power density, $V^2 / \mu m$')
ax3.grid(True)
ax3.legend()

ax0 = plt.subplot(221)
ax0.plot(xPrime, np.abs(IrradFFT), '.', label = 'FFT')
ax0.plot(xPrime, IrradTheory, label = 'Theory', linewidth = 2)
ax0.set_xlim((-500, 500))
ax0.set_ylim((0.0025, 0.0043))
ax0.set_xlabel(r'x-position, $\mu m$')
ax0.set_ylabel(r'Power density, $V^2 / \mu m$')
ax0.grid(True)

ax1 = plt.subplot(222)
ax1.plot(xPrime, np.abs(IrradFFT), '.', label = 'FFT')
ax1.plot(xPrime, IrradTheory, label = 'Theory', linewidth = 2)
ax1.set_xlim((-2250+800, -1750+800))
ax1.set_ylim((0.000, 0.0004))
ax1.set_xlabel(r'x-position, $\mu m$')
ax1.grid(True)
ax1.legend()

plt.tight_layout()
plt.savefig('thoeryvsnum.png')
plt.show()
"""
