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

The initilization function can be as simply or complex as needed, and not all the input arguments need to be saved. Consider:
- An initializer that takes a filename as the input, and reads & parses the file to set its attributes
- An initializer that opens a connection to an instrument, and 'remembers' the open connection
- An initializer that creates instances of a different class.

  *A `Library` class takes the names of the librarians and a filename listing its books. It creates a `Librarian` instance for each of the librarians, and a `Book` instance for each book listed in the file. It has the attributes `myLibrary.librarians` and `myLibrary.catalog`, and a method `myLibrary.checkout(booktitle)`*

When writing methods, aside from any arguments the user passes in, you also have access to any variables that have been assigned to `self`.

You can also access a method by using the class name and explicitly passing in the instance: `MyClass.method_with_arg(myInstance, 2)`

### Exercise
- Write a Rectangle class that has width, height, area, and perimeter attributes. Add a `grow` method that multiplies the area by a fixed amount
by adjusting the width/height without changing the aspect ratio. Add a `isbigger` method that takes another rectangle as an input, and returns True if
the current rectangle has a larger area, False otherwise.
- Look at the data files in [the IV-Curve example](../../examples/iv-curves). The first column represents the voltage a measurement was taken at, the rest represent current.
What would the data file look like as a class? What attributes might it have?

## Static vs Dynamic variables
In the examples up to this point, the classes have all used attributes and methods that would not make sense without creating an instance of the class first. How can you have the
width and height of the concept of a rectangle? These kinds of variables are called *dynamic* variables and methods, since they are only defined at runtime.

However, there are some variables that do make sense outside of an instance. These are called *static*, since they always exist. Consider a `Circle` class: the raidus is specific
to the instance, but pi is always pi, regardless of a 'physical' circle to define it. To define a static variable, simply declare it outside of the initializer.

```python
class Circle:
    PI = 3.14159

    def __init__(self,r):
        self.radius = r
        self.area = Circle.PI * r**2 # access Circle class' static attribute
        self.area = self.PI * r**2 # since 'self' is a Circle, this also works!
```
By convention, constants are typically named in all caps. A static variable doesn't have to be constant, however. When one instance changes the value of a static variable, all instances & future instances
of the class will see the new value. A common use of this is to use a static variable to automatically create a unique ID number for each instance:
```python
class ClubMemeber:

    ID = 1

    def __init__(self,name):
        self.name = name
        self.id = self.ID
        self.ID += 1

alice = ClubMember("Alice")
bob = ClubMember("Bob")

print(alice.id) # 1
print(bob.id)   # 2
```
Classes can also have static methods, which are classes defined with the `@staticmethod` decorator, and class methods, defined with the `@classmethod` decorator. A static method doesn't have a `self` argument, while a class method replaces `self` with `cls`, representing the class instead of the instance.
Static methods behave the same as module-level functions, except that you can call them from either the class name or a class instance, and are generally used to create "utility" methods.
Class methods are typically used to write "factory methods"- methods that return an instance of the class, but constructed in vastly different ways, especially if there's a significant difference
in input arguments because of it.
```python
class ClubMember:

    def __init__(self, name, id, address, start_date):
        self.name = name
        self.id = id
        self.address = address
        self.start_date = start_date

    @classmethod
    def from_database(cls,database_connection, id):
        name, address, start_date = database_connection.get(id)
        return cls(name, id, address, start_date)

    @classmethod
    def create_new(cls,database_connection, name, address)
        id, start_date = database_connection.add_new(name, address)
        return cls(name, id, address, start_date)

    @staticmethod
    def id_exists(id,database_connection):
        if id in database_connection.get_ids():
            return True
        else:
            return False

alice_id = 1
if ClubMember.id_exists(alice_id, db_conn):
    alice = ClubMember.from_database(db_conn, alice_id)
else:
    alice = ClubMember.create_new("Alice", "1 First Street, 12345")
```
### Excersices
Complete the Circle class to match the interface of the Rectangle class from earlier. The `isbigger` method for both classes should work regardless
of whether the input was a Circle or a Rectangle instance.

## Getters, Setters, and Properties
In many non-Python languages, a group of methods called *getters* and *setters* are a standard way of manipulating attributes. The basic idea is that
a getter method would return the value, while a setter method would actually change the value. It's more 'pythonic' in most cases to simply directly
access the variable, whether retrieving or assigning the value. Below is an example of how a class with getter and setters might look like:
```python
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def set_title(self,title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self,author):
        self.author = author

book = Book("The Name of the Wind","Patrick Rothfuss")

print(book.get_title())
print(book.title)       # This is easier to use than all those extra methods!
```
However, the concept of getters and setters in python gets wrapped into a class' *properties*.
These are special variables that run a defined function when retrieved or modified, acting on the front end like any other variable.
A property might make use of an internal 'hidden' variable, or might be used to syncronize several variables with a change (Using a single
underscore at the beginning of a attribute or method signifies that it's intended for class-internal use only).
```python
class Kelvin:
    def __init__(self,temp):
        self.T = temp # This runs self._set_T(temp)

    def toCelcius(self):
        return self.T - 273.15 # This uses self._get_T

    def _set_T(self,temp):
        """Kelvin must have temperatures > 0!"""
        assert temp > 0
        self._T = temp

    def _get_T(self):
        return self._T # An internal variable to holt the actual value

    T = property(_set_T,_get_T)

t1 = Kelvin( 77 )
print( t1.toCelcius )
t1.T = -196.15 # Raises an error
```

### Execerses
- Turn the `radius` of the circle into a property. When the radius of the circle changes, the area should automatically
change with it. What small extra step do you need to do to make that work with the width/height of the Rectangle?

- For fun: Take a look at the GameCharacter class in [gamechar.py](gamechar.py). Which are the static variables? The static or dynamic methods?
Write a Team class containing a list of characters on that team, and a method for determining how many members of the team are still alive.
Use the two classes to write a mini-game!


|[< Previous (Intro to OOP)](introduction.md) | [Intermediate Python](../README.md)| [Next (Inheritance) >](inheritance.md) |
|----|----|----|