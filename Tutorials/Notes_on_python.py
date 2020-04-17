"""
Python Tutorials!!
remove the # before the print statement to see the output of the code above 

Simple function
f(x) = x^2 if 0 > x < 20
f(x) = 0 if x < 0
f(x) = 20 if x > 20


"""

def func(x): #this is a function to return x**2
    y = 0# initialize y value
    if x < 0:
        y = 0
    elif x > 20:
        y = 20
    else:
        y = x**2
    return y
#can also be written like this
def func2(x):
    y = 0
    if x < 0:
        return 0
    elif x > 20:
        return 20
    else:
        return x**2
#one should be careful when using func2 since there is no general return Statement
#although there is one in the else


#print(func2(5)) #Output: 25
#print(func(23)) #Output: 20
#print(func(-10)) #Output: 0


"""
You can also use custom print statements by doing the following

"""
#print("The value of f(x) = x^2 for x = 4 is {}".format(func(4)))

#print("The value of f(x) = x^2 for x = {} is {}".format(3, func(3)))

b = 25
#print("The value of f(x) = x^2 for x = {} is {}".format(b, func(b)))

"""

So far we have seen how to define a function using def and returning using return
Also printing the output using print() and using the functions
Now we go onto lists and for loops
"""

"""
Task:
Given a List, Count how many of a certain value appear.
A for loop will run the code inside of it as long as the statement it is defined by
is true.

i.e if we go through a list of animals with a for loop, it will iterate through the list
until there are no more animals to go through
In the below code it will start at Tiger, then go to Dog -> Bat -> Egyptians

"""
animal_list = ['Tiger', 'Dog', 'Bat', 'Egyptians']
scary_animals = 0 #Initalize the count
for animal in animal_list:
    if animal == 'Tiger' or animal == 'Egyptians':
        #scary_animals = scary_animals + 1
        scary_animals += 1

#print("The number of scary animals in the zoo: {}".format(scary_animals))

"""
You can also put the above into a function
"""
def count_things(list, thing):
    count = 0
    for item in list:
        if item == thing:
            count += 1 # Same as just adding 1 to the count
    return count

#print("The number of {} in the list {} is:".format('Tigers', 'animal_list', count_things(animal_list, 'Tiger')))


"""

Now if we wanted to make an evenly spaced interval of integers we can use a for loop
in the case as long as the i is in the range of numbers, the loop will continue, so
once i becomes the stop number, the loop will finish.

"""

def make_interval(start, stop):
    interval_list = [] #initialize the array
    for i in range(start, stop):
        interval_list.append(i)
    return interval_list
#print(make_interval(1, 100))
#print(type(make_interval(1,100))) # this is to show it is a list and is different from the numpy array
"""
Note: the array made with make_interval stops at 99, since the for loop will close when i reaches 100
so if you want an array from 1 to 100, you need to make the stop number 101


one can also use numpy to achieve the same thing. They basically have
preset functions like make_interval that do the work for us

"""
import numpy as np
#print(np.linspace(1,100, num=100))
#print(type(np.linspace(1,100, num=100))) # this will return its class of nd array




"""
Previously we covered how:
functions can be defined
for loops
if else statements
lists



Numpy and its goodness
Making Pretty Graphs
"""

#pip install numpy in terminal

import numpy as np


#list -> array

first_list = [1,2,3,4,5]

numpy_array = np.array(first_list)
#print(type(numpy_array))
#print(type(first_list))

second_list = [[1,2,3], [5,4,1], [3,6,7]]
new_2d_arr = np.array(second_list)

#print(new_2d_arr)  #This line show the result of the array generated



"""
Creating from built-in numpy functions
when using a function you are not so sure how to use, just google the library and the function name

for example: search numpy arange
and you will find exactly what you are looking for

arange: Generates values from (start, stop, increment)
zeros: array of zeros of size (N)
ones: same but with ones
All of these can be two d!
"""

my_list = np.arange(10) #https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html
#OR
#print(my_list)
my_list = np.arange(0,11) #This generates 10 digits of values from index 0 to 10.
#print(my_list)
my_list = np.arange(0,10, 2) #This generates 5 digits of values from index 0 to 10 with increment of 2
#print(my_list)


zeros = np.zeros(7) #createws array of seven zeros
#print(zeros)
my_ones = np.ones(5)
#print(my_ones)
#TWO DIMENSIONS!!
two_d = np.zeros((3,5)) # Notice the (n, m) as this is the 2 dimensions of the matrix: 3 rows, 5 Columns
#print(two_d)
"""
Axis creations: or domain
Evenly spaced values from 0, 10
"""
lin_arr = np.linspace(0, 10)
#print(lin_arr)

#Identity matrix

my_matrix = np.eye(6)    #6 is the number of columns/rows you want
#print(my_matrix.shape)
"""
Indexing

first value in array has index 0, and each element after has +1 of the element before
for 2d arrays it is the same but with row first then column
"""

arr = np.arange(0,51)
two_d_arr = np.array([[10,20,30], [40,50,60], [70,80,90]])
#print(arr)
#print(two_d_arr)

#print(arr[0])
#print(arr[5])
"""
Google array splicing
"""
#print(two_d_arr[1,2]) #value 60
#print(two_d_arr[0][:])
#print(two_d_arr[:1, :2])           # This returns [[10, 20]]
#print(two_d_arr[:,2])           # This returns ([[20, 30], [50, 60]])
#print(two_d_arr[:2, :2])          #This returns ([[10, 20], [40, 50]])
#print(two_d_arr[0])    #This grabs row 0 of the array ([10, 20, 30])
#print(two_d_arr[:2]) #This grabs everything before row 2 ([[10, 20, 30], [40, 50, 60]])

"""
Logical operations (AND OR > < ==)
"""
new_arr = np.arange(5,15)
#print(new_arr)
#print(new_arr > 10)
bool_arr = new_arr > 10

#print(new_arr[bool_arr])

#shorter and cuter
greater_than_10 = new_arr[new_arr>10]

#print(greater_than_10)

"""
Arithemtic and scaler
using numpy functions
"""

arr = np.arange(1,11)
#print(arr*arr)
#print(arr-arr)
#print(arr+arr)
#print(arr/arr)

#scaler
#print(arr+50)

#print(np.sqrt(arr)) #return sqrt of each elemtn
#print(np.sin(arr)) #Returns sin of each element
#print(np.std(arr))     #Returns the standard deviation of in the array
#mat = np.arange(1,26).reshape(5,5)
#mat.sum()         #Returns the sum of all the values in mat
#mat.sum(axis=0)   #Returns the sum of all the columns in mat
#mat.sum(axis=1)   #Returns the sum of all the rows in mat

"""
Simple showing of matplotlib
to see more examples check out example_problems.py

"""
import matplotlib.pyplot as plt


x = np.linspace(0, 10)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y)
plt.plot(x,z)
plt.show()
