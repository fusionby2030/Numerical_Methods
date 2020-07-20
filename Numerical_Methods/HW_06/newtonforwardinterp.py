import numpy as np

def calculate_u(u, n):
    cache = u
    for i in range(1,n):
        cache *= (u-i)
    return cache
n = 4
x = [0.0, 1.0, 2.0, 3.0]
y = np.zeros((n,n))
y[0][0] = 1.0
y[1][0] = 2.0
y[2][0] = 1.0
y[3][0] = 10.0
for i in range(1, n):
    for j in range(n-1):
        y[j][i] = y[j+1][i-1] - y[j][i-1]

value = 4.0
sum = y[0][0]
u = (value-x[0])/(x[1] - x[0])
for i in range(1, n):
    sum += (calculate_u(u, i)*y[0][i])
sum
