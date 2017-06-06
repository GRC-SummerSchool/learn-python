|[< Previous (Input)](Input.md) | [Day1](../README.md)| [Next (Conditionals) >](Conditionals.md) |
|----|----|----|
# Lists

In Python a list is an ordered collection of elements of any type. To define a list, simply include a 
comma separated list of elements between square brackets.
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers)      # prints the entire list on one line
```
Lists are indexed by numerical position, starting from 0, and going to (number of elements-1). To access 
the first element in the list

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[0])   # prints out just the first element
```

Lists may also be indexed from the end, using a negative index.  To access the last element in the 
list you may either use the index of the last element, or simply supply a negative index which counts 
backwards from the end of the list.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[len(numbers)-1])   # will output last element
print(numbers[-1])               # also prints out last element
```

Lists can be easily sliced using the [:] operator
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[:])    # will print the entire list
print(numbers[5:])   # will print from the 6th element to end of list
print(numbers[:5])   # will print from the first element up to but not including the 6th element
print(numbers[1:3])  # will print [ 2, 3 ]
print(numbers[9:10]) # will print [ ]
```

Slices can also be used to update the list
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[2:4] = [-3,-4]  # modify the 3rd and 4th element
print(numbers[:])       # prints [1, 2, -3, -4, 5, 6, 7, 8, 9]
```

Lists can be heterogeneous, allowing you to mix types at will.

```python
mix = [1, "cat", 3, "dog", 5, 6, 7, 8, "giraffe"]
print(mix)
```

To add to a list once its constructed, use the append(x) function
```python
mix = [1, "cat", 3, "dog", 5, 6, 7, 8, "giraffe"]

mix.append(10)
mix.append("lion")
print(mix)
```

To remove elements from the list once its constructed, use the pop(x) function
```python
mix = [1, "cat", 3, "dog", 5, 6, 7, 8, "giraffe"]

mix.pop(0)  # removes the first element (1)
mix.pop(-1) # removes the last element
mix.insert(0, "front of list")  # inserts element at supplied position (0)
print(mix)
```

Running the above example will produce the following output:
```
['front of list', 'cat', 3, 'dog', 5, 6, 7, 8]
```

|[< Previous (Input)](Input.md) | [Day1](../README.md)| [Next (Conditionals) >](Conditionals.md) |
|----|----|----|