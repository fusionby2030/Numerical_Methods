import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
blue = '#34c3eb'


""" Viscosity """

given_x = [110, 130, 160, 190]
given_y = [10.8, 8.1, 5.5, 4.8]
viscapprox = lambda x: 10.8-(27.0/220)*(x-110) + (29.0/30000)*(x-110)*(x-130) - (7.0/3200000)*(x-110)*(x-130)*(x-160)
x_range = np.linspace(100, 200, num = 100)
plt.plot(x_range, viscapprox(x_range), label='Newton Approximation')
plt.scatter(given_x, given_y, color=pink, label='Given Points')
plt.scatter(140, viscapprox(140), color=gold, label='Estimate of T = 140')
plt.legend()
plt.xlabel('Temperature')
plt.ylabel('Viscosity')
plt.title('Newton Divided Difference Approximation ')

given_x = [654, 658, 659, 661]
given_y = [2.8156, 2.8182, 2.8189, 2.8202]
logapprox = lambda x: -(1.0/140)*(x-658)*(x-659)*(x-661)*(2.8156) +(1.0/12)*(x-654)*(x-659)*(x-661)*(2.8182) - (1.0/10)*(x-654)*(x-658)*(x-661)*(2.8189) + (1.0/42)*(x-654)*(x-658)*(x-659)*(2.8202)
x_range = np.linspace(652, 662, num = 100)
plt.plot(x_range, logapprox(x_range), label='Newton Approximation')
plt.plot(x_range, np.log10(x_range), color=green, label='Log base 10', linewidth=0.75)
plt.scatter(given_x, given_y, color=pink, label='Given Points')
plt.scatter(656, logapprox(656), color=gold, label='Estimate of x = 656')
plt.legend()
plt.xlabel('x')
plt.ylabel('log base 10')
plt.title('Lagrange Polynomial Approximation of log base 10')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Numerical_Methods/HW_06/files/log10trial.png')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/log10trial.png')
