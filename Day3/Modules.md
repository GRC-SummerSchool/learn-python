| [< Previous (Functions)](Functions.md) | [Day3](../README.md) | [Next (Software Testing) >](Testing.md) |
|----------------------------------------|----------------------|-----------------------------------------|

# Modules & Packages

Here are a couple of external references for more information on modules and packages:

- [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)
- [Python Modules](https://www.programiz.com/python-programming/modules)
  and [Python Packages](https://www.programiz.com/python-programming/package)
- (Interactive) [Modules and Packages](https://www.learnpython.org/en/Modules_and_Packages)

## Modules

```python
import antigravity
```

Outside the basic functionality, one of Python's strong points is its use of modules,
pre-written code & functions for a task. If you're trying to use linear algebra, or
connect to a USB device, or any number of tasks, chances are, someone has already written
that code. Because Python is open-source, the most common modules have been thoroughly
inspected and improved, just by being used so often.

You can import modules in a number of ways:

```python
import numpy
```

_Imports all functions from the "number Python" module_

```python
import numpy as np
```

_Imports all functions, and names the module "np"_

```python
from numpy import matrix
```

_Only imports the parts of the module that the code uses_

```python
from numpy import *
```

_Imports the whole module without giving it a name. *Not recommended!* Doing this can
cause issues down the line!_

Depending on the method you imported it with, you can then access the functions and
structures in the module with:

```python
m = numpy.matrix(...)
m = np.matrix(...)
m = matrix(...)
```

Some common modules:

1. *numpy* stands for "numbers python", and is used for arrays, matrices, and other
   linear algebra. Provides, among other things, exponential functions/natural log,
   constants such as pi, and various statistical functions such as mean and standard
   deviation.
2. *matplotlib* is the "math plotting library" used to generate plots with just a few lines.
3. *scipy* stands for "science python", and has many efficient packages for
   curve-fitting, optimization, and image processing.

## pip

Many modules come already installed in the Anaconda distribution of Python that you
downloaded prior to the class. However, if you ever come across a module that you'd
like you use but isn't already installed, Python provides an easy way to install it.
Simply go to a command line, and type in "pip install [module name]". Warning: this
won't work from the GE network, and you might need to check that you have permission
before installing it.

# Writing your own Modules

## \_\_name\_\_

When you run a Python script, all the code in the script executes from top to bottom.
Before executing the code, the Python interpreter defines some special variables.
One of the variables that the interpreter defines is **\_\_name\_\_**. If the script
is being run as the top level script passed to the interpreter, **\_\_name\_\_** will
be set to the value **"\_\_main\_\_"**; otherwise, **\_\_name\_\_** will be set to the
name of the module being defined.

### Why is this important?

This allows the application to define code that executes conditionally based on the
code being run directly or when imported as part of a larger project.

```python
def main():
    print("My main() function was just called")


if __name__ == '__main__':
    main()
```

### Defining and using modules

When you encounter an import statement, it searches for the named module, then it binds the results of that
search to a name in the local scope.

if you have a python file named `my_module.py`, you can import that file and bind to a variable.

```python
def my_function():
    print("my function was called")
```

```python
import my_module as m

m.my_function()
```

## Packages

More advanced modules may be broken up into several files, and a Python **Package** is simply a collection of
many modules. These may be imported by referring to the directory containing the module.

Consider the following directory tree:

```
my_package
    __init__.py       # Special file that Python interpreter inteprets this as a package
    mod_a.py          # Module a
    sub_package       # Sub package may include submodules, which have their own __init__.py file
        __init__.py
        submod_1.py   # Submodule 1
    mod_b.py          # Module b
```

If Python program `imports my_package.sub_package`, `my_package/__init__.py` will execute implicitly along
with `my_package/sub_package/__init__.py`.

| [< Previous (Functions)](Functions.md) | [Day3](../README.md) | [Next (Software Testing) >](Testing.md) |
|----------------------------------------|----------------------|-----------------------------------------|
