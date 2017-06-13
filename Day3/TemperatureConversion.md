[< Previous (Debugging)](Debugging.md) | [Day3](../README.md)| [Next (File I/O) >](CSVFiles.md) |
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

In the above example, the input argment ```temperatureF``` is a string type. The ```float()``` operator is used to convert the string to a float before performing the conversion calculation.


[< Previous (Debugging)](Debugging.md) | [Day3](../README.md)| [Next (File I/O) >](CSVFiles.md) |
|----|----|----|
