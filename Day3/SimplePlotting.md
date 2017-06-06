[< Previous (Debugging)](Debugging.md) | [Day2](../README.md)| [Next (Day3) >](../README.md) |
|----|----|----|

# Simple Plotting

Now that we have loaded the weather data, let's create a few plots. There are many plotting packages available.
Here we are going to use the [matplotlib](https://matplotlib.org/) package to create some plots.


## Using matplotlib

Before we can use the matplotlib library, we must import it
```python
import matplotlib.pyplot as plt
```

## Simple X, Y Plot

To create an X, Y plot, the arrays of the X and Y values are simply passed to the ```plot()``` function

```python
def plot_tavg(array_YEARMONTH, array_TAVG):
    plt.plot(array_YEARMONTH, array_TAVG)
    plt.title('Average Temperature')
    plt.show()
```

![](.SimplePlotting_images\ec4101b5.png)

## Multiple sub-plots

Often it is useful to plot several plots together. Below two subplots are created, one for Average Temperture and another for Precipitation.

```python
def plot_division (division_data):

    array__DIVISION = create_attribute_array(division_data, 'Division')
    array_YEARMONTH = create_attribute_array(division_data, 'YearMonth')
    array_TAVG = create_attribute_array(division_data, 'TAVG')
    array_PCP = create_attribute_array(division_data, 'PCP')

    plt.subplot(2, 1, 1)
    plt.plot(array_YEARMONTH, array_TAVG, 'ko-')
    plt.title('Division ' + str(array__DIVISION[0]))
    plt.ylabel('TAVG (F)')

    plt.subplot(2, 1, 2)
    plt.plot(array_YEARMONTH, array_PCP, 'r.-')
    plt.xlabel('array_YEARMONTH')
    plt.ylabel('PCP')

    plt.show()
```

![](.SimplePlotting_images\52bf7c6c.png)
