|[< Previous (Intro to OOP)](introduction.md) | [Intermediate Python](../README.md)| [Next (Inheritance) >](inheritance.md) |
|----|----|----|

# Classes

A *class* is a structure made up of *attributes* (variables) and *methods* (functions). When you *initialize* an *instance* of a class,
you create a copy of the attributes that will be specific to that instance.

To initialize an instance, you simply use the class name, followed by any arguments that it needs. In a way, it's similar to calling a function.
By convention, class names start with a capital letter (and variable names or functions don't).

```python
rect1 = Rectangle(width=2,height=4)
rect2 = Rectangle(width=1,height=7)
```

To access an attribute or method from a class, use the syntax `instance.variable` or `instance.method()`. In the above example, you could reasonably
assume that the Rectangle class has width and height attributes, which you would access by

```python
rect1.width  # 2
rect1.height # 4
rect2.width  # 1
rect2.height # 7
```

Additionally, maybe the Rectangle class calculates the area for you, so despite the fact that it wasn't an explicit input, you could also run
```python
rect1.area  # 8
rect2.area  # 7
```

## Writing your own Class

A basic python class uses the `class` keyword, followed by an indented block representing the entire class. Inside the indented block are a number
of functions that represent the different methods. These behave like normal functions, with all the same capabilites, with 2 exceptions:
1. These is always a function `__init__(...)`, which is the initilizing function. This function runs when a new instance of the class is created.
2. The first argument to all methods, including `__init__` is a variable `self`. This variable represents the object "to itself". To access any of the
instance's attributes or methods, use `self` inside the class in the exact same way you might use `rect1` outside of the class. When using the class, you
don't need to explicitly pass in the `self` variable. You would pass in arguments and keyword arguments as if that `self` variable was not there. However,
`self` allows variables to persist from one function to the next. If it's a variable you want the class to remember, use `self`!

Below is an example of the basic structure of a class:
```python
class MyClass:

    def __init__(self,arg1,arg2,kwarg1=0):
        """Creates a class instance with 2 attributes"""
        self.attr1 = arg1
        self.attr2 = arg2 + kwarg1

    def method(self):
        return self.attr1

    def method_with_arg(self,arg):
        return self.method() + self.attr2 + arg

myInstance = MyClass(0,5)
myOtherInstance = MyClass(3,7,kwarg1=4)

print( myInstance.method() )
print( myOtherInstance.method_with_arg(-1) )

```

### Exercise
Write a Rectangle class that has width, height, area, and perimeter attributes, as well as a `grow` method that multiplies the area by a fixed amount
by adjusting the width/height without changing the aspect ratio.


## Static vs Dynamic variables

For some variables, it does not make sense to create a separate copy of the variable for each new instance of the class


|[< Previous (Intro to OOP)](introduction.md) | [Intermediate Python](../README.md)| [Next (Inheritance) >](inheritance.md) |
|----|----|----|