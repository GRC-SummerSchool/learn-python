|[< Previous (Git - Collaboration)](../Extra/GitBranch.md) | [Intermediate Python](README.md)| [Next (Pointers) >](pointers.md)
|----|----|----|

# Exceptions

With some blocks of code, no matter how well you program it, you can never be sure that the code will execute 100% of the time. While `x = 1 + 1` will always be safe, consider the following scenarios:

- You want to convert user input into an integer, but the input they gave is "hello world".
- You want to read in a file, but the file gets moved (by a different user or so) before you open it.
- You want to connect to a database, but the server hosting it is down.

In each of these cases, your program is dependent on more than just the actual code you've written. Most of the time, your code will execute just fine. However, based on the exact conditions at runtime, it may not execute perfectly. When something goes wrong, it can be important that your code handles it properly.

Imagine that you've been doing a lengthy, 5-hour calculation, and writing the results to a file. Three hours in, your code crashes because of something silly, like a divide-by-zero error. 
Since you never closed the file, your results so far never got saved, and you have to start over. Of course, before you do so, you add a couple of `if` statements to make sure you catch that particular error before it happens.
You rerun your code, and 4 hours later, you crash again because of something else. Your 5-hour calculation has now taken you at least 12 hours, plus time for re-writing and debugging.

Now imagine that instead, when you hit that first `ZeroDivisionError`, your code first saved the file, and a couple of key variables. When you fixed the issue, you re-ran the code by loading those variables, and started right from where you left off.
And that your code did that, not only with a `ZeroDivisionError`, but with _any_ fatal error or interruption. It's even possible to guard against `KeyboardInterrupt`s because you had to stop your code early since a colleague needed to use the computer.

Exception handling is about expecting the unexpected, and keeping your code running regardless.

## Try-Catch Blocks

The basis of exception handling is the try-catch blocks. In python, there are 4 keywords:

1. `try`
 
	A `try` block must always be combined with at least one `except` block, or with the `finally` block. This block defines the main part of the program, which you're expecting might generate an error.
