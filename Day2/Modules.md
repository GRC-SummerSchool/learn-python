|[< Previous (Debugging)](Debugging.md) | [Day2](../README.md)| [Next (Day3) >](../README.md) |
|----|----|----|
# Modules

## \_\_main\_\_

Unlike other languages, Python has no predefined entry point (e.g. main). 
When you run a Python script, all the code in the script executes from top to bottom.
Before executing the code, the Python interpreter defines some special variables.
One of the variables that the interpreter defines is **\_\_main\_\_**. If the script
is being run as the top level script passed to the interpreter, **\_\_main\_\_** will 
be set set to the value **"\_\_main\_\_"**; otherwise, **\_\_main\_\_** will be set to the 
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

if you have a python file named mymodule.py, you can import that file and bind to a variable.
```python
def myfunction() :
    print("my function was called")
```
```python
import mymodule as m

m.myfunction()
```

### Defining modules from directory

More advanced modules may be broken up into several files. These may be imported by referring to the directory
containing the module.

Consider the following directory tree:
```
my-module
    __init__.py  # Special file that runs when module is loaded
    a.py
    submodule    # Modules may include submodules, which have their own __init__.py file
        __init__.py
    b.py
```

If Python program imports my-module.submodule, my-module/__init__.py will execute implicitly along
with my-module/submodule/__init__.py. 










