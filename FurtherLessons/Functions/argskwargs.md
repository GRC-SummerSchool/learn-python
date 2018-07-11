|[< Previous (Pointers)](../pointers.md) | [Intermediate Python](../README.md)| [Next (Recursion) >](recursion.md) |
|----|----|----|

# Arguments and Keyword Arguments

_Before beginning this section, you should be comfortable with the [basics of functions](../../Day3/Functions.md) and [pointers](../pointers.md)._

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

### Exercises
- Write a function `add` that adds two or more inputs. How can you ensure there are at least two inputs?
- Write a function `add_and_multiply` that calls `add`, then multiplies the result by a multiplier that defaults to 1. Why is several multipliers with each their own default a hassle?
  - Bonus: Raise an exception if any of the arguments are [not numbers](https://stackoverflow.com/questions/3441358/what-is-the-most-pythonic-way-to-check-if-an-object-is-a-number).

|[< Previous (Pointers)](../pointers.md) | [Intermediate Python](../README.md)| [Next (Recursion) >](recursion.md) |
|----|----|----|