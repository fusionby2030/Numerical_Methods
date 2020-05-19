
import matplotlib.pyplot as plt

SMALL_SIZE = 12
MEDIUM_SIZE = 15
BIGGER_SIZE = 20


plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=SMALL_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)

plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'

import numpy as np
def secant_method(f, x0, x1, max_iter=100, tolerance = 1e-5):
    steps_taken = 1
    iter_x, iter_y, iter_count = np.empty(0),np.empty(0),np.empty(0)
    i = 0

    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        i +=1
        x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) )
        iter_x = np.append(iter_x,x2)
        iter_y = np.append(iter_y,f(x2))
        iter_count = np.append(iter_count ,i)

        x1, x0 = x2, x1
        steps_taken += 1
    return x2, iter_x, iter_y, iter_count
f = lambda x: x**3 - 2*x - 5
root, iter_x, iter_y, iter_count = secant_method(f, 1, 4)



x = np.linspace(0, 4)
fig, axs = plt.subplots(1, figsize=(10,10))
axs.plot(x, f(x), label = 'x**3 - 2x - 5')
axs.set_ylim(-10, 10)
axs.set_xlim(1, 3)

axs.plot(iter_x,iter_y)
axs.scatter(iter_x, iter_y)
for i in range(len(iter_x)):
    plt.vlines(iter_x[i], ymin = 0, ymax = iter_y[i], color = pink)
    if i <  2:
        plt.text(iter_x[i], iter_y[i] + 6, 'x{}'.format(i +1), fontsize=15)
    if i == 2:
        plt.text(iter_x[i], iter_y[i] + 2, 'x{}'.format(i +1), fontsize=15)
    elif i < 5 and i > 2:
        plt.text(iter_x[i], iter_y[i] + 3, 'x{}'.format(i+1), fontsize=15)
    elif i == 5:
        plt.text(iter_x[i], iter_y[i] + 4, 'x{}'.format(i+1), fontsize=15)
    elif i == (len(iter_x) -1) :
        plt.text(iter_x[i], iter_y[i] -3, 'Root at x = {0:8.4f}'.format(iter_x[i]), fontsize=15)
axs.set_title('Secant Method: {} iterations'.format(len(iter_count)))
plt.legend()
plt.hlines(0, 0, 5, color = 'white')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Numerical_Methods/HW_04/secant1.png')
"""

"""
