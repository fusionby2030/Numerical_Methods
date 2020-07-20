import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
blue = '#34c3eb'


def coef(x, y):
    """
    Determine the Coefficients for the divided difference formula

    """
    x.astype(float)
    y.astype(float)
    n = len(x)
    a = [value for value in y]
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i] - a[i-1])/float(x[i]-x[i-j])
    return np.array(a)

input = np.array([5, 7, 11, 13, 17])
output = np.array([150, 392, 1452, 2366, 5205])
[value for value in input]
def evaluate_coef(a, x, r):
    n = len(a) - 1
    cache = a[n] + (r-x[n])
    for i in range(n-1, -1, -1):
        cache *= (r-x[i])
        cache += a[i]
    return cache
coefficients = coef(input, output)
evaluate_coef(coefficients, input, 10)
x_value = np.linspace(5, 20, num = 100)
problem1 = lambda x: 150 +121*(x - 5) + 24*(x-5)*(x-7) + (x-5)*(x-7)*(x-11) + 0.001041*(x-5)*(x-7)*(x-11)*(x-13)
problem1(10)
plt.plot(x_value, problem1(x_value), label='Interpolation')
plt.scatter(input, output, color=pink, label='Dataset')
plt.scatter(10, problem1(10), color=gold, label='f(10) = {}'.format(problem1(10)))
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Problem 1 - Newton Divided Difference')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/newtpr1.png')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Numerical_Methods/HW_07/files/newtpr1.png')

"""
Problem 2
"""
inputs = np.array([0, 10, 15, 20, 25, 30])
outputs = np.array([0, 227.04, 362.78, 517.35, 701.37, 901.67])
co2 = coef(inputs, outputs)
firstord = lambda x: co2[0] + co2[1]*(x)
secondord = lambda x: co2[0] + co2[1]*x + co2[2]*(x)*(x-10)
x_values = np.linspace(0, 30)
firstord(16)
secondord(16)
plt.plot(x_values, firstord(x_values), label='First Order')
plt.plot(x_values, secondord(x_values), label='Second Order')
plt.scatter(inputs, outputs, color=pink, label='Measurements')
plt.scatter(27.5, secondord(27.5), color=green, label='v(27.5) = {0:.4g}'.format(secondord(27.5)))
plt.legend()
plt.xlabel('time')
plt.ylabel('velocity')
plt.title('Rocket Velocity')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/rocket.png')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Numerical_Methods/HW_07/files/rocket.png')
