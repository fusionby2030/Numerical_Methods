import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')
pink = '#F08080'
green = '#96f542'

plt.plot(np.linspace(0,5), f(np.linspace(0,5)))
plt.scatter(root, 0, color=pink)
plt.grid(True)

""" Bisection Method """

f = lambda x: x**3 + 2*x**2 + 10*x - 20
def bisection(f, lower, upper, max_iters=50, tolerance=1e-5):

    steps_taken = 0

    while steps_taken < max_iters:
        m = (lower + upper) / 2.0

        if m == 0 or abs(upper-lower) < tolerance:
            return m, steps_taken
        if f(m) > 0:
            upper = m
        else:
            lower = m

        steps_taken += 1

    final_estimate = (lower + upper) / 2.0
    return final_estimate, steps_taken


root, steps = bisection(f, 1, 8)

"""
Newton Raphson Method
"""
f = lambda x: 4*x**2 - 10*x - 30
fprime = lambda x: 8*x - 10
#if we do not know the derivative
def discrete_method_approx(f, x, h=.00000001):
    return (f(x+h) - f(x)) / h

def newton_raphson(f, x, tolerance=.001):
    steps_taken = 0

    while abs(f(x)) > tolerance:
        #df = discrete_method_approx(f, x)
        x = x - f(x)/fprime(x)
        steps_taken += 1
    return x, steps_taken
root, steps = newton_raphson(f, 8)

"""
Secant Method
"""
def secant_method(f, x0, x1, max_iter=100, tolerance = 1e-5):
    steps_taken = 1
    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) )
        x1, x0 = x2, x1
        steps_taken += 1
    return x2, steps_taken



root, steps = secant_method(f, 2, 8)



"""
Muellers Method
"""
import math
def Muller(a, b, c, f, MAX_ITERATIONS):

    res = 0;
    i = 0;

    while (True):
        # Calculating various constants
        # required to calculate x3
        f1 = f(a); f2 = f(b); f3 = f(c);
        d1 = f1 - f3;
        d2 = f2 - f3;
        h1 = a - c;
        h2 = b - c;
        a0 = f3;
        a1 = (((d2 * pow(h1, 2)) -
               (d1 * pow(h2, 2))) /
              ((h1 * h2) * (h1 - h2)));
        a2 = (((d1 * h2) - (d2 * h1)) /
              ((h1 * h2) * (h1 - h2)));
        x = ((-2 * a0) / (a1 +
             abs(math.sqrt(a1 * a1 - 4 * a0 * a2))));
        y = ((-2 * a0) / (a1 -
            abs(math.sqrt(a1 * a1 - 4 * a0 * a2))));

        # Taking the root which is
        # closer to x2
        if (x >= y):
            res = x + c;
        else:
            res = y + c;

        # checking for resemblance of x3
        # with x2 till two decimal places
        m = res * 100;
        n = c * 100;
        m = math.floor(m);
        n = math.floor(n);
        if (m == n):
            break;
        a = b;
        b = c;
        c = res;
        if (i > MAX_ITERATIONS):
            print("Root cannot be found using",
                            "Muller's method");
            break;
        i += 1;
    return res, i

# Driver Code
a = 0;
b = 1;
c = 2;
root, step = Muller(a, b, c, f, 100)
