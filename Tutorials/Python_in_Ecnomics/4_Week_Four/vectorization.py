import numpy as np
import timeit
import matplotlib.pyplot as plt

np.random.seed(420)
#Using a random seed, so that the same random values are
#generated each time





"""
#https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.randint.html
Create array of 100 coin flips :
2 is one above the highest integer to be chosen for distribution -> high arg
size = 100 -> shape of output array

we multiply the output array by 2, since the current output would be 0's and 1's
then we subtract 1 from each value to get an array of 1's and -1's
"""

def coin_flipys(N):
    return 2*np.random.randint(2, size=N)-1
#print(np.unique(coin_flipys(10))) #output is an array of [-1, 1]
#print(coin_flipys(10))


coin_flips = coin_flipys(100)

"""
https://docs.scipy.org/doc/numpy/reference/generated/numpy.cumsum.html

many ways of summing up arrays
1.) Looping (inefficient) time: O(n)
2.) Iterating (also inefficient): O(n log n )
3.) Vectorizing (applying one function to the whole array): O(1)

"""


#1 Looping
def looping(initial_array):
    looping_displacement = []
    looping_displacement.append(initial_array[0])
    for i in range(1, len(initial_array)):
        looping_displacement.append(looping_displacement[i-1] + initial_array[i])
    return looping_displacement

#print(looping(coin_flips))


#2 Iterating
from itertools import accumulate
def iterating(initial_array):
    return list(accumulate(initial_array))

#print(iterating(coin_flips))

#3 Vectorizing
def vectorizing(initial_array):
    return np.cumsum(initial_array)
#print(vectorizing(coin_flips))


from functools import partial
def plotTC(function, nMin, nMax, nInc, nTests):
    """
    Run timer and plot time complexity
    """
    x = []
    y = []
    for i in range(nMin, nMax, nInc):
        N = i
        testNTimer = timeit.Timer(partial(function, coin_flipys(N)))
        t = testNTimer.timeit(number=nTests)
        x.append(i)
        y.append(t)
    p1 = plt.plot(x, y, 'o')
    #plt.legend([p1,], [function.__name__, ])

def sizing(N):
    return N
def main():
    print(timeit.timeit("looping(coin_flipys(sizing(10000)))", setup="from __main__ import looping, coin_flipys, sizing", number = 1000))
    print(timeit.timeit("iterating(coin_flipys(sizing(10000)))", setup="from __main__ import iterating, coin_flipys, sizing", number = 1000))
    print(timeit.timeit("vectorizing(coin_flipys(sizing(10000)))", setup="from __main__ import vectorizing, coin_flipys, sizing", number = 1000))
    #plotTC(vectorizing, 10, 10000, 10, 10)
    #plotTC(looping, 10, 10000, 10, 10)
    #plotTC(iterating, 10, 10000, 10, 10)
    #plt.show()

if __name__ == '__main__':
    import timeit
    main()