2. `except`
   
	This block defines the code to run in case an exception does occur. You can combine multiple `except` blocks to specify a behavior for different type of exceptions:
	```python
	try:
		divisor = float(raw_input('Divide 5 by this number: '))
		answer = 5.0/divisor
		print('5/%g = %g'%(divisor,answer))
	
	except ZeroDivisionError:
		# This error occurs if divisor == 0
		print("Cannot divide by 0!")
	
	except ValueError as e:
		# This error will occur if the user input cannot be converted to a float, eg 'hello world'
		# 'e' is now a variable holding information on the error
		print(e.message)
		print('Please input a valid number!')
	
	except:
		# This takes care of everything else
		print('Congratulations, you broke the code in strange and creative ways!')
	```
	
	Generally, that last `except` block is considered bad programming practice, since it effectively hides any and all issues from the rest of the program- even if those issues would be better handled by other pieces of code. 
	Just like with `if` statements and loops, try-catch blocks can be nested within each other, and an outer block might be prepared to deal with the exception that the inner block is not.
	Or, in the case of a `KeyboardInterrupt` to stop a program early (because, during debugging, you accidentally made an infinite loop), since that counts as an exception which would be stopped by a generic catch-all block, it would not stop the program at all.
	
	With multiple `except` blocks, the order matters, since some errors are sub-types of other errors. In a case where an error could get handled by multiple blocks, the error goes to the first block that matches its type. 
	For example, `ZeroDivisionError` is a type of `ArithmeticError`. If there was a block catching the `ArithmeticError`s before the block catching the `ZeroDivisionError`s, a `ZeroDivisionError` would get handled by that block instead.
	The base type for all errors is the `BaseException` type. For specific, user-defined types (which may come with imported modules), it's recommended to use `Exception` as the base type instead, and `BaseException` is intended for built-in types.
	
	Some other types:
	* `IndexError` (for lists) and `KeyError` (for dictionaries) are both a type of `LookupError`
	* `IOError` (for input/output) and `OSError` (for operating systems) are a type of `EnvironmentError`
	* For more types of errors and their description, see the [Python Error Documentation](https://docs.python.org/2/library/exceptions.html)
	
	When a type of exception occurs that has no corresponding `except` block, the exception will get passed 'outwards', out of any loops, functions, or further try-catch blocks until it is either handled, or it stops the program.
	Before that happens though, the rest of the try-catch block will take effect first.
   
   (In a large number of other programming languages, the `except` block is called the 'catch' block, since it 'catches' an exception that the try block 'throws'. In python, however, exceptions are 'raised', as discussed below.)
3. `else`
	
	The `else` block must always be combined with one or more `except` blocks, and executes when no exceptions were raised during the `try` block. 
	In the following example, the block loops until a valid input has been given, or the user stops the program with Ctrl-C:
	
	```python
	zero_count = 0
	value_count = 0
	while True:
		try:
			divisor = float(raw_input('Divide 5 by this number: '))
			answer = 5.0/divisor
			
		except ZeroDivisionError:
			# Occurs if divisor == 0	
			zero_count+=1
			if zero_count >= 3:
				print("Are you even trying?")
			else:
				print("Cannot divide by 0!")
			
		except ValueError as e:
			# User input cannot be converted to a float, eg 'hello world'
			value_count+=1
			print(e.message)
			if value_count>=3:
				print("Do you know what a number is?")
			else:
				print('Please input a valid number!')
			
		except KeyboardInterrupt:
			# User stops the program
			print("I didn't want to run this program anyways.")
			exit() 
		
		else:
			print('5/%g = %g'%(divisor,answer))
			break # Stops the loop
	```
	Remember that python blocks are defined by their indentation, so the `else` in the `if-else` statement is distinguished from the `else` that comes at the end of the `try` block.
	
4. `finally`
	
	The `finally` block executes a piece of code, regardless of if an error happened or not. It is most used to make sure a resource closes properly, and will execute, even if a `return` or `break` statement happens inside the other blocks. 
	Unlike the `else` block, the `finally` block can be used even without any `execpt` blocks.
	
	```python
	try:
		divisor = float(raw_input('Divide 5 by this number: '))
		answer = 5.0/divisor
		print('5/%g = %g'%(divisor,answer))
	
	finally:
		print("Have a nice day!")
	```
	
	When this code creates an error, it does not stop the error from propagating at all. However, before it allows it to crash the program, it executes the code in the `finally` block. Similarly, if the `try` block completes without issue, the `finally` block still runs.
	
	In the earlier example, with a long calculation saving to a file, the `finally` block is how a programmer would ensure that the file always gets saved, regardless if the calculation finishes or not, while individual `except` blocks might define what to do in case of a specific sort of error.
	
### Nested Example
In this pseudo-code example, the function tries to connect to a database, pull information, and return a result.
Note the structure of the various try-catch blocks. (This code is pseudo-code, so the functions and error types are made up for illustration purposes. Running this will not work!)

```python
def database_query(query_information):
	try:
		database.connect()
		
		try:
			results = database.query(query_information)
			return results
		finally:
			database.disconnect()
	
	except DatabaseConnectionError:
		print("Could not connect to database.")
```

**Why nested try-catch statements?** The `finally` statement of the inner block would not apply to a database connection that wasn't open; trying to close a connection that wasn't open might raise its own exception!
However, talking to the database itself could have multiple issues; the _query_information_ could be in the wrong format, or be asking for information that doesn't exist. 
Regardless of what kind of error occurred, an open connection should be closed, otherwise the program could run into issues later on. The `finally` block even executed when everything goes as planned, even after the `return` statement!

**Making this better** This example has code that 'gives up' if it can't connect, but it's possible to write a function that attempts to connect multiple times, before passing on the issue for a separate part of the code to deal with:

```python
def database_query(query_information):
	retry_count = 0
	is_connected = False
	while not is_connected:
		retry_count+=1
		
		try:
			database.connect()
			
		except DatabaseConnectionError as e:
			if retry_count>=3:
				raise e #Passes the error onwards; see below for explanation 
			
		else:
			is_connected = True
			try:
				results = database.query(query_information)
				return results
			finally:
				database.disconnect()
```

### Traceback

The _traceback_ is the handy little error messages that you see explaining where the error occurred. Something like:

Run the following code snippet:
```python
def func2():
    func3()

def func1():
    func2()

def func3(arg):
    print(arg)

func1()
```

When you run it, you should see something along the lines of

```
Traceback (most recent call last):
  File "/Codebase/learn-python/FurtherLessons/demo.py", line 10, in <module>
    func1()
  File "/Codebase/learn-python/FurtherLessons/demo.py", line 5, in func1
    func2()
  File "/Codebase/learn-python/FurtherLessons/demo.py", line 2, in func2
    func3()
TypeError: func3() takes exactly 1 argument (0 given)
```
which tells you, line-by-line, where the error occurred. What caused the error? Line 2 of the file, inside func2 (which was called by func1, on line 5, which was called by the main script on line 10).
This kind of information can be incredibly helpful for debugging, since an error might originate from something that happens earlier in the program.
Of course, using a debugger helps trace the actual issue, but in cases where that's not practical, catching the exception, dealing with it, and putting the traceback in a log file can still help you determine the source of the error.

Python provides the [traceback](https://docs.python.org/2/library/traceback.html) module, which mimics the behavior of the python interpreter. 
This allows for all of the usual error information to be available, without needing to crash the program to get it.
```python
import traceback

try:
	answer = 5/0
except ZeroDivisionError as e:
	traceback.print_exc()

print("The program didn't crash though")
```

### Exercises
Use the following code snippet to open [exception_exercises.txt](exception_exercises.txt) and read in each line as a string.

```python
fin = open('exception_exercises.txt','r')
numAsStr = fin.readlines()
fin.close()
```
Loop through the entries and create two lists: one with the entries converted to integers, and one with the entries that 
can only be converted to complex numbers. Count how many entries are neither intergers nor complex numbers. You can use `int(string)` and `complex(string)`
to convert strings to the respective datatypes.

## Raising your own exceptions

You might find it useful to create your own exceptions. Consider a function that could return True, False, None, or any number of ambiguous values if it succeeds- how could you indicate to the function caller that it had failed?
Or a mathematical function that's intended for a certain input, although there would be no issue actually doing the math.
Creating your own errors and error messages helps users avoid unexpected behaviors.

In the example below, a factorial function raises errors if the input is not an integer (what would `factorial(3.14)` mean?), or if the input is less than one (`factorial(-4)` = ?).

Python has two keywords for creating errors: `raise` and `assert`

1. `raise`
	
	When you `raise` an exception, you specify the type of exception, generally with a descriptive message about why it occurred:
	
	```python
	def factorial(num):
		if not isinstance(num,int):
			raise TypeError("Input must be an integer")
		if not num>=1:
			raise ValueError("Input must be >= 1")
		
		# Input is valid
		answer = 1
		for i in range(num+1):
			answer*=i
	
		return answer
	```
	As seen in the earlier database example, if you have an error stored in a variable, you can use that as the argument in `raise`.
	Both of the following are valid syntax:
	
	```python
	...
	except TypeError as e:
		raise e
	```
	```python
	err = ValueError("Input must be >= 1")
	raise err	
	```
	
2. `assert`
	
	The `assert` keyword is a special case of the `raise` keyword, in that it first checks a condition before raising an exception.
	When the condition fails, an `AssertionError` gets raised, with an optional message specified after the condition.
	
	```python
	def factorial(num):
		assert isinstance(num,int),"Input must be an integer"
		assert num>=1,"Input must be >= 1"
		
		# Input is valid
		answer = 1
		for i in range(num+1):
			answer*=i
	
		return answer
	```
	
	This is commonly used to validate function input or output, but is also used when running tests on code:
	```python
	assert factorial(1)==1
	assert factorial(3)==6
	```
	You can read more about code testing in the [original Day 3 lesson](../Day3/Testing.md).
	
### Exercises
Turn the previous exercise into a function. If the number of discarded entries is more than 40% of the total entries,
raise an appropriate error. Try this with both [exception_exercises.txt](exception_exercises.txt) and [exception_exercises2.txt](exception_exercises2.txt)

	
|[< Previous (Git - Collaboration)](../Extra/GitBranch.md) | [Intermediate Python](README.md)| [Next (Pointers) >](pointers.md) |
|----|----|----|