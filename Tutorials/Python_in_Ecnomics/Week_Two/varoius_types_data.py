
"""
Data types available in python
you could be working with various types of data
These are built in types, i.e., they do not require an import statement

"""
#type()
#bool (boolean) True/False
a = True
b = False
not 1
not 0
#int (integer)
a = 1
b = 97
type(a)
#float (floating point decimal)
a = 13.4
type(a)
#str (string of characters)
string_a = 'Hello'
type(string_a)

"""
Mutable: can be modified
Immutable: can not be modified
list -> mutable
tuple -> immutable

"""
#list (sequence) -> can story any data type -> multi dimensional MUTABLE!
list_a = [1, 2, 3, 4]
list_b = ['Hi', 5, 'Dog']
type(list_b) #list
type(list_b[0]) #Str
list_a[0] = 'Goodbye'
list_a # ['Goodbye', 2, 3, 4]


#tuple () #IMMUTABLE
tuple_a = (1, 'Cat', 6.4)
type(tuple_a)
type(tuple_a[1])
tuple_a[0] = 'Goodby' #TYPE ERROR
#range (sequence) -> loops in for loops
list(range(10))
for _ in range(10): 
	print(_)
#1 // 2 // 3 // ...
#set (unordered collection of objects) -> no duplicants

list_c = [0,0,1,3,4,5,1000,2,4,1,4]
set(list_c) #[0,1,2,3,4,5,1000]

#dict (dictionary)
dict1 = {key1: value1, key2: value2}
dict1[key1] #value1


import pandas as pd

"""
Pandas is a high level programming library that gives us tools
to read data stored in "tabular" format.
Lets say we start with a .csv file
"""

data_DataFrame = pd.read_csv('/location/to/file.csv')

#Sometimes, we do not get exactly the data we want from just doing This
#therefore we look at the documentation for read_csv by googling pandas read_csv
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
