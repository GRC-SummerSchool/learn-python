|[< Previous (Lists)](Lists.md) | [Day1](../README.md)| [Next (Day2) >](../README.md) |
|----|----|----|
# Conditionals

Conditionals allow you to execute a portion of code when a condition is satisfied.

### If Statements
You can add an if clause to execute when the condition is satisfied:

```python
x = 10
if x <= 10:
  print("x is <= 10")
```

You can add else clause to execute when the condition is not satisfied:

```python
x = 10
if x <= 10:
  print("x is <= 10")
else:
  print("x is not <=10")
```

You can add additional elif (else if) clauses that are also evaluated. Only one condition 
will execute. Each condition is evaluated in the order listed.  Once a condition evaluates
true, any remaining conditions are skipped.

```python
x = 10
if x <= 10:
  print("x is <= 10")
elif x > 10:
  print("x is > 10") 
else:
  print("x is not <=10 and x is not > 10")
```

### Exercise

Modify the variable x's value to trigger different conditional paths.


|[< Previous (Lists)](Lists.md) | [Day1](../README.md)| [Next (Day2) >](../README.md) |
|----|----|----|