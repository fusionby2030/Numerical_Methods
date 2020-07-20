import numpy as np

x = np.array([-1, 0, 1])
y = np.array([0, 1, 3])



import matplotlib.pyplot as plt

plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
p1 = lambda x: x*x + 2*x + 1
p2 = lambda x: 2*x + 1

plt.scatter(x, y, color=pink, label = 'Data Points')
plt.plot(np.linspace(-1, 0), p1(np.linspace(-1, 0)), label='p1')
plt.plot(np.linspace(0, 1), p2(np.linspace(0,1)), label='p2')
plt.axhline(0, color=green, lw = 1, ls='--')
plt.axvline(0, color=green, lw = 1, ls='--')
plt.title('Quadratic Spline')
plt.legend()
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/qspine')
