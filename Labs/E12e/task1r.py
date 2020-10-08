import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

def fit_curvefit(datax, datay, f, bounds):
    pfit, pcov = \
        curve_fit(f, datax, datay, bounds=bounds)
    error = []
    for i in range(len(pfit)):
        try:
            error.append(np.absolute(pcov[i][i]) ** 0.5)
        except:
            error.append(0.00)
    pfit_curvefit = pfit
    perr_curvefit = np.array(error)
    return pfit_curvefit, perr_curvefit



res_df = pd.read_csv('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E12e/data/Task1R.dat', sep='\t', header=0)
freq, V = np.array(res_df['f (Hz)']) * np.pi * 2, np.array(res_df['V (mV)'])
V_in, V_out = np.array(res_df['X (mV)']), np.array(res_df['Y (mV)'])
V_tot = np.array(res_df['V (mV)'])

L = 35 / 1000
R_S = 12
C = 6.8e-6


def model_in(X, R = 1, delta = 1, omega0 = 1):
    freq1, V_tot1 = X
    return (V_tot1*R*L*delta*2) / (L*(4*delta**2 + (freq1**2 - 2*omega0**2 + omega0**4 / freq1**2)))

def model_in2(X, R=1, delta = 1):
    freq2, V_tot2 = X
    return (V_tot2*R*L*delta*2) / (4*L**2*delta**2 + (freq2*L - 1 / (freq2*C))**2)

def model_out(X, R = 1, delta = 1):
    freq3, V_tot = X
    return (V_tot * R * (freq3*L - 1 / (freq3*C))) / (4*L**2*delta**2 + (freq3*L - 1 / (freq3*C))**2)


in_fit, in_err = fit_curvefit((freq, V_tot), V_in / V_tot, model_in, bounds=([0,0], [np.inf, np.inf]))
print("\n # in-phase: R, Delta")
print(in_fit)
print(in_err)


in_fit2, in_err2 = fit_curvefit((freq, V_tot), V_in / V_tot, model_in2, bounds=([0, 0], [np.inf, np.inf]))
print("\n # in-phase: R, Delta")
print(in_fit2)
print(in_err2)

out_fit, out_err = fit_curvefit((freq, V_tot), V_out / V_tot, model_out, bounds=([0, 0], [np.inf, np.inf]))
print("\n # in-phase: R")
print(out_fit)
print(out_err)


# plt.scatter(freq, V_in)
# plt.scatter(freq, V_tot)
plt.scatter(freq, V_in / V_tot, label='In Phase Voltage')
# plt.plot(freq, model_in((freq, V_tot), *in_fit), label='In Fit', c='green')
plt.plot(freq, model_in2((freq, V_tot), *in_fit2), label='In Fit 2', c='orange')
plt.scatter(freq, V_out / V_tot, label='Out Phase Voltage')
plt.plot(freq, model_out((freq, V_tot), *out_fit), label='Out Fit', c='black')
plt.xlabel('Frequency (Hz)')
plt.ylabel('V_tot / X or Y [a.u]')
plt.title('Series RLC \n In-/Out-of-phase components of Voltage Drop across Resistor')
# plt.plot(freq, imag_part)
plt.legend()
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/E12e/data/seriesres.png')
plt.show()
