| [< Previous (Loops)](Loops.md) | [Day2](../README.md) | [Next (Day3 - Debugging) >](../Day3/Debugging.md) |
|--------------------------------|----------------------|---------------------------------------------------|

# Dictionaries

In Python, a dictionary is an unordered collection of elements indexed by a key. A dictionary can be thought of as a
list where the index may be a string rather than a number, e.g., `grocery_dict["bread"]` rather than
`my_list[2]`.

Note, a key can be an integer, but it still acts as a look-up key. That is while both lists and dictionaries can be
indexed with positive integers, only lists are ordered. Test the code below to see the output.

```python
a = {}  # Another way to declare a dictionary: a = dict()
a["a"] = "A"
a[65] = "A"
print(a)
```

Consider the example dictionary:

```python
grocery_dict = {
    "bread": 3.09,
    "eggs": 2.19,
    "milk": 2.29
}
print(grocery_dict)
```

Which produces the following output:

```
{'bread': 3.09, 'eggs': 2.19, 'milk': 2.29}
```

### Iteration

Dictionaries can be iterated over, accessing each element; however, the dictionary is unordered
so the order of iteration is subject to change as the contents of the dictionary change.

```python
grocery_dict = {
    "bread": 3.09,
    "eggs": 2.19,
    "milk": 2.29
}

for item, price in grocery_dict.items():
    print(f"Item: {item}, cost: {price:.2f}")
```

### Adding and Removing Elements

Items may be added or removed from dictionaries.

```python
grocery_dict = {
    "bread": 3.09,
    "eggs": 2.19,
    "milk": 2.29
}
grocery_dict.pop("eggs")  # Removes eggs from the dictionary
grocery_dict["bananas"] = 2.33  # Add new item to dictionary 

for item, price in grocery_dict.items():
    print(f"Item: {item}, cost: {price:.2f}")
```

Running the above code will produce the following output:

```
Item: bread, cost: 3.09
Item: milk, cost: 2.29
Item: bananas, cost: 2.33
```

### Exercise

Create a new Python file, `groceries.py`.
Copy the code above and run. Add some additional print statements so you can see the original dictionary contents and
the new dictionary contents. Include a separation between the two parts.

| [< Previous (Loops)](Loops.md) | [Day2](../README.md) | [Next (Day3 - Debugging) >](../Day3/Debugging.md) |
|--------------------------------|----------------------|---------------------------------------------------|
