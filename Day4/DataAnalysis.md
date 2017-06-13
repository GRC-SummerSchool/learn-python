[< Previous (Git)](Git.md) | [Day4](../README.md)| [Next (Software Testing) >](Testing.md) |
|----|----|----|

# Data Analysis

Often we do some additional analysis on the data before plotting results. Let's extend the weather example to calculate the following for the data for each weather station:

* Calculate minimum and maximum temperate
* Calculate the average precipitation

## Calculating Stats For Each Station

In the weather example, the data has been loaded into a dictionary with the station (division) as the key. Let's write a new routine called ```perform_analysis()``` to iterate over the stations in the map. We can leverage the ```create_attribute_array()``` routine to extract the tempearature and precipitation values into an array:
```python
def perform_analysis(data_map):

    stats = []
    for division in data_map:
        division_data = data_map[division]
        array_TAVG = create_attribute_array(division_data, 'TAVG')
        array_PCP = create_attribute_array(division_data, 'PCP')

        # Calcualte stats for each station

    return stats
```

Python has some built-in functions for obtaining the min and max of an array. However, there is not a built-in function for the mean, so let's create a simple one:

```python
# Calculate the mean of an array
def mean(a):
    return sum(a) / float(len(a))
```

Let's compute our stats for a station:

```python
def perform_analysis(data_map):

    stats = []
    for division in data_map:
        division_data = data_map[division]
        array_TAVG = create_attribute_array(division_data, 'TAVG')
        array_PCP = create_attribute_array(division_data, 'PCP')

        # Calcualte stats for each station
        max_TAVG = max(array_TAVG)
        min_TAVG = min(array_TAVG)
        mean_PCP = mean(array_PCP)
    return stats
```

Now that we have the desired values in an array, we can return the statistics in an array of dictionary objects:

```python
def perform_analysis(data_map):

    stats = []
    for division in data_map:
        division_data = data_map[division]
        array_TAVG = create_attribute_array(division_data, 'TAVG')
        array_PCP = create_attribute_array(division_data, 'PCP')

        # Calcualte stats for each station
        max_TAVG = max(array_TAVG)
        min_TAVG = min(array_TAVG)
        mean_PCP = mean(array_PCP)

        station_stats = {
            "station" : int(division),
            "max_TAVG" : max_TAVG,
            "min_TAVG" : min_TAVG,
            "mean_PCP" : mean_PCP
        }
        stats.append(station_stats)
    print stats
    return stats
```

## Plotting the Results as a Bar Chart

Again, we leverage the  [matplotlib](https://matplotlib.org/) package to plot some charts.  Here we create a bar chart showing the min and max average temperatures for each station

```python
def plot_min_max (station_stats):
    array_STATION = create_attribute_array(station_stats, 'station')
    array_MIN_TAVG = create_attribute_array(station_stats, 'min_TAVG')
    array_MAX_TAVG = create_attribute_array(station_stats, 'max_TAVG')
    array_MEAN_PCP = create_attribute_array(station_stats, 'mean_PCP')

    N = len(array_STATION)
    ind = np.arange(N)  # the x locations for the groups

    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, array_MIN_TAVG, width, color='b')
    rects2 = ax.bar(ind + width, array_MAX_TAVG, width, color='r')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Average Temperature (F)')
    ax.set_title('Min and Max Temperature by Station')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(array_STATION)
    ax.legend((rects1[0], rects2[0]), ('Min', 'Max'))
    plt.show()
```

The resulting chart:

![](.DataAnalysis_images/4cceee54.png)
