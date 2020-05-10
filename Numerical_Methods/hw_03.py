import numpy as np

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

f = lambda g: g*np.exp(g) - np.cos(g)

root, steps = bisection(f, 0, 1)
root
steps
