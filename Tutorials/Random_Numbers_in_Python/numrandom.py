import random as random #https://docs.python.org/2/library/random.html

random.seed(1) # use the same random numbers when running the program again

print(random.random()) #Random number from uniform distribution from 0-1
#0.13436424411240122
for _ in range(10):
    print(random.randint(0,10)) #random int from 1, 10
random.gauss(0,1) # mean is 0 and 1 is std deviation in this gaussian distribution


#Sampling
sequence = [i for i in range(20)] #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

for _ in range(5):
    selection = random.choice(sequence)
    print(selection) #prints 5 numbers from the list of 1 - 20
subset = random.sample(sequence, 5) #returns a subset of the sequence of length 5 as a list
random.shuffle(sequence)
print(sequence) #[17, 15, 1, 10, 2, 4, 9, 18, 11, 6, 13, 14, 8, 3, 12, 0, 7, 16, 19, 5]

import numpy as np
np.random.seed(420)
int_array_values = np.random.randint(0,10,20)
#array([1, 8, 6, 3, 9, 8, 7, 6, 4, 3, 8, 4, 5, 6, 0, 5, 5, 8, 8, 2])
gaussian_random_values = np.random.randn(10)
#array([ 1.56267506, -0.18006799,  0.36222899,  0.47430314,  0.72829863, -0.76664673, -1.45184634, -0.30116949, -1.00106212,  0.33552654])
