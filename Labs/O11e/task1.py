import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

import numpy as np


def fit_curvefit(datax, datay, f):
    pfit, pcov = \
        curve_fit(f, datax, datay, )
    error = []
    for i in range(len(pfit)):
        try:
            error.append(np.absolute(pcov[i][i]) ** 0.5)
        except:
            error.append(0.00)
    pfit_curvefit = pfit
    perr_curvefit = np.array(error)
    return pfit_curvefit, perr_curvefit


def malus_model(theta, I_0=1):
    # theta = np.pi*theta/180
    return I_0 * np.cos(theta) ** 2


pa_list = [0, 15, 30, 45, 60, 75, 90]
linpol_df = pd.read_csv('data/Set2/LINPOL2.dat', sep='\t', header=0)
angles = np.array(linpol_df['Angle'])
zero_wave = np.array(linpol_df['0'])
angles_for_fit = angles * np.pi / 180

# Find Intensity_0
wave_to_fit = np.array(linpol_df['15'])
m_fit, m_err = fit_curvefit(angles_for_fit, zero_wave, malus_model)
print("\n# Intensity")
print("pfit = ", m_fit)
print("perr = ", m_err)
I_0 = m_fit[0]

"""
# Zero Angle 
plt.plot(angles, wave_to_fit, label='Data')
plt.plot(angles, malus_model(angles_for_fit, *m_fit), label='Fit')
plt.xlabel('Angles')
plt.ylabel('Intensity')
plt.title('0 Angle Quarter Wave Plate ')
plt.legend()
plt.tight_layout()
plt.show()
"""


def circular_model(theta, alpha, phi):
    """
    :param theta: analyser angle and vertical
    :param alpha: angle between polarization direction and vertical
    :param phi: angle between wave plate and vertical
    :return: Function for Intensity
    """
    return I_0 / 2 * (1 + np.cos(2 * (theta - phi)) * np.cos(2 * (alpha - phi)))

phi = 45
adjustment = 15
one_wave = np.array(linpol_df[str(phi)])
angle_to = phi - adjustment


"""
Plotting
fig, axs = plt.subplots(1, 2, sharex=True, constrained_layout=True)
axs[0].plot(angles, one_wave, label='Measured')
axs[1].plot(angles, circular_model(angles_for_fit,  * np.pi / 180,  angle_to * np.pi / 180), label='Theory', c='red')
axs[0].legend()
axs[1].legend()
axs[0].set_ylabel('Intensity')
fig.text(0.5, 0.01, 'Analyser Angle', ha='center')
# fig.text(0.04, 0.5, 'Intensity', va='center', rotation='vertical')
fig.suptitle('Measured VS Theory (angle = {})'.format(phi))
# plt.tight_layout()
plt.show()
"""