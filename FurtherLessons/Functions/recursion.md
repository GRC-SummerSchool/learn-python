|[< Previous (Args and Kwargs)](argskwargs.md) | [Intermediate Python](../README.md)| [Next (Generators) >](generators.md) |
|----|----|----|

# Recursion

_Before beginning this section, you should be comfortable with [recursion](recursion.md)._

Recursion is a programming technique using functions that allows code to solve problems that would be difficult to do otherwise. It is most useful when using a divide-and-conquer strategy, when trying to navigate a "tree" structure (like a filesystem), or when the problem would otherwise require an arbitrary number of nested loops.

The definition of a recursive function is a function that calls itself. There are generally two parts to a recursive function: an ending condition, and a call to the function, with changed input. Like with loops, the ending condition is checked before the next piece of code runs; otherwise, you'll end up with something similar to an infinite loop... infinitely nested functions. Ending conditions are usually based on having a fixed outcome for a given input.

To begin with, consider the mathematical factorial function: 5! = 5 * 4!, 4! = 4 * 3!, and so on and so forth. Meanwhile, 1! = 1, without decreasing any further. Written as a recursive function:
```python
def factorial(x):
    print("Running factorial with x=%i..."%x)
    if x == 1:  # Ending condition
        print("Ending condition reached. Returning 1.")
        return 1
    else:  # Recursion
        ans = x * factorial(x-1)
        print("Returning %i * factorial(%i)."%(x,x-1))
        return ans

factorial(6)
```
Run this code to see how the function gets nested- none of the function calls return until the ending condition is reached.

Of course, something like a factorial could be easily calculated using a loop, and more efficiently too- repeating a loop is more efficient than calling a function.
Recursion really shows its power in situations where loops would be ill-suited.

## "Tree-structures"

Consider navigating a filesystem to find a specific type of file. Each folder may have multiple folders inside, which also have multiple folders inside. Using loops to complete the task quickly runs into issues- how many loops to have? What if one folder has 4 nested folders, and another one has none? This kind of problem is shaped like a tree, in that each branch might have 0 or more branches.

Using recursion, the problem becomes simpler. Here, the ending condition is "no more folders to investigate," while the function itself takes a folder's path as the input. The following code finds how many .md files there are in total in a folder:
```python
import os

def find_md(path):
    total = 0
    
    for filename in os.listdir(path):  # Lists all files in a folder
        if filename.endswith('.md'):
            total+=1
        elif os.path.isdir(path+filename):
            # If the file is a directory, repeat this same action for that folder
            total += find_md(path+filename+'/')
            
    return total

# Start the code
print(find_md('../../'))
```
Run this code, changing the starting folder to the path to this repository on your computer. At the time of writing this, there were 32 .md files. You may want to add in some print statements to understand what each part of the code is doing.

## Divide & Conquer
Some problems become much more difficult to solve depending on the size of the input. Sorting is one such type of problem. Sorting 2 numbers takes one comparison, sorting 3 numbers takes three, sorting 100 takes on the order of 10,000, worst-case.
Since the number of comparisons increases non-linearly, it makes much more sense to sort a smaller list, then merge two sorted lists, which can be done relatively easily (needing about as many comparisons as the length of the list). But what counts as a smaller list?
Dividing the list in half or even quarters might not be sufficient, if the original list was 1,000 long.

In this popular **Merge Sort** algorithm, the list gets divided in half recursively, until the list length is zero or one- an empty list, or a list of only one number is sorted by definition.
Then, each half of the list is 'zipped up': the first two numbers are compared, since those are the lowest in a sorted. Then, the larger of those is compared with the next number of the 'winning' list, and so on:
```
listA = [1, 3, 4, 6, 8]
listB = [0, 2, 5, 7, 9]

Compare 1 and 0... [0]
Compare 1 and 2... [0, 1]
Compare 3 and 2... [0, 1, 2]
Compare 3 and 5... [0, 1, 2, 3]
Compare 4 and 5... [0, 1, 2, 3, 4]
Compare 6 and 5... [0, 1, 2, 3, 4, 5]
```
The crux of this algorithm is that it _assumes it will work_- that by calling `merge_sort` on half of a list, the returned list will be sorted and ready for merging. Take a look at the full function:
```python
def merge_lists(listA,listB):
    # This function 'zips' two sorted lists
    result = []
    
    while len(listA)>0 and len(listB)>0:
        if listA[0] < listB[0]:
            result.append(listA[0])
            # Remove first element from listA
              # when all numbers are used up, listA will be empty, triggering end of loop
            listA.pop(0)
        else:
            result.append(listB[0])
            listB.pop(0)
		
    # One of these lists will be empty, and 'everything else' gets added to the end
    result = result + listA + listB
    
    return result
    
    
def merge_sort(sort_list):
    # Ending condition checked first
    if len(sort_list) < 2: #0 or 1
        return sort_list
        
    # Split list in half
    midpoint = int(len(sort_list)/2)
    listA = sort_list[:midpoint] # Excludes midpoint
    listB = sort_list[midpoint:] # Includes midpoint
    
    # Sort each half
    listA = merge_sort(listA)
    listB = merge_sort(listB)
    
    # Assume function worked, so listA and listB are sorted and can be merged
    return merge_lists(listA,listB)
```
Run the [speed test](recursion_speedtest.py) to see the difference in efficiency between merge sort and another sorting algorithm.

### Exercises

- Fibonacci's sequence is 0, 1, 1, 2, 3, 5... each number is the previous two numbers added together, with the first two numbers set to 0 and 1. Write a function to recursively calculate the nth Fibonacci number. 

  Keep an eye on the function calls. Why is this significantly _less_ efficient than using a loop?
  
- Instead of counting them, change the find_md code to create a dictionary of all the .md files that matches the following format:

  ```
  "FurtherLessons": {
    ".md":["exceptions.md","README.md"]
    "Functions": {
      ".md":["argskwargs.md","recursion.md"]
    }
  }
  ```
  
- Because of its function calls, Merge Sort performs worse than Swap Sort beneath a certain length. In [recursion_speedtest.py](recursion_speedtest.py), change the ending condition to use Swap Sort instead beneath that length. Why does this not invalidate the assumption used in the rest of the function?

|[< Previous (Args and Kwargs)](argskwargs.md) | [Intermediate Python](../README.md)| [Next (Generators) >](generators.md) |
|----|----|----|