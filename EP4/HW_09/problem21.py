import numpy as np

a_0 = 1 #atomic distance
#ground state hydrogen
hywave = lambda r: (1/(4*np.sqrt(2*np.pi)*a_0**(3.0/2)))*(2-(r/a_0))*np.exp(-r/(2*a_0))
#Expected
expected = lambda r: (1/(4*np.sqrt(2*np.pi)*a_0**(3.0/2)))*(2-(r/a_0))*np.exp(-r/(2*a_0))* (1/(4*np.sqrt(2*np.pi)*a_0**(3.0/2)))*(2-(r/a_0))*np.exp(-r/(2*a_0))*(4*np.pi*r**3)
#Inverse Expected
inverse = lambda r: (1/(4*np.sqrt(2*np.pi)*a_0**(3.0/2)))*(2-(r/a_0))*np.exp(-r/(2*a_0))* (1/(4*np.sqrt(2*np.pi)*a_0**(3.0/2)))*(2-(r/a_0))*np.exp(-r/(2*a_0))*(4*np.pi*r)
import scipy.integrate as integrate
result = integrate.quad(expected, 0, np.inf)
inverse_result = integrate.quad(inverse, 0, np.inf)
r_domain = np.linspace(0,15, num = 200)



pa = (4*np.pi)*r_domain*r_domain*hywave(r_domain)*hywave(r_domain)

result_y = a_0*(4*np.pi)*result[0]*result[0]*hywave(result[0])*hywave(result[0])
max_y = np.max(pa)
max_x = r_domain[pa.argmax()]
inverse_result_y = a_0*(4*np.pi)*inverse_result[0]*inverse_result[0]*hywave(inverse_result[0])*hywave(inverse_result[0])

import matplotlib
matplotlib.rcParams['text.usetex'] = False
import matplotlib.pyplot as plt

plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
orange = '#eb5834'

fig, ax = plt.subplots(2)
ax[0].set_title('Probility Amplitude')
ax[0].plot(r_domain/a_0, pa)
ax[0].vlines(max_x, 0, max_y, color=green, label='Max')
ax[0].vlines(result[0], 0, result_y, color=pink, label='Average Distance <r> = {0:.2}'.format(result[0]))
ax[0].vlines(inverse_result[0],0, inverse_result_y, label='Inverse Distance <1/r> = {0:.2}'.format(inverse_result[0]), color=gold )
ax[0].set_ylabel('r^2 R^2')
ax[1].plot(r_domain/a_0, hywave(r_domain))
ax[1].set_xlabel('r/a_0')
ax[1].set_ylabel('R')

ax[1].set_title('Wave Function')
ax[1].vlines(max_x, 0, hywave(max_x), color=green, label='Max')
ax[1].vlines(result[0], 0, hywave(result[0]), color=pink, label='Average Distance <r> = {0:.2}'.format(result[0]))
ax[1].vlines(inverse_result[0],0, hywave(inverse_result[0]), label='Inverse Distance <1/r> = {0:.2}'.format(inverse_result[0]), color=gold)
ax[1].hlines(0, 0, 15, color=orange)
ax[1].legend()
ax[0].legend()
plt.tight_layout()
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/problem21.png')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/EP4/HW_09/files/problem21.png')
