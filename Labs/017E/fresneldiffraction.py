import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')
plt.rcParams['image.cmap'] = 'plasma'

filename = './O17e_Data/ES3_904b.csv'
newfilename = filename.split('/')[2].split('.')[0]

distance = int(newfilename.split('_')[1].split('b')[0])
print(distance)
df = pd.read_csv(filename, header=None)


plt.plot(np.arcsin((df[0]-1000)*(7e-6)), df[1])
plt.title(newfilename)
plt.xlabel('Distance')
plt.ylabel('Intensity')
plt.xlim(-0.0025, 0.0025)
plt.savefig('FresnelGraphs/{}'.format(newfilename) + '.png')
plt.show()
