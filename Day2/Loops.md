|[< Previous (Day2)](../README.md) | [Day2](../README.md)| [Next (Dictionaries) >](Dictionaries.md) |
|----|----|----|
# Loops

In Python supports for loops and while loops.

### For Loop
You can iterate through all the elements in a list using a for loop:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in numbers:
    print(n)
```
will produce the following output:
```
1
2
3
4
5
6
7
8
9
```

You specify a range of numbers to iterate over using the range function:
Note - you can leave off the step if you choose to increment by 1

```python
for n in range(2,12,2):   # Starts at 2, less than 12, step by 2
    print(n)
```
will produce the following output:
```
2
4
6
8
10
```

### While Loops

A while loop will repeat until the loop condition isn't satisfied

```python
count = 1
while count < 10:
    print(count)
    count = count + 1
```

|[< Previous (Day2)](../README.md) | [Day2](../README.md)| [Next (Dictionaries) >](Dictionaries.md) |
|----|----|----|