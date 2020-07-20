import numpy as np

def lagrangecoeff(x, y, n):
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
    #print(lcoeffs)
    for i in range(N):
        cache_sum = np.ones_like(domain)*(lcoeffs[i])
        for j in range(N):
            if j == i:
                continue
            cache_sum *= domain - x_values[j]
        sum += cache_sum
    return sum

x_domain = np.linspace(3, 8, num=1000)
x_values = np.arange(3, 9)
y_values = np.array([0.205, 0.240, 0.259, 0.262, 0.250, 0.224])



x_domain_interp3 = np.linspace(1.65, 1.9)
x_domain3 = np.linspace(1.5, 2.2)
x_values3 = np.array([1.7, 1.74, 1.78, 1.82, 1.86])
y_values3 = np.array([0.9915, 0.9856, 0.9780, 0.9691, 0.9584])


approxvalue3 = polynomial(1.74, x_values3, y_values3)
new3 = -np.sqrt(1- approxvalue3*approxvalue3)

import matplotlib.pyplot as plt
plt.style.use('dark_background')
pink = '#F08080'
green = '#96f542'
gold = '#ebdb34'
orange = '#eb5834'

maxx = x_domain[np.argmax(polynomial(x_domain, x_values, y_values))]
max= np.max(polynomial(x_domain, x_values, y_values))
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color=pink, label='Data Points')
ax.plot(x_domain, polynomial(x_domain, x_values, y_values), label='Interpolation')
ax.scatter(maxx, max, color=gold,  label='Maximum ({:.3}, {:.3})'.format(maxx, max))
ax.legend()
plt.title('Problem 4')
plt.savefig('/home/fusionby2030/Uni_Ausgabe/Semester4/Labs/Reports/data/maxgraph.png')
