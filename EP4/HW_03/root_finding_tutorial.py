""" Root Finding Algorithms """

"""
https://docs.scipy.org/doc/scipy/reference/optimize.html
For just quick root finding, one can use the scipy.optimize library
"""
f = lambda x: x**2 - 20

""" lambda arguments : expression """
x = lambda a: a+10
#x(5) = 15

 x = lambda a, b : a * b
 #x(5, 6) -> 5*6 = 30
""" Doubles the number you send in """
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
#mydoubler(11) = 22
#mydoubler(11) = 33

"""
A naive root/ line search method would look something like this
where each guess is a function of the previous guess,
plus some step size alpha and direction p.
"""
from __future__ import division

def naive_root(f, x_guess, tolerance, step_size):

    steps_taken = 0

    while abs(f(x_guess)) > tolerance:
        if f(x_guess) > 0:
            x_guess -= step_size
        elif f(x_guess) < 0:
            x_guess += step_size
        else:
            return x_guess

        steps_taken += 1

    return x_guess, steps_taken


root, steps = naive_root(f, x_guess=4.5, tolerance=.01, step_size=.001)

#root = 4.473, steps_taken = 27

"""
Problems with this approach:
if tolerance < step_size: the program never completes

if we started at 5 and not 4.5 we need 527 stpes instead of 27!\

This is why we use rootfinding algorithms
"""


""" Bisection method """

def bisection(f, lower, upper, max_iters=50, tolerance=1e-5):

    steps_taken = 0

    while steps_taken < max_iters:
        m = (lower + upper) / 2.0

        if m == 0 or abs(upper-lower) < tolerance:             return m, steps_taken                 if f(m) > 0:
            upper = m
        else:
            lower = m

        steps_taken += 1

    final_estimate = (lower + upper) / 2.0
    return final_estimate, steps_taken


root, steps = bisection(f, 1, 8)

""" Newton - Raphson Method """

def discrete_method_approx(f, x, h=.00000001):
    return (f(x+h) - f(x)) / h

def newton_raphson(f, x, tolerance=.001):
    steps_taken = 0

    while abs(f(x)) > tolerance:
        df = discrete_method_approx(f, x)
        x = x - f(x)/df
        steps_taken += 1
    return x, steps_taken



root, steps = newton_raphson(f, 8)

#root: 4.47213597002, steps: 4
# NOTE: This takes far fewer iterations than the bisection method!
#and is more accurate!

""" Secent Method """

def secant_method(f, x0, x1, max_iter=100, tolerance = 1e-5):
    steps_taken = 1
    while steps_taken < max_iter and abs(x1-x0) > tolerance:
        x2 = x1 - ( (f(x1) * (x1 - x0)) / (f(x1) - f(x0)) )
        x1, x0 = x2, x1
        steps_taken += 1
    return x2, steps_taken



root, steps = secant_method(f, 2, 8)


""" Inverse Quadratic Interpolation and Lagrange Polynomials """

def inverse_quadratic_interpolation(f, x0, x1, x2, max_iter=20, tolerance=1e-5):
    steps_taken = 0
    while steps_taken < max_iter and abs(x1-x0) > tolerance: # last guess and new guess are v close
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)
        L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
        L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
        L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
        new = L0 + L1 + L2
        x0, x1, x2 = new, x0, x1
        steps_taken += 1
    return x0, steps_taken



root, steps = inverse_quadratic_interpolation(f, 4.3, 4.4, 4.5)
#root: 4.4721359579 steps taken: 2
