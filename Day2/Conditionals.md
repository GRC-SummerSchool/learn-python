|[< Previous (Lists)](Lists.md) | [Day2](../README.md)| [Next (Loops) >](Loops.md) |
|----|----|----|
# Conditionals

Conditionals allow you to execute a portion of code when a condition is satisfied.

### If Statements
You can add an *if* clause to execute when the condition is satisfied:

```python
x = 5
if x < 10:
    print("x is < 10")
```

You can add an *else* clause to execute when the condition is not satisfied:

```python
x = 15
if x < 10:
    print("x is < 10")
else:
    print("x is not < 10")
```

You can add additional *elif* (else if) clauses that are also evaluated. Only one condition 
will execute. Each condition is evaluated in the order listed. Once a condition evaluates
true, any remaining conditions are skipped.

```python
x = 10
if x < 10:
    print("x is < 10")
elif x > 10:
    print("x is > 10") 
else:
    print("x is not < 10 and x is not > 10")
```

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

You can choose the number of spaces in your code, but when working with others agree on a common style. Otherwise you can end up with code that looks like this and won't build!

```python
if 1 + 1 == 2:
    print("All these statements")
  print("this is a problem because it is not indented 0 or 4 spaces")
print("This statement does not belong to the conditional and will always execute")
```

### Why not tabs

Tabs can be used for indentation; however, python treats tabs as an indentation of 8, so unless you
are 100% certain that everyone in your project will always have their tabstops all set to 8, and 
no-one will ever add spaces with using the wrong tabstop - then go ahead...  
__But don't say I didn't warn you!__

### IDE (Integrated Development Environment

The editor you use, pyCharm or even Notepad++, often is setup to help you with indentation. You should check the settings and make sure it is set to replace tabs by spaces. When you hit return at the end of the line, the editor will "guess" what indentation you want. Many times it is correct, but sometimes, especially to END the block, you will need to change the indentation.

### Exercise

Create a new python file, practice-conditionals.py. Copy the last block of code and then modify it to allow you to input a value for x. Run it several times and use different values of x to trigger different conditional paths.


|[< Previous (Lists)](Lists.md) | [Day2](../README.md)| [Next (Loops) >](Loops.md) |
|----|----|----|