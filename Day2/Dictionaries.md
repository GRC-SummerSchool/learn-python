|[< Previous (Loops)](Loops.md) | [Day2](../README.md)| [Next (Debugging) >](Debugging.md) |
|----|----|----|
# Dictionaries

In Python, a dictionary is an unordered collection of elements indexed by a non-numeric key.  A dictionary can be thought of as a list where the index is a string rather than a number, e.g. myDict["bread"] rather than myList[2].
```python
dict = {
    "bread" : 3.09,
    "eggs" : 2.19,
    "milk" : 2.29
}
print(dict)
```
Which produces the following output:
```
{'bread': 3.09, 'eggs': 2.19, 'milk': 2.29}
```

### Iteration

Dictionaries can be iterated over, accessing each element; however, the dictionary is unordered
so the order of iteration is subject to change as the contents of the dictionary change.
```python
dict = {
    "bread" : 3.09,
    "eggs" : 2.19,
    "milk" : 2.29
}
for item, price in dict.items():
    print("Item: %s cost: %4.2f" % (item, price))
```

### Adding and Removing Elements

Items may be added or removed from dictionaries.

```python
dict = {
    "bread" : 3.09,
    "eggs" : 2.19,
    "milk" : 2.29
}
dict.pop("eggs")        # Removes eggs from the dictionary
dict["bananas"] = 2.33  # Add new item to dictionary 


for item, price in dict.items():
    print("Item: %s cost: %4.2f" % (item, price))
```
Running the above code will produce the following output:
```
Item: bread cost: 3.09
Item: milk cost: 2.29
Item: bananas cost: 2.33
```

### Exercise

Create a new python file - groceries.py.
Copy the code above and run. Add some additional print statements so you can see the original dictionary contents and the new dictionary contents. Include a separation between the two parts.


|[< Previous (Loops)](Loops.md) | [Day2](../README.md)| [Next (Debugging) >](Debugging.md) |
|----|----|----|
