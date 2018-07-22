|[< Previous (Classes)](classes.md) | [Intermediate Python](../README.md)| [Next (Magic Methods) >](magicmethod.md) |
|----|----|----|

# Class Inheritance

_This section uses examples and code from the previous section. Make sure you have the Rectangle and Circle classes completed before starting this section.
It's recommended to understand the [syntax for variable number of arguments](../Functions/argskwargs.md) too_

Inheritance is a programming technique that creates subclasses of a class. In the previous lesson, we worked with the Rectangle class and Circle class. Both
of these classes could be a subclass of a more generic Shape class, while a Square might be a subclass of Rectangle. By separating classes into parent-child
relationships (super- or sub-classes), you can create a "family tree": if Square is-a Rectangle, and Rectangle is-a Shape, then Square is-a Shape too. Code
that checks if a variable is a Shape will let both Squares and Rectangles pass:

```python
if not isinstance(myVar,Shape):
	# Works for Rectangles, Circles, Squares, Shapes, but not lists
	raise TypeError("Must be a Shape!")
	

if not isinstance(myVar,Rectangle):
	# Works for Rectangles or Squares but not Circles or Shapes
	raise TypeError("Must be a Rectangle!")
```

There are a couple of benefits to doing this. A subclass inherits all the methods and attributes of its parent class, keeping or rewriting (_overloading_)
methods, while adding new methods that may be more specific to the subclass.

A subclass looks for the most part like the classes from the previous section, except they list their parent class, and call the parent class' initializer. Once the initializer
runs, the `self` variable will have all the bells and whistles (and variables) from the parent class.

```python
class SubClass(SuperClass):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs) # Run the initializer of the superclass.
		
	def method1(self,arg1):
		# New method specific to SubClass
		# superclass.method1(0) would fail, but subclass.method1(0) works
		return arg1
```
In this template, the child class passed in all its arguments to the parent initalizer directly, but that doesn't have to be the case.
Let's take a look at some possible initializers for the Shape, Rectangle, and Square classes:

```python
class Shape:
	def __init__(self,nSides):
		self.nSides = nSides

class Rectangle(Shape):
	def __init__(self, width, height):
		super().__init__(4) # Shape.__init__(nSides) - Rectangle has 4 sides, always
		self.width = width
		self.height = height

class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side,side) # Rectangle.__init__(width, height)

# nSides inherited from Shape
rect = Rectangle(3,8)
print("# Sides: %i \t Width: %i \t Height: %i"%(rect.nSides,rect.width,rect.height))

# nSides inherited from Shape, width & height inherited from Rectangle
square = Square(5)
print("# Sides: %i \t Width: %i \t Height: %i"%(square.nSides,square.width,square.height))
```

Additionally, a child class can use all the methods of its parent. In the previous section, both the Circle and Rectangle
classes had an `isbigger` method. Instead of writing the same method twice, it could become part of their parent Shape class:
```python
class Shape:
	def __init__(self,nSides, area):
		self.nSides = nSides
		self.area = area
		
	def isbigger(self,otherShape):
		if not isinstance(otherShape,Shape):
			raise TypeError("Can only compare to other Shapes")
		
		# Returns True, False, or None if both are equal
		if self.area == otherShape.area:
			return None
		return self.area > otherShape.area

class Rectangle(Shape):
	def __init__(self, width, height):
		area = width * height
		super().__init__(4, area)
		
		self.width = width
		self.height = height
		
rect1 = Rectangle(4,6)
rect2 = Rectangle(3,8)

print(rect1.isbigger(rect2)) # Runs the Shape.isbigger method
```

### Overriding Methods
When a subclass has a method that's called the same as its parent class, calls from that class to the method will take the
subclass' version of the function. This is a technique known as overriding. This allows for subclasses to pick & choose which
behaviors from the parent they keep, and which they modify. The `__init__` method is an example of an overridden method. If
a class should use the exact same initializer as its parent, then there's no need to write a separate one. Like with the
initializer, the parent's overridden method can still be accessed by using `super()`.

If you followed the previous section to the end, you created width and height as properties in the Rectangle class. For a Square,
those setter methods would get modified so that when one changes, the other changes as well. However, depending on how you
wrote the Rectangle's `grow` method, that one might not need to be overridden. See [shapes.py](shapes.py) for the full implementation
of the Shape, Circle, Rectangle, and Square classes.

### Abstract Classes
Some classes are not intended to be used as-is, but to provide a template for all the classes that inherit it to follow. These
classes may implement some of the methods, but leave other crucial methods empty, intending for the child class to implement them.
In this example, Shape came close to being an abstract class- knowing something is a shape is not enough information to draw it
on a piece of paper, for example, even if we know the area. If that had been an important aspect of "using a shape", the classes
might have the following structure:

```python
class Shape:
	def draw(self,paper):
		"""To be overridden in children classes"""
		raise NotImplementedError
		
class Rectangle(Shape):
	def draw(self,paper):
		"""pseudo-code representing a rectangle being drawn on a paper"""
		paper.draw([self.width, self.height])

class Circle(Shape):
	def draw(self,paper):
		"""pseudo-code representing a circle being drawn on a paper"""
		paper.draw([self.radius])
```

Using an abstract base class (ABC) allows you to use the base class to define an _interface_- a set of methods which all members
of the class must have- even if there is not enough information to implement the full class in the "generic case" represented by
the base class. Consider a class representing a measurement instrument, that tracks its measurement history to determine if a temperature is stable, but
the connection could be over USB, Ethernet, or Serial Port. The different connections each require vastly different read_instrument methods,
but beyond that, the methods to track the history and the criteria to determine stability are the same for each subclass.


## Custom Exception Types
The simplest kind of inheritance is where the child behaves *exactly* like the parent, but is called by a different name.
This allows exception handling to filter for an error for a very specific circumstance, while leaving similar types of errors
alone. Although custom errors can be fully fleshed out like any subclass, they don't have to be:
```python
class ShapeAreaError(ValueError):
	"""Behave exactly like a ValueError"""
	pass
	
class Shape:
	def __init__(self,area):
		if area < 0: raise ShapeAreaError("Must have a positive area")
		
		sqrt(-1) # ValueError: Math domain error

try:
	area = 5
	shape = Shape(area)
except ShapeAreaError as e:
	print("We know how to handle this one")
	shape = Shape(-area)
except ValueError as e:
	print("Whoops, we need to debug!")
	
try:
	area = 5
	shape = Shape(area)
except ValueError as e:
	print("Catches ShapeAreaErrors as well, since there's nothing more specific to catch it")
	
``` 
When creating a custom error type, try to base it off of one of the existing exception types. In this case,
since the exception signified that the value of the area was incorrect, it was based off of `ValueError`.

|[< Previous (Classes)](classes.md) | [Intermediate Python](../README.md)| [Next (Magic Methods) >](magicmethod.md) |
|----|----|----|