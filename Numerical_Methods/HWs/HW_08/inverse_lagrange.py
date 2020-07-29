import numpy as np
#lagrange inverse formula
#Estimate a root for f(x) = 0
x_data = np.array([30, 34, 38, 43])
y_data = np.array([-30, -13, 3, 18])

def lagrangecoeff(x, y, n):
    """
    input
    x: array or list of x-values to interpolate
    n: index of x_value to interpolate on

    return:
    lagrange coefficient for given N and domain values to interpolate
    """
    indexed = x[n]
    denonimator = np.array([value for value in x if value != indexed])
    denonimator = indexed - denonimator
    coef = y[n]
    for value in denonimator:
        coef /= value

    return coef

def polynomial(domain, x_values, y_values):
    N = len(x_values)
    sum = np.zeros_like(domain)
    lcoeffs = [lagrangecoeff(x_values, y_values, _) for _ in range(0, N)]
    for i in range(N):
        cache_sum = np.ones_like(domain)*(lcoeffs[i])
        for j in range(N):
            if j == i:
                continue
            cache_sum *= domain - x_values[j]
        sum += cache_sum
    return sum

domain = 0.0

x_domain = np.linspace(30, 50)
import matplotlib.pyplot as plt
plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
orange = '#eb5834'

plt.plot(x_domain, polynomial(x_domain, x_data, y_data), label='Approximation')
plt.scatter(x_data, y_data, label='Data Points', color=gold)
plt.scatter(polynomial(0.0, y_data, x_data), 0.0, color=green, label='root = {:.2g}'.format(polynomial(0.0, y_data, x_data)))
plt.hlines(0, 30, 50, color=pink)
plt.title('Inverse Lagrange Root Finding')
plt.legend()
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Numerical_Methods/HW_08/files/invlagrange.png')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/invlagrange.png')
