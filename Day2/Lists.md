|[< Previous (Day1 Input)](../Day1/Input.md) | [Day2](../README.md)| [Next (Conditionals) >](Conditionals.md) |
|----|----|----|
# Lists

In Python a list is an ordered collection of elements of any type. To define a list, simply include a 
comma separated list of elements between square brackets.
```python
numbers = [1, 20, 3, 40, 5, 60, 7, 80, 9]

print(numbers)      # prints the entire list on one line
```
Lists are indexed by numerical position, starting from 0, and going to (number of elements-1). To access 
the first element in the list

```python
numbers = [1, 20, 3, 40, 5, 60, 7, 80, 9]

print(numbers[0])   # prints out just the first element
```

Lists may also be indexed from the end, using a negative index.  To access the last element in the 
list you may either use the index of the last element, or simply supply a negative index which counts 
backwards from the end of the list.

```python
numbers = [1, 20, 3, 40, 5, 60, 7, 80, 9]

print(numbers[len(numbers)-1])   # will output last element
print(numbers[-1])               # also prints out last element
```

Lists can be easily sliced using the [:] operator, which returns a portion of a list as another list.
```python
numbers = [1, 20, 3, 40, 5, 60, 7, 80, 9]

print(numbers[:])    # will print the entire list
print(numbers[5:])   # will print from the 6th element to end of list
print(numbers[:5])   # will print from the first element up to but not including the 6th element
print(numbers[1:3])  # will print [ 20, 3 ]
print(numbers[9:10]) # will print [ ]
```

Slices can also be used to update the list
```python
numbers = [1, 20, 3, 40, 5, 60, 7, 80, 9]

numbers[2:4] = [-3,-4]  # replace the elements starting at 
                        # 3rd location through 4th (up to but not including 5th)
                        # with the contents on right-hand side
print(numbers[:])       # prints [1, 20, -3, -4, 5, 60, 7, 80, 9]
#some more variations to try:
numbers[2:4] = [-3,-4,-5,-6,-7]
numbers[5:] = ['cat', 'dog', 100]
numbers[4:4] = ['a', 'b', 'c']
```

Lists can be heterogeneous, allowing you to mix types at will.

```python
mix = [1, "cat", 3, "dog", 5, 6, 7, 8, "giraffe"]
print(mix)
```

To add elements to the end of a list once it is constructed, use the append(x) function.
```python
mix = [1, "cat", 3, "dog", 5, 6, 7, 8, "giraffe"]

mix.append(10)
mix.append("lion")
print(mix)
[1, 'cat', 3, 'dog', 5, 6, 7, 8, 'giraffe', 10, 'lion']
```

To remove elements from the list once it is constructed, use the pop(x) function.  Without an argument, pop removes the last element of the list.
```python
mix.insert(0, "front of list")  # inserts element at supplied position (0)
print(mix)
mix = [1, "cat", 3, "dog", 5, 6, 7, 8, "giraffe"]
mix.pop(0)  # removes the first element
1
```

```python
mix.pop()  # removes the last element
'giraffe'
```

```python
print(mix)
['cat', 3, 'dog', 5, 6, 7, 8]
```
To insert elements in a list at a specific location, use the function insert(n, value).  Continuing with list "mix":
```python
mix.insert(0, "front of list")  # inserts element at index 0
print(mix)
['front of list', 'cat', 3, 'dog', 5, 6, 7, 8]
```

### Exercise

Create a new python file (play-with-lists.py). Copy the above code into the new file and run it to see if you get the same results.

|[< Previous (Day1 Input)](../Day1/Input.md) | [Day2](../README.md)| [Next (Conditionals) >](Conditionals.md) |
|----|----|----|
