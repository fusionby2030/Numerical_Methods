"""
Taylor Expansions

say we have a function f(x)
and we want to 'linearize' the function into an approximation of linear terms
we can use the taylor series
"""

import numpy as np
np.random.seed(42)
b = np.random.rand(1)
a = np.random.rand(1)


def f(x, beta=b, alpha=a):
    return beta * np.cos(alpha * x)


inputs = np.linspace(-np.pi, np.pi , num=500)
outputs = f(inputs)


def tay_approx(x, beta=b, alpha=a):
    # 5th order taylor expansion
    return b - 0.5 * x * x * (a * a * b) + (1 / 24) * (b * a ** 4) * x ** 4 - (1 / 720) * (b * a ** 6) * (x ** 6)


aprox = tay_approx(inputs)

import matplotlib.pyplot as plt

plt.scatter(inputs, outputs, label='Data')
plt.plot(inputs, aprox, label='Fit', color='orange')
plt.title('bcos(ax) \n b={}, a={}'.format(b, a))
plt.legend()
plt.show()

"""
Now we want to find the values for the 
"""