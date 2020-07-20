"""
Use Lagrange's formula to interpolate the following function
f(x) = 1/ 1+2x*x
with give equally spaed points between -1 and 1
"""
import numpy as np

"""
Lagrange polynomial:
    N degree polynomial for discrete points xi, i = 0, 1, N
    multiply each yi

Determine Coefficients
"""
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
    """
    input
        domain: array or list of the domain to fill interpolated function
        x_values: array or list of given data to interpolate over
    return
        sum: array of size domain that represents the range of the domain after interpolation
    """
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
#Cheb Roots
cheb_roots = np.array([np.cos(np.pi*(2*k-1)/(2*n)) for k in range(1, n+1)])

""" Plotting  """
import matplotlib.pyplot as plt
plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
orange = '#eb5834'

domain = np.linspace(-1.2, 1.2, num=200)

f = lambda x: 1/(1+2*x*x)
x_range = np.linspace(-1, 1, num=5)
x_range2 = np.linspace(-1, 1, num=10)

n = 10
x_cheb = np.array([np.cos(np.pi*(2*k-1)/(2*n)) for k in range(1, n+1)])

fig, ax = plt.subplots(2)
#ax[0].plot(domain, polynomial(domain, x_range, f(x_range)), label='xi = {}'.format(x_range))
ax[0].plot(domain, polynomial(domain, x_range2, f(x_range2)), label='xi = {}'.format(np.around(x_range2, 1)))
ax[0].plot(domain, polynomial(domain, x_cheb, f(x_cheb)), label='Cheb xi = {}'.format(np.around(x_cheb, 3)))
ax[0].plot(domain, f(domain), label='Real', color=pink)
#zoomed in
#ax[1].scatter(domain, polynomial(domain, x_range, f(x_range)), s=10, label='xi = {}'.format(x_range))
ax[1].scatter(domain, polynomial(domain, x_range2, f(x_range2)), s=10, label='xi := Evenly Spaced')
ax[1].scatter(domain, polynomial(domain, x_cheb, f(x_cheb)), s = 10, label='xi := Chebyshev Roots')
ax[1].plot(domain, f(domain), label='Real', color=pink)
ax[1].set_xlim(domain[10], domain[50])
ax[1].set_ylim(f(domain[0]), f(domain[50]))
ax[0].set_title('Lagrange Interpolation with Evenly Spaced vs Chebyshev Roots, N = 10')
plt.tight_layout()
#ax[0].legend()
ax[1].legend()
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Numerical_Methods/HW_08/files/lvscheb10.png')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/lvscheb10.png')
