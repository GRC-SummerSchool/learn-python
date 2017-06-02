|[< Previous (Day3)](../README.md) | [Day4](../README.md)| [Next (Dictionaries) >](Dictionaries.md) |
|----|----|----|
# Loops
# Prompting the User For Input

At times, some input is needed from the user. Python provides the ```input("Message...")``` method to print a message and wait fot the user to enter a value from the console.

## Example: Prompting for  Temperature Threshold Value

```
def prompt_for_threshold():
    t = input("Enter temperature threahold in Celsius: ")
    return float(t)
```

By default all inputs are typed as strings. Above, we convert the value to a float and return it.
