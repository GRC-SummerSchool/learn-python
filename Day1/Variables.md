| [< Previous (Whitespace)](Whitespace.md) | [Day1](../README.md)| [Next (Input)>](Input.md) |
|----|----|----|
### Single Line Comments
You can add comments to your code in several ways.
Single line comments start with a # and go until the end of the line

```python
# This is a comment
print("Hello World")  # This is also a comment
```
### Multi Line Comments
If you want to extend a comment for multiple lines, you can use triple quotes (single or double)

```python
''' This is a comment that
    extends until the next triple
    quote is encountered
''' 
print("Hello World")
"""" 
  You can also use double quotes to create a multi-line
  comment block 
"""   
```

## Variables

In Python, a ***variable*** is the name of a computer memory location that can store a certain value.

In manner of speaking, we say things like:

- "A variable stores/holds a value or object"
- "A value is assigned to a variable"
- "The (value of a) variable may change or can remain constant"

In Python, every variable is an object and there is no need to declare the variable before their use.

### Numbers

Python supports 3 **types** of numbers (int, float and complex).

```python
i = 5       # integer arbitrary length 
f = 2.37    # floating point number (typically 64 bit)
j = 2+3j    # complex number (typically 2 x 64 bit)
```
_Note prior to Python 3.6, Python had two integer types int (32-bit) and long (arbitrary). Now all integers
have arbitrary length_

### Boolean

Python also supports the notion of boolean values (which are really a subtype of int).

```python
t_val = True     
f_val = False    
```

### Strings

In python strings are defined using either single or double quotes. The opening and closing quote must match. They must
either both start and end with a single quote, or both start and end with a double quote.

```python
string1 = 'hello there'       
string2 = "I am also a string"
string3 = "I'm also a string"   # No need to escape the single quote, because string is defined with double quotes
string4 = 'I\'m also a string'  # Here a single quote appearing inside a single quoted string needs to be escaped
```

### Dynamic Type

Often, you may hear people say, *"Python is a dynamically-typed language"*. This means that the same variable can hold different types of objects during the course of execution of a program. In the example below, observe how the same variable holds different types of objects!

``` python
temp = 30		# integer
print(type(temp))	# type (variablename) is a special built-in function

temp = 133.3	# float
print(type(temp))

temp = "Very hot !"	# string
print(type(temp))
```

### Printing

Python allows variables to be passed to print statements using commas to separate items.

```python
i = 5       # integer
f = 2.37    # floating point number
j = 2+3j    # complex number

# print("The value of i = ", i)
print("The value of f = ", f)
print("The value of j = ", j)
print("The value of i = ", i, ", f=", f)

print("The sum of 1 + f + j ", i + f + j)  # The numbers are added together and then printed out
```

Strings may be concatenated together using the + operator.
```python
string1 = 'Hello'       
string2 = "World"
print(string1 + " " + string2)

print("The length of string1 is ", len(string1))
```



### Assigning one variable to another

Until now, we saw variables being assigned a value. Variables can also be assigned (the value of) another variable. Think of this as copying a variable.

```python
x1 = 50					# integer
x2 = 60					# another integer
title = "Shark Tank"	 # a string	
x3 = x1 				# x3 now holds the value of x1
x1 = 70					# now we changed the value of x1, should x3 change ?
print(x1, x2, x3)		# note the values : 70, 60, 50
x2 = title				# x2 held an integer (60) previously, now holds a string
print(x2)				# "Shark Tank"
```

The important thing to note is that once an assignment is done, the two variables are NOT related, i.e their values do not follow or track each other. Each can be independently changed without affecting the other.

### Exercise

1. Modify your Hello World program to greet you by name, where your name is stored in a variable.

2. Add some variables with different types and print them (as shown in the sections above).
3. Extra credit : Store your first and last names in two different variables, and print out a concatenated line (e.g. "My name is Sherlock Holmes")
4. More extra credit: Print the number of characters in your name (e.g. Number of characters in my name : 14). Be cognizant of the blank space.



| [< Previous (Whitespace)](Whitespace.md) | [Day1](../README.md) | [Next (Input)>](Input.md) |
|----|----|----|