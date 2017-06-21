|[< Previous (Conditionals)](Conditionals.md) | [Day2](../README.md)| [Next (Dictionaries) >](Dictionaries.md) |
|----|----|----|
# Loops

Python supports _for_ loops and _while_ loops.

### For Loop
You can iterate through all the elements in a list using a _for_ loop:

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

You may specify a range of numbers to iterate over using the range function:
Note - you can leave off the step parameter if you choose to increment by 1

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

A _while_ loop will repeat until the loop condition isn't satisfied:

```python
count = 1
while count < 10:
    print(count)
    count = count + 1
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

### Infinite Loops

If a chunk of code is taking much longer than you expected it to, it might be that you
created an infinite loop - a loop whose ending condition will never be reached.

```python
count = 1
while count < 10:
    print(count)
    #Oops! I forgot to add one!
```

It's always useful to know ahead of time how to stop your code from running if this
happens!

### Exercise

Modify your practice-conditionals.py file from Day 1 to run the code in a loop.

### Additional Information

There are two keywords you can use inside a loop to change how it operates.

_break_ will exit the loop immediately, skipping any conditions or the remainder
of the list:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in numbers:
    if n == 6:
        print("I hate the number 6! I quit!")
        break
    print(n)
```
will produce the following output:
```
1
2
3
4
5
I hate the number 6! I quit!
```

_continue_ will skip the rest of the code inside the loop, and move immediately to the
next iteration of the loop, either moving to the next item on the list, or re-evaluation
the condition:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in numbers:
    if n == 6:
        print("You can't make me say that number!")
        continue
    print(n)
```
will produce the following output:
```
1
2
3
4
5
You can't make me say that number!
7
8
9
```

### Further Practice

Create a new python file, guess.py. Write a guessing game that generates a random number, and prompts 
the user for input until they guess correctly. Generate a random number between 1 and 10 by 
using the following code snippet:

```python
from random import randint

answer = randint(1,10)
```

|[< Previous (Conditionals)](Conditionals.md) | [Day2](../README.md)| [Next (Dictionaries) >](Dictionaries.md) |
|----|----|----|