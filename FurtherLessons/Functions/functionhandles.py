"""
Part 1: Example code on callbacks

Part 2: Lambda function exercise
Use lambda functions to sort the people list once by name, then by age.
What's the problem with sorting the list without its nominally-optional key callback?

Sort the list using sorted(list,key=fn). The input to the callback function is the entire
list element, eg, people[0]. The callback should return something comparable to the results
of the other elements to determine the order.
"""

# Part 1 - callback example from notes

import numpy as np

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

def load_math_save(filename,callback):
    numbers=np.loadtxt(filename)

    n1 = numbers[:,0]
    n2 = numbers[:,1]
    result = callback(n1,n2)

    # Create a new filename from filename + function name!
    basename = '.'.join(filename.split('.')[:-1]) # Removes extension
    save_fname = basename + '_' + callback.__name__ + '.txt'
    np.savetxt(save_fname,result,'%g')

load_math_save("callback_numbers.txt", add )
load_math_save("callback_numbers.txt", multiply )
load_math_save("callback_numbers.txt", subtract )
load_math_save("callback_numbers.txt", divide )

# Since you can put function handles into a list:
for fn in [add, multiply, subtract, divide]:
    # Variable 'fn' is the function handle- works like a pointer!
    load_math_save( "callback_numbers.txt", fn )


# Part 2 - Lambda function exercise

people = [
    {"name":"Bob",   "age":22},
    {"name":"Ellen", "age":21},
    {"name":"Alice", "age":25},
    {"name":"Cathy", "age":20},
    {"name":"Dylan", "age":27},
]

naive = sorted(people)
print(naive)