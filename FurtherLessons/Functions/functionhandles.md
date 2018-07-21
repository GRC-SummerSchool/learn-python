|[< Previous (Recursion)](recursion.md) | [Intermediate Python](../README.md)| [Next (Generators) >](generators.md) |
|----|----|----|

# Function Handles and Lambda Functions
_Before beginning this section, you should be comfortable with [pointers](../pointers.md) and [function arguments](argskwargs.md)._

An interesting thing about functions is that the function name can be treated as a proper variable in its own right.
This means you can:
- Pass in a function as an argument to another function
- Return a function as the result of a function
- Create a list or dictionary of functions
- Anything else you could do with a regular variable

When you use a function like this, you're actually using what's called a *function handle*. 

## Callbacks
A callback function is a function passed in as the argument to another function, to be run as part of that other function.
This is typically seen when the programmer doesn't have as much control about when that second function will run, especially in
situations with a user interface. A common example is "When the user presses a button, run this function". Alongside the callback
function, there will typically be arguments to represent the arguments/keyword arguments that get passed into the callback.
Below is a standard way of creating and calling a function with a callback. Notice that when the function is passed in as the
argument, it does not have any parentheses after it. This is how the code knows to use it as a handle, and not immediately run it
(passing in the returned value as the argument instead). 

```python
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


load_math_save( "callback_numbers.txt", add )
load_math_save( "callback_numbers.txt", multiply )
load_math_save( "callback_numbers.txt", subtract )
load_math_save( "callback_numbers.txt", divide )

# Since you can put function handles into a list:
for fn in [add, multiply, subtract, divide]:
    # Variable 'fn' is the function handle- works like a pointer!
    load_math_save( "callback_numbers.txt", fn )
```

You can design your callback functions however you need. In this case, all the arguments for the callbacks were intended
to come from the function calling them. You can also design the function so that all or some of the arguments get passed
into the calling function. Combined with the ability to handle variable numbers of arguments, this allows for very flexible code:
```python
# arg1 is calculated, arg2 is passed into the function
def myFunc1(callback,arg2):
	arg1 = 4
	callback(arg1,arg2)
	
# myFunc1(callback_fn,2)
	
	
# Any number of arguments are passed in
def myFunc2(user,callback,*args,**kwargs):
	if allowed(user):
		return callback(*args,**kwargs)
	else:
		return None
	
# Instead of: callback_fn( 2, 3, 5, 8, greeting="Hello")
# myFunc1("Alice", callback_fn, 2, 3, 5, 8, greeting="Hello")

		
# Combination of calculated arguments and variable number
def myFunc3(database,callback,*args,**kwargs):
	dbc = connect(database)
	result = callback(dbc,*args,**kwargs)
	close_connection(dbc)
	return result

# Instead of: callback_fn(connection, 2, greeting="Hello")
# myFunc1(local_db, callback_fn, 2, greeting="Hello")
	
	
# Multiple callbacks with varible number of arguments
# The args/kwargs for each is passed in as a list/dictionary
def myFunc4(user,callback1,args1,kwargs1,callback2,args2,kwargs2):
	if allowed(user):
		return callback1(*args1,**kwargs1)
	else:
		return callback2(*args2,**kwargs2)
```
Especially with callbacks that use a variable number of args/kwargs, this allows the callback functions themselves to be
written "as normal", without restricting input because of the calling function (the function that runs the callback).

## Lambda functions

In Python, a lambda function is a special kind of function defined entirely in just one line (or expression)
They are frequently used when the callback function is very basic, as the `add`, `subtract` functions in the example above.
They consist of just the input arguments and the returned value. Because of their simplicity, aside from being assigned to
a variable, they can also be defined 'on the spot'. 

```python
# Assign to a variable
add = lambda n1, n2: n1+n2 # Takes n1, n2 input, returns n1+n2
print( add(1,4) )
load_math_save( "callback_numbers.txt", add )

# Define in-line
load_math_save( "callback_numbers.txt", lambda n1, n2: n1-n2)
```
### Exercises
The `sorted(list,key = fn)` function returns a list, optionally sorted by a custom key that's used to determine which values
are before or after the others. Open [functionhandles.py](functionhandles.py). Create a lambda function to use as the key.
Sort the `people` list first by age, then by name. What happens when there is no callback function? Why? Note: the input to the
lambda function will be the entire entry, eg, `people[0]`, `people[1]`, etc.

## Returning a function

Using a function as a variable means it's also possible to create a function inside a function, and return it. This is generally
for creating related groups of functions that have only a couple key differences.

In the example below, the `power(n)` function returns a function that returns `x^n`. The comments 

