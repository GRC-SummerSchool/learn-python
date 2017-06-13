[< Previous (Debugging)](Debugging.md) | [Day3](../README.md)| [Next (Modules) >](Modules.md) |
|----|----|----|
# Temperature Conversion

Temperature is commonly represented in degrees in units of Fahrenheit (F) or Celsius. Below are formulaey for converting between the units.

## Conversion formulas

Celsius to Fahrenheit:
```
T(°F) = T(°C) × 9/5 + 32
```

Fahrenheit to Celsius:
```
T(°C) = (T(°F) - 32) × 5/9
```

## Python Code to Convert Fahrenheit to Celsius

```
def convertFtoC (temperatureF):
    temperatureC = (float(temperatureF) - 32) * (5.0/9.0)
    return temperatureC
```

The keyword ```def``` defines the function name: ```convertFtoC```.
```temperatureF``` is an input argument to the function. We will call this function with different values.
```return temperatureC``` is the syntax to send the calculation back to the calling program.
In the above example, the input argment ```temperatureF``` is a string type. The ```float()``` operator is used to convert the string to a float before performing the conversion calculation.

After defining the function, we can use it to perform calculations.
## Python Code to call the conversion function

```
freezing = convertFtoC('32')
print 'freezing = ',freezing,'C'
```


### Exercise

Create a new file, temperatureConversion.py. Copy the function definition code above to your file. Add some calls to convert selected temperatures and print the results.



### Main program

So far we have just run one python file at a time. As projects get complex, you may have several functions and put the definitions in separate files. When you want to run them, one file needs to be the starting point. This is __main__. To include code to run only when the file is the starting point add a section checking if this is the main program like this:

```
if __name__ == "__main++":
    print('this is the main program')
```

### Exercise
Move the calls to the temperature function into a __main__ section. Leave the def part of the function outside the if statement block. Run this program.

Create a new program with just an if __name__ == "__main__": block. Put different code in this main section. Some suggestions:
Create a loop to ask the user for input values and then call the convert function.

Use conditionals to print comment about the temperatures, like "that is cold!", "that is a nice temperature for playing golf", "that is hot, let's go swimming", etc.
Divide the function and main into two python files and run again.

Run this program and see the different output. 

[< Previous (Debugging)](Debugging.md) | [Day3](../README.md)| [Next (Modules) >](Modules.md) |
|----|----|----|
