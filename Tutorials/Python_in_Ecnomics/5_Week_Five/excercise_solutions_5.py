"""
1

Time series
x(t+1) = ax(t) where a = 0.5, x0 = 0 , t = 0 -> T
"""

import numpy as np
import matplotlib.pyplot as plt

a = 0.5
T = 50
x = np.empty(T+1)
x[0] = 0
for t in range(T):
    x[t+1] = a*x[t]

plt.plot(x)
plt.show()


"""
2
samme function but three different a values 
a = 0, 0.8, 0.98
"""
T = 200
a_values = [0, 0.8, 0.98]
for value in a_values:
    x = np.empty(T+1)
    for t in range(T):
        x[t+1] = value*x[t]
    plt.plot(x, label='a = ' + str(value))
plt.legend()
plt.show()

"""
3

absolute value
"""

T = 200
a = 0.9
random_values = np.random.randn(200)
x = np.empty(T+1)
x[0] = 0
for t in range(T):
    x[t+1] = np.abs(x[t]) * a + random_values[t]

plt.plot(x)
plt.show()



"""
4
Using logic statements rewrite 3 
"""

T = 200
a = 0.9
random_values = np.random.randn(200)
x = np.empty(T+1)
for t in range(T):
    if x[t] < 0:
        x[t + 1] = -x[t] * a + random_values[t]
    else:
        x[t+1] = x[t] * a + random_values[t]

plt.plot(x)
plt.show()

"""
5 
Monte Carlo
Consider the circle of diameter 1 embedded in the unit square.

Let A be its area and let r=1/2 be its radius.

If we know π  then we can compute A via A=πr2

But here the point is to compute π , which we can do by π=A/r2


Summary: If we can estimate the area of a circle with diameter 1, then dividing by r2=(1/2)2=1/4
gives an estimate of π

We estimate the area by sampling bivariate uniforms and looking at the fraction that falls into the circl
"""

n = 100000

count = 0
for i in range(n):
    u, v = np.random.uniform(), np.random.uniform()
    d = np.sqrt((u - 0.5)**2 + (v - 0.5)**2)
    if d < 0.5:
        count += 1

area_estimate = count / n

print(area_estimate * 4)  # dividing by radius**2


