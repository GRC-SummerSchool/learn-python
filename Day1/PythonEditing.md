|[< Previous (HelloWorld)](HelloWorld.md) | [Day1](../README.md)| [Next (Variables) > ](Variables.md) |
|----|----|----|
# Python specifics
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

"""
  You can also use double quotes to create a multi-line
  comment block 
"""   
```

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



|[< Previous (HelloWorld)](HelloWorld.md) | [Day1](../README.md)| [Next (Variables) > ](Variables.md) |
|----|----|----|
