| [< Previous (Variables)](Variables.md) | [Day1](../README.md)| [Next (Input)>](Input.md) |
|----|----|----|

## Expressions

An ***expression*** is a statement that describes an operation. There are many different kinds of expressions. The simplest ones look like math operations. The operands can be constants or variables. 

Parentheses can be used to indicate and control the ***order of precedence***, that is what operations are performed first.

### Typical Math Operations

```python
i = 5 + 3 - 2.3 
k = 7 * 45 + 5 ** 3       #  ** is the power operation, so 5 cubed.
w = (7 * (45 + 5)) ** 3   #  note the reordering of operations.
```

### String operations

String variables also have operations, like concatenation. This is indicated by the + symbol.

```python
str1 = "abc"     
str2 = "defghij"
strlong = str1 + str2    
```

### Conversion operations

Sometimes you need to convert a variable from one data type to another. We saw that python will figure out the type by the assignment. If you need to change it you use a conversion function. For instance, to convert from a string to an integer, use the int() function.

Some common and interesting conversion functions:

| Function | Behavior |
|----|----|
| int | convert to an integer |
| float | convert to a real number |
| str | convert to a string (for printing or concatenating with other strings) |
| hex | convert to a string in hexadecimal format prefixed by 0x |
| ord | return the integer code for a single character |
| chr | return the character for a given unicode integer value |



```python
str_number = "123"
a = int(str_number)
b = 7 * a
print("7 * a = ", b)
```

### Exercises

1. Practice writing different types of expressions.
2. Convert between different data types and print your results.


| [< Previous (Variables)](Variables.md) | [Day1](../README.md)| [Next (Input)>](Input.md) |
|----|----|----|
