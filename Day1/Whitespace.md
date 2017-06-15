|[< Previous (HelloWorld)](HelloWorld.md) | [Day1](../README.md)| [Next (Variables) > ](Variables.md) |
|----|----|----|
# Python specifics
## White Spaces

Python takes a minimalist approach to typing and prefers to avoid unnecessary typing.
Many languages use curly braces {} to denote grouping of statements or blocks;
however, Python has chosen to represent the block structure of a program with simple indentation.

### Indentation

The leading 4 spaces (or tabs, BUT DON'T USE THEM) provide the statement grouping or block definition.
Empty lines may appear anywhere, and can aid in the readability of your program.

```python
if 1 + 1 == 2:
    print("All these statements")
    print("sharing the same indentation")
    
    print("will execute when the condition evaluates true")
print("This statement does not belong to the conditional and will always execute")
```

Some people don't like the forced indentation style, but it is required to use Python.
The benefit to this structure is that code written by different teams has a similar style.

### Long Lines

Often times for readability it's desirable to break up a long line across multiple statements.
Python has a few ways to handle this...  You can break any statement in the middle of matching
braces (parenthesis, square brackets, and curly braces).

```python
if (some_long_expression == some_long_condtion and        # line continuation automatic
  some_other_long_expression == some_other_long_condtion):  
    print("Condition was true")

mylist = [ 1, 2, 3, 4, 5, 6, 7,                           # this also continues naturally
           8, 9, 10]

dict = {                                                  # continues naturally too
    "bread" : 3.09,
    "eggs" : 2.19,
    "milk" : 2.29
}

# If you want to break up a statement that doesn't fall within braces you can
# use the \ at the end of the line to signify the continuation onto the next line

if some_long_expression == some_long_condtion and         \
  some_other_long_expression == some_other_long_condtion: 
    print("Condition was true")
```

*__NOTE: Nothing else can follow the line continuation character (not even comments).__*

### Why not tabs

Tabs can be used for indentation; however, python treats tabs as an indentation of 8, so unless you
are 100% certain that everyone in your project will always have their tabstops all set to 8, and 
no-one will ever add spaces with using the wrong tabstop - then go ahead...  
__But don't say I didn't warn you!__

## Comments

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

|[< Previous (HelloWorld)](HelloWorld.md) | [Day1](../README.md)| [Next (Variables) > ](Variables.md) |
|----|----|----|
