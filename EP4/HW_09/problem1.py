import numpy as np
A = 1.2/(np.pi)
a = 1.5
wf = lambda r: A*np.exp(-(r*r)/(2*a*a))
prob = lambda r: A*np.exp(-(r*r)/(2*a*a))*A*np.exp(-(r*r)/(2*a*a))*(4*np.pi*r*r)
expec = lambda r: (4*np.pi*A**2)*(np.exp(-(r**2)/(a**2)))*(r**3)

import scipy.integrate as integrate
result = integrate.quad(expec, 0, np.inf)[0]
expected = 2*np.pi*A*A*a*a

r_domain =  np.linspace(0, 5, num=200)
exp_mean = np.sum(prob*r_domain)
pa = (4*np.pi*r_domain*r_domain)*wf(r_domain)*wf(r_domain)
result_y = (4*np.pi*expected*expected)*wf(expected)*wf(expected)
""" Plotting """
import matplotlib.pyplot as plt
plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
orange = '#eb5834'
fig, ax = plt.subplots()
ax.plot(r_domain, pa, label='Probability Amplitude')
ax.vlines(expected, 0, result_y, color=green , label='<r>={0:.4g}'.format(expected))
ax.vlines(r_domain[pa.argmax()], 0, np.max(pa), label='Max' ,color=pink)
ax.set_xlabel('r/a')
ax.set_ylabel('r^2 Psi ^2')
ax.legend()
plt.title('a = 1.5, A = 1.2/pi')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/problem1.png')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/EP4/HW_09/files/problem1.png')
