[< Previous (Functions)](TemperatureConversion.md) | [Day3](../README.md)| [Next (Plotting) >](SimplePlotting.md) |
|----|----|----|
# CSV Files

Data is often stored in a type of filed called a CSV file. CSV stands for comma separated value file, where data has been organized into columns, and are separated by delimiter, usually a comma.

For example, the first few rows of the weather data CSV file (../examples/weather/nystate_climate_indices_2010_2017.csv) looks like:
```
StateCode,Division,YearMonth,PCP,TAVG,PDSI,PHDI,ZNDX,PMDI,CDD,HDD,SP01,SP02,SP03,SP06,SP09,SP12,SP24,TMIN,TMAX
30,1,201001,2.8,21.8,0.59,2.19,0.95,2.1,0,1339,0.45,0.56,-0.26,0.44,0.75,0.41,1.01,14.5,29.2
30,9,201001,2.42,22.4,-0.25,2.39,-0.36,1.86,0,1321,-0.32,0.06,-0.66,-0.08,0.51,0.51,1.52,16,28.8
30,2,201001,2.77,21.9,0.08,1.67,-0.05,0.66,0,1336,0.09,0.1,-0.67,0.22,1.1,0.5,1.07,14.2,29.5
30,4,201001,1.99,31.3,1.6,1.6,-1.58,0.84,0,1045,-1.08,0.63,0.03,-0.15,1.1,0.47,0.84,24.2,38.3

```

Before doing any analysis or plotting of the data in the CSV file, the data is first read and loaded into memory.

There are many ways to load data in Python. One way is to represent the data in each row of the CSV as a dictionary and create an array of Dictionary elements. See [Dictionaries](../Day2/Dictionaries.md) to learn more about creating dictionaries.

## Reading data from a CSV file: Array of Dictionary Elements

Python routine to load weather CSV file into a python array of dictionary elements:
```python
def load_data_objects (filename):
    data = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            object = {
                'StateCode' : row['StateCode'],
                'Division' : row['Division'],
                'YearMonth' : row['YearMonth'],
                'PCP' : row['PCP'],
                'TAVG' : row['TAVG']
            }
            data.append(object)
    return data
```


## Reading data from a CSV file: Dictionary or Map

The weather data contains data for weather stations throughout New York State. These weatehr stations are called Divisions. Below we still load the data into an array of Dictionary objects, but we create a map based on Division to store each array.

Python routine to load weather CSV file into a python dictionary (map) using Division as key
```python
def load_data_objects_into_map (filename):
    map = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_division = row['Division']
            if (row_division not in map):
                data = []
                map[row_division] = data

            data = map[row_division]

            object = {
                'StateCode' : int(row['StateCode']),
                'Division' : int(row['Division']),
                'YearMonth' : convert_yearmonth_to_date(row['YearMonth']),
                'PCP' : float(row['PCP']),
                'TAVG' : float(row['TAVG'])
            }

            data.append(object)

    return map
```

### Exercise

Create a new file, readweather.py. Copy the two function definitions into your file.

Create a main section to call one or the other and print some information so that you are confident the function worked. Use the debugger to also check the data is loaded.


[< Previous (Functions)](TemperatureConversion.md) | [Day3](../README.md)| [Next (Plotting) >](SimplePlotting.md) |
|----|----|----|
