|[< Previous (Loops)](Loops.md) | [Day2](../README.md)| [Next (Day3 - Source Code Management) >](../Day3/GitOverview.md) |
|----|----|----|
# Dictionaries

In Python, a dictionary is an unordered collection of elements indexed by a key.  A dictionary can be thought of as a list where the index may be a string rather than a number, e.g. groceryDict["bread"] rather than myList[2]. 

Note, a key can be an integer, but it still acts as a look-up key. That is while both lists and dictionaries can be indexed with positive integers, only lists are ordered. Test the code below to see the output.

```python
a = {}
a["a"] = "A"
a[65] = "A"
print(a)
```
Consider the example dictionary:
```python
groceryDict = {
    "bread" : 3.09,
    "eggs" : 2.19,
    "milk" : 2.29
}
print(groceryDict)
```
Which produces the following output:
```
{'bread': 3.09, 'eggs': 2.19, 'milk': 2.29}
```

### Iteration

Dictionaries can be iterated over, accessing each element; however, the dictionary is unordered
so the order of iteration is subject to change as the contents of the dictionary change.
```python
groceryDict = {
    "bread" : 3.09,
    "eggs" : 2.19,
    "milk" : 2.29
}

for item, price in groceryDict.items():
    print("Item: %s, cost: %4.2f" % (item, price))
```

### Adding and Removing Elements

Items may be added or removed from dictionaries.

```python
groceryDict = {
    "bread" : 3.09,
    "eggs" : 2.19,
    "milk" : 2.29
}
groceryDict.pop("eggs")        # Removes eggs from the dictionary
groceryDict["bananas"] = 2.33  # Add new item to dictionary 

for item, price in groceryDict.items():
    print("Item: %s cost: %4.2f" % (item, price))
```
Running the above code will produce the following output:
```
Item: bread cost: 3.09
Item: milk cost: 2.29
Item: bananas cost: 2.33
```

### Exercise

Create a new python file, groceries.py.
Copy the code above and run. Add some additional print statements so you can see the original dictionary contents and the new dictionary contents. Include a separation between the two parts.


|[< Previous (Loops)](Loops.md) | [Day2](../README.md)| [Next (Day3 - Source Code Management) >](../Day3/GitOverview.md) |
|----|----|----|
