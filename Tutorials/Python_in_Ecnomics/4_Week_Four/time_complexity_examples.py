# O(1) + O(n) +O(n^2) -> O(n^2)
import timeit
"""
Unsorted List
Linear Search
We want to find the index of a certain desired value from a given list using linear search.
"""

sample = [1, 5, 3, 9, 2, 4, 6, 7, 8]


def lin_search(input_list, want):
    for index in range(len(input_list) - 1):
        if input_list[index] == want:
            break
        else:
            continue
    return index
lin_search(sample, 1)
#timing the function
#print(timeit.timeit(lin_search, number = 1000))
"""
Best Case - solving the problem for the best input
We are searching for the value 1, so the first iteration would find
"""

# print(lin_search(sample, 1))

"""
Average Case
We are searching for the value in the "middle" of the list, so 2.
"""

# print(linear_search(sample, 2))

"""
Worst Case - solving the problem for the worst input of size of n
In this case: 8
"""

# print(linear_search(sample, 8))

"""
Constant Time - O(1)
Not dependent on the input data (n). No matter the size of the input data, the running time will always be the same.
ex.

if a > b:
    return True
else:
    return False
"""


def get_first(sample):
    return sample[0]


"""
Logarithmic - O(log n)
Reducing the size of the input data at each time step such that it does not look at all the values of the input data
Most commonly binary trees or binary searches which we will go into next week.

ex.
for index in range(0, len(data), 3):
    print(data[index])
"""
sample = [1, 5, 3, 9, 2, 4, 6, 7, 8]

def binary_search(data = sample, value = 8):
    n = len(data)
    left = 0
    right = n - 1
    i = 0
    while left <= right:
        print("Starting Iteration Number {}".format(i))
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
            print("Update Right")
        elif value > data[middle]:
            left = middle + 1
            print("Update Left")
        else:
            print("Found the value!!")
            return middle
        print("Ending Iteration")
        i = i + 1
    raise ValueError('Value is not in the list')
print(binary_search(sample, 8))
print(timeit.timeit(binary_search, number = 1000))
"""
Steps of Binary Search
    Calculate the middle of the list.
    If the searched value is lower than the value in the middle of the list, set a new right bounder.
    If the searched value is higher than the value in the middle of the list, set a new left bounder.
    If the search value is equal to the value in the middle of the list, return the middle (the index).
    Repeat the steps above until the value is found or the left bounder is equal or higher the right bounder.
"""

# print(binary_search(sample, 8))


"""
Linear Time - O(n)
Running time increases at most linearly with the size of the input data.

for value in data:
    print(value)
"""
def lin_search(input_list, want):
    for index in range(len(input_list) - 1):
        if input_list[index] == want:
            break
        else:
            continue
    return index

def linear_search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Value not found in the list')


# print(linear_search(sample, 8)


"""
Quasilinear Time - O(n log n)
Each operation in the input data has a logarithmic time complexity

ex.

for value in data1:
    result.append(binary_search(data2, value))
"""


def merge_sort(data):
    if len(data) <= 1:
        return

    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]

    merge_sort(left_data)
    merge_sort(right_data)

    left_index = 0
    right_index = 0
    data_index = 0

    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1

    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]


merge_sort(sample)
print(sample)

"""
Quadratic Time O(n^2)
Preforming a linear time operation for each value in the input data

ex
for x in data
    for y in data:
        print(x, y)
"""

sample = [1, 5, 3, 9, 2, 4, 6, 7, 8]

def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True


bubble_sort(sample)
print(sample)

"""
Exponential Time - O(2^n)
growth doubles with each addition to the input data set
Normally in Brute Force Algorithms i.e., checking all possible elements of a password through guessing
"""


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


"""
What is the time complexity of my algorithm?
Describe the algorithm based on the largest complexity among all operations
"""


def my_function(data):
    first_element = data[0]
    for value in data:
        print(value)

    for x in data:
        for y in data:
            print(x, y)

# What is the time complexity for this?
# Answer is the first line of this file!