```python
def power(n):
	
	# Create a new function where n is fixed
	def fn(x):
		return x**n
	
	return fn # return the function handle
	
square = power(2)
# def square(x):
#	 return x**2
cube = power(3)

assert square(0) == 0
assert square(1) == 1
assert square(2) == 4

assert cube(2) == 8
```

### Exercises
Write `quadratic(c, b, a)` that returns a function to take a numpy array and applies the quadratic equation to it (`a*x^2 + b*x + c`). Now create a 
function `linear` that does the same thing, but with a variable number of arguments, to create a generic linear equation (the first variable should be the constant).
When `linear` has the same three arguments as `quadratic`, both results should be effectively the same. Create & plot several equations.

## Decorators
Decorators in Python combine both aspects of callback functions and returning a function. Where the `power` example above took the exponent `n` as the
variable to bake into its returned function, a decorator function actually takes the callback function to include in its created function.
This is especially helpful in cases where you *only* want a function to be run as a callback. Functions that require authentication, connection to a resource
that must be opened or closed, a specific type of exception handling, or other similar behaviors are simplified using decorators.

Below is the basic structure of a decorator function, but hold on, because there's one more neat trick to make it a full decorator!
```python
def authenticate(callback):
	
	def fn(user,*args,**kwargs):
		if allowed(user):
			return callback(user,*args,**kwargs)
		else:
			raise ValueError("User not allowed")

	return fn
	

def logout(user):
	pass
logout = authenticate(logout) # Reassigning the logout function handle to new function!

def read_db(user, database):
	return read(database)
read_db = authenticate(read_db)

def write_db(user,database,data):
	write(database, data)
write_db = authenticate(write_db)

read_db(user,database)
write_db(user,database,"Foo Bar")
logout(user)
```
Wrapping all three functions in the `authenticate` decorator means that when the actual code inside the function tries to
run, it first goes through the authentication code. However, using the function itself is no different than if it hadn't
been modified. Since the callback's output gets returned from the created function inside the decorator, this especially
makes the decorator "invisible"

Instead of needing to continuously re-assign the function handle to the decorator after the function has been created, it's
possible to do it in one step! Python has an `@decorator` syntax that makes it easy:
```python
@authenticate
def logout(user):
	pass

@authenticate
def read_db(user, database):
	return read(database)
	
@authenticate
def write_db(user,database,data):
	write(database, data)
```
This also allows you to stack multiple decorators, and keep track of which one is nesting which- order can matter! For example,
you'd want to authenticate before opening a database connection, so you'd want something that looked like this:
```python
@authenticate
@open_db
def write_db(user,dbc,data):
	dbc.write(data)
```

For some cases, you'll need to slightly modify your decorator in order for the function's name to get properly reassigned. This
is done with yet another decorator! To ensure you don't run into errors, it's best to always include it. The full makeup of a decorator is below:
```python
from functools import wraps

def decorator(callback):

	@wraps(callback) # Correctly re-assigns function handles
	def fn(*args,**kwargs):
		# Your code here!
		return callback(*args,**kwargs)

	return fn

@decorator
def myFunc(a,b,c):
	return 1, 2, 3
```

### Things get meta
The drawback of the `@` syntax is that it can only take a single argument- the callback itself- as the decorator input.
However, it's possible to use a function (with multiple arguments) to create a decorator (with the callback as its argument),
which creates the function that wraps the callback function. This results in *3* nested functions:

```python
from functools import wraps

def authenticate(scope): # Scope means like, "admin", "user", etc

	def decorator(callback):
		
		@wraps(callback)
		def fn(user,*args,**kwargs):
			if allowed(user,scope):
				return callback(user,*args,**kwargs)
			else:
				raise ValueError("Access Denied")
		
		# decorator returns fn, which has callback and scope defined
		return fn 
	
	# authenticate returns a decorator, generally "one-time use"
	return decorator 

@authenticate("user")
def logout(user):
	pass

@authenticate("user")
def read_db(user, database):
	return read(database)
	
@authenticate("admin")
def write_db(user,database,data):
	write(database, data)
```
Working through what happens when `@authenticate("admin")` is called:
1. `authenticate("admin")` creates and returns the decorator function, where scope = "admin"
2. The decorator function plugged into the `@decorator` syntax, and gets `write_db` as its callback
3. The decorator returns its function, with callback and scope both defined.


### Exercises
- Write a decorator that times and prints out how long a function takes to run. Create example functions that pause for
various lengths of time to test the decorator.
- Write a decorator `shush` that suppresses all errors from the function it wraps. Now never use it, because that's a terrible idea.
For a challenge, create a decorator that takes in a specific type of error message to suppress (eg, `ValueError`, `IndexError`, etc)

|[< Previous (Recursion)](recursion.md) | [Intermediate Python](../README.md)| [Next (Generators) >](generators.md) |
|----|----|----|