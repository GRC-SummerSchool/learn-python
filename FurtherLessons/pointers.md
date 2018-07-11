|[< Previous (Exceptions)](exceptions.md) | [Intermediate Python](README.md)| [Next (Args and Kwargs) >](Functions/argskwargs.md) |
|----|----|----|

# Pointers

There's a fundamental difference between the two blocks of code:

```python
x = 3
y = x
y = y + 7

print("x = %i, y = %i"%(x,y)) # x = 3, y = 10
```
Here, `y` is initially set to the value of `x`, 3, then is changed, while `x` remains the same.
When you run this, nothing unexpected happens. Now try running this next section:
```python
x = [3]
y = x
y[0] = y[0] + 7

print("x[0] = %i, y[0] = %i"%(x[0],y[0])) # x[0] = 10, y[0] = 10
```
The value of `x` has changed, even though it was never set explicitly by the program. This is because lists, like many other variable types in python, are **pointers**.

A pointer is a variable that is actually an address in the computer's memory. When you copy the variable (in `y = x`, for example), you are copying the address, not the value.
It's the difference between working on a text document on your computer or on Google docs.
When you want to share a document that's on your computer with a coworker, you stick it in an email and send it to them. Any changes they make will only apply to their copy. The `int`, `boolean`, `float`, `string` and other basic variable types behave like this.
However, when you want to share a document that's on Google drive with someone, you email them a link. Whether you or the other person makes edits, the changes will be visible to anyone using that link to access the document. Lists, dictionaries, and pretty much all other variable types use this behavior.

Understanding when a variable gets copied by value and when it gets copied by reference is key when writing functions, where the arguments can be any variable type. The example functions so far have all performed simple calculations, but what about functions that modify their input arguments?
Unintentionally modifying a variable that was a pointer can have unexpected (frustrating) consequences. But with a solid understanding of the difference, many programmers use it intentionally.
```python
def sum_list(li):
    result = li[0]
    for i in li[1:]:
        result += i

    return result

list1 = [1, 2, 3, 4, 5]
print(sum_list(list1)) # 15
print(list1) # [1, 2, 3, 4, 5]

list2 = [[1,2], [3,4], [5]]
print(sum_list(list2)) #[1, 2, 3, 4, 5] - expected result, summing arrays concatenates them
print(list2) # [[1, 2, 3, 4, 5], [3, 4], [5]] - unexpected and undesired behavior
```
What happened in with `list2`? For both `list1` and `list2`, when they are passed into the function, they are passed as pointers. Any changes to li in the function will change the original array.
Then, when the initial value for `result` is set, it copies the first value of `li`; which, in the case of `list2`, is itself a pointer. Now, any changes to `result` changes `li[0]`... which changes `list2[0]`.

Fixing this is easy enough- all that's needed is to make sure that `result` is not a pointer, but a copy. Fortunately, python already provides functions to do that. Making sure that `result` doesn't point to anything that already exists is enough to make sure that modifying it doesn't lead to weird behavior:
```python
import copy
def sum_list(li):
    result = copy.copy(li[0])
    for i in li[1:]:
        result += i

    return result
```
When you copy a list that contains pointers (like `list2`, a list of lists), a new list is created, but the pointers inside still point to their same variables. To truly create an entirely new list, use `copy.deepcopy` instead, which copies the contents as well as the list.

**Why pointers at all?** Programmers have a saying: "It's not a bug if it's a feature." Pointers speed up execution of a program, and save on memory: a list of one million numbers does not get copied again...and again...and again with each function call.
Although they might take getting used to, they are also incredibly powerful in helping different aspects of your program stay in sync with each other. Look at file I/O, for example:
```python
fo =  open("data.txt",mode='w') # File Object
fo2 = fo

names = ["Alice","Bob","Cathy","Dylan"]

fo.write(names[0]+"\n")
fo.write(names[1]+"\n")


fo2.write(names[2]+"\n")
fo2.write(names[3])

fo.close()
```
Files work by having cursors. When text gets written, the cursor advances, and overwrites what comes after it (typically, the end of the file).
Because the file object is a pointer, both `fo` and `fo2` are the same cursor: hence, the `fo2` cursor advances as `fo` writes to the file. If not, whichever cursor was ahead would get constantly overwritten; the two variables would be warring over the contents of the file.
Even if that was desired for some reason, the specific mechanics of how data gets written versus actually saved would make multiple cursors unpredictable.
But since file objects are pointers, operations that move the cursor, or save the file, or any number of things, stay in sync across the whole program, without additional effort on the part of the programmer.
(Plus, if multiple cursors were really desired, there's always the ability to use the `open` function multiple times.)


### Exercises

- Change fo2 in the above example to `fo2 = open("data.txt",mode='w')`, and see what happens with two file objects. Can you mimic the behavior of having just one? You may want to use the `fo.flush()` (to save) and the `fo.seek()` (to move the cursor) functions.


|[< Previous (Exceptions)](exceptions.md) | [Intermediate Python](README.md)| [Next (Args and Kwargs) >](Functions/argskwargs.md) |
|----|----|----|