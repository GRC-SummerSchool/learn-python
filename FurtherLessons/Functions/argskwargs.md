|[< Previous (Exceptions)](../exceptions.md) | [Intermediate Python](README.md)| [Next (Recursion) >](recursion.md) |
|----|----|----|

# Arguments and Keyword Arguments

_Before beginning this section, you should be comfortable with the [basics of functions](../../Day3/Functions.md)._

Computer functions, like math functions, can have multiple arguments:

```python
import math
def r(x,y):
    return math.sqrt(x**2 + y**2)
    
def sin(x,y):
    return y/r(x,y)
    
def cos(x,y):
    return x/r(x,y)
    
u = 3.0
v = 4.0

print("sin(%g,%g) is %g"%(u,v,sin(u,v)))      # sin(3,4) is 0.8
print("sin(%g,%g) is not %g"%(u,v,sin(v,u)))  # sin(3,4) is not 0.6
print("cos(%g,%g) is %g"%(u,v,cos(u,v)))      # cos(3,4) is 0.6
```

While that hopefully sounds like a trivial statement, it's important to understand that when a user calls the function, they must supply all the arguments required, and in the same order as specified in the function definition.
For that reason, arguments like these are also sometimes referred to as "positional arguments."

Python has a second type of argument, called "keyword arguments," where a default value for the argument is supplied in the function definition. Since there is a default value, supplying the argument when calling the function becomes optional.
Additionally, when a function has more than one keyword argument, a user can specify which of the values they're setting- the rest get left as the default value.
When a function has keyword arguments, all of them are defined _after_ the positional arguments, since all of the positional arguments must still be given.

```python
def greet(name,greeting="Hello",ending="."):
    print(greeting+", "+name+ending)
    
greet("Alice") # Hello, Alice.
greet("Bob",greeting="Good morning") # Good morning, Bob.
greet("Cathy",ending='!') # Hello, Cathy!
greet("Dylan",greeting="How are you",ending="?") # How are you, Dylan?
greet("Ellen",ending="",greeting="Later") # Later, Ellen
greet(greeting="Greetings") # Error because of missing 'name' argument
```

Positional arguments and keyword arguments are usually abbreviated to args and kwargs respectively.

## *Args and **Kwargs

If you've used python's plotting module (matplotlib), you might have noticed something weird:
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x)
plt.plot(x,y1)
plt.plot(x,y2,'y.--')
plt.show()
```
When calling plot, it will accept 1, 2, or 3 arguments. Acutally, it will accept any number of triplets of arguments, for `x`, `y`, `format`:
```python
plt.plot(x,y1,'m--',x,y2,'y.--')

```
The plot function specifies an argument in the function definition for "and all the rest of the arguments," allowing it to have a flexible number of input arguments.
This is done by marking one of the arguments with a `*` in the name. There can be only one "et cetera" for the arguments, and one for the keyword arguments:
```python
def plot(*args,**kwargs):
	print("This is the function definition for matplotlib.pyplot.plot.")
```
Inside the function, the variable `args` (without the star) is now an array containing all the spare arguments, while `kwargs` (again, without the stars) is a dictionary of the keyword arguments, `{"keyword":value}`.
The two arguments are called `*args` and `**kwargs` by convention, but it's the `*` that's the important part. (Technically, `**kwargs` doesn't need 2 asterisks either, but again, convention.)

This can also be reversed to feed in a list or dictionary to a function. Take a quick look at [matplotlib.pyplot.plot list of available keywords](https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot).
There's about 40 different keywords to specify everything from the line width to the marker edge color. Now imagine you're writing a function to help with some aspect of plotting, but you'd like to leave the line-plotting options open for the user to specify.
You don't need to do this:
```python
def plot_helper(x,y,agg_filter=None,alpha=1.0,animated=False,antialiased=True,axes=None,clip_on=False,clip_path=None,color='you get the idea'):
    plt.plot(x,y,agg_filter=agg_filter,alpha=alpha,animated=animated,antialiased='honestly, I quit midway through writing this out')
```
Or this:
```python
def plot_helper(x,y,**kwargs):
    if not "agg_filter" in kwargs:
        kwargs["agg_filter"] = None # Default value
    if not "alpha" in kwargs:
        kwargs["alpha"] = 1.0 # Default value

    plt.plot(x,y,agg_filter=kwargs["agg_filter"],alpha=kwargs["alpha"]) # Now do this for all 42 possible keywords 
```
Instead, this (thankfully) works, giving the plot function the `args` list as positional arguments, and the `kwargs` dictionary as keyword arguments:
```python
def plot_helper(x,y,*args,**kwargs):
    plt.plot(x,y,*args,**kwargs)
```
Here's a more thorough example:
```python
import numpy as np
import matplotlib.pyplot as plt

def plot_helper1(x,y,*args,**kwargs):
    plt.subplot(2,1,1)
    plt.plot(x,y,*args,**kwargs)

def plot_helper2(x,y,*args,**kwargs):
    plt.subplot(2,2,3)

    plot_x = x[y>0]
    plot_y = y[y>0] # Prevent log(0)-type errors

    plt.plot(plot_x,np.log(plot_y),*args,**kwargs)

def plot_helper3(x,y,*args,**kwargs):
    plt.subplot(2,2,4)

    plot_x=x[y>=0]
    plot_y=y[y>=0] # Prevent sqrt(-1)-type errors

    plt.plot(plot_x,np.sqrt(plot_y),*args,**kwargs)

x = np.arange(0,10,0.2)
y = x**2

plot_helper1(x,y)
plot_helper2(x,y)
plot_helper3(x,y)

y2 = np.exp(x)
plot_helper1(x,y2,'m--')
plot_helper2(x,y2,'m--')
plot_helper3(x,y2,'m--')

y3 = y + y2
style = {"color":"g","linestyle":":","marker":"o"}
plot_helper1(x,y3,label="Combined",**style)
plot_helper2(x,y3,label="Combined",**style)
plot_helper3(x,y3,label="Combined",**style)

plt.show()
```

## Pointers

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
Write a function that takes an arbitrary number of lists and pads each list in-place to the length of the longest one. The default padding should be `None`, but could be changed.

Change fo2 in the above example to `fo2 = open("data.txt",mode='w')`, and see what happens with two file objects. Can you mimic the behavior of having just one? You may want to use the `fo.flush()` (to save) and the `fo.seek()` (to move the cursor) functions.