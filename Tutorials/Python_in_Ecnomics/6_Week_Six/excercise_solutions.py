"""
1.

factorial
"""


def factorial(n):
    p = 1
    for i in range(n):
        p = p * (i + 1)
    return p


"""
2
Binomial rv 
"""

from numpy.random import uniform


def binomial_rv(n, p):
    count = 0
    for i in range(n):
        U = uniform()
        if U < p:
            count = count + 1  # Or count += 1
    return count


"""
3

2 random devices
"""

from numpy.random import uniform


def device_one(k):  # pays if k consecutive successes in a sequence

    payoff = 0
    count = 0

    for i in range(10):
        U = uniform()
        count = count + 1 if U < 0.5 else 0
        print(count)  # print counts for clarity
        if count == k:
            payoff = 1

    return payoff


def device_two(k):  # pays if k successes in a sequence

    payoff = 0
    count = 0

    for i in range(10):
        U = uniform()
        count = count + ( 1 if U < 0.5 else 0 )
        print(count)
        if count == k:
            payoff = 1

    return payoff
