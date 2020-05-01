import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.ticker import FormatStrFormatter
from fastfouriertransform import FFT()
filename = 'O17e_Data/ES1_2.csv'
df = pd.read_csv(filename, header=None)
lam = 636e-9
focal_length = .3017


#Graphs of FFT vs Intensity Profile
index, intensity = df[0].to_numpy(), df[1].to_numpy()

index  -= 1410
index = index*(7e-6)
x_values = index

index = index*(2*np.pi/(focal_length* lam))
yf = (np.abs(FFT(intensity)))
freq = FFT(len(index), index[1] - index[0])
indexes = []
n = int(len(yf) - 5)

""" Intensity Profile VS FFT
fig, axs = plt.subplots(1,2)
axs[0].plot(x_values, intensity)
axs[0].set_title('Intensity vs Pixel Width')
axs[1].plot(np.roll(freq, 250)[1:550], np.roll(yf, 250)[1:550])
axs[0].set_xlabel('Distance (m)')
axs[0].set_ylabel('Intensity')
axs[1].set_title('FFT')
axs[1].set_xlim(-0.00005, 0.00005)
axs[0].set_xlim(-0.005, 0.005)
axs[1].set_xlabel('Frequency (1/m)')

axs[1].ticklabel_format(axis='x', style='sci')
axs[1].tick_params(labelrotation=12)
axs[1].set_ylabel('Magnitude')
fig.subplots_adjust(wspace=0.3)
fig.savefig(filename.split('/')[1].split('.')[0] + 'graph.png')

plt.show()
"""
