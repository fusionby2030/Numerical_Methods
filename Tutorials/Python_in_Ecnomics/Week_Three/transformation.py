"""
To transform data, we write functions
these functions can be as simple or complex as you want.
They can have an input, and or an output
A function without expleccit return statemtns returns None
Functions must then be called to be used
"""
#Example of Input and Output
def add_one(x):
    """ Function to add 1 to input integer """
    return x+1
#call the function
add_one(2) #3
#Example of no input but output
def create_data():
    x = []
    y = []
    return x, y
x, y = create_data()
x.append(1)


#Example of no output
def hello_function():
    print('Hello World')

hello_function()

"""
The input into a function is called an argument
they can be defined in the function
or be passed implicitely by position or explicitly by name
Let's make our add_one function to be usable for any add
"""

def add(x = 1, n= 1):
    return x+n
add(2)
new_x = add(2) #stored in new variable
add(new_x)
add(2, 2)
add(n = 2, x = 3)

"""
If we wanted to add items to a list
The instance of the default value is bound at the time the function is defined.
Consequently, there is a single instance of the mutable object
that will be used across all calls to the function.

Mutable objects can utelize looping methods!
"""
def add_items(new_items, base_items=[]):
    for item in new_items:
        base_items.append(item)
    return base_items
add_items((1,2,3)) #[1, 2,3]
add_items((1,2,3)) #[1, 2, 3, 1, 2, 3]
"""
As a result, it is best to use default value of None as a flag
to signify the absense of the argument and handle the case inside the function body.
"""
def add_items(new_items, base_items=None):
    if base_items is None: # is -> ==
        base_items = []
    for item in new_items:
        base_items.append(item)
    return base_items
add_items((1,2,3)) #[1, 2, 3]
add_items((1,2,3)) #[1, 2, 3]

"""
We can get even more complex
Lets try to add 1 to each value of a list, then sum every item

[1, 2, 3, 4, 5] -> 20

"""
"""
One may be tempted to write out what is in function (oops)
"""
def oops(input):
    sum = 0
    for number in input:
        number = number + 1
    for number in input:
        sum = sum + number
    return sum
"""
But we did not change the numbers in the input array!
Be carefuly when looping and carefully check what is going on during each iteration.
"""
def loopy_way(input):
    sum = 0
    for i in range(0, len(input)):
        input[i] = input[i] + 1
    # What is another way we could write this? (+=)
    for number in input:
        sum = sum + number
    return sum
# we can also utelize built-in python functions
def not_so_loopy(input):
    return sum([i + 1 for i in input])
loopy_way([1, 2, 3, 4, 5])
not_so_loopy([1,2,3,4,5])
