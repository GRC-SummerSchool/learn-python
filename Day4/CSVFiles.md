[< Previous (Weather Analysis Overview)](WeatherAnalysisOverview.md) | [Day4](../README.md)| [Next (Plotting) >](SimplePlotting.md) |
|----|----|----|
# File I/O: CSV Files

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

There are many ways to load data in Python from a file. The basics consist opening your file, reading the data and putting it into local variables and then closing the file. Using the with statement on open, simplifies this by eliminating the need to explicitly close the file. All the statements performed with the open file are nested in a block in the with statement.

One of common way to represent the data from the file is to make a dictionary object for each row and an array of all the rows. The csv module has a DictReader function to do help us do that. 

To refresh your understanding of dictionaries, go to [Dictionaries](../Day2/Dictionaries.md).
To refresh your understanding of modules, go to [Modules](../Day3/Modules.md).

## Reading data from a CSV file: Array of Dictionary Elements

We will import the csv module at the top of the file. Next we have to open the file so the DictReader function can process it. We use the with statement and put the rest of our commands in the block. We call the csv.DictReaader function with the csvfile variable from the open statement to get a single row of data. We create our own object and add to our array.

Python routine to load weather CSV file into a python array of dictionary elements:
```python
import csv

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

At the end, the result of the function an array - one element for each row in your csv file - of dictionary objects. Each dictionary object has the header of the row as the name of an element in the dictionary and the value from the row as the value. The data result looks like this (formatted instead of one line):

```
[{'StateCode': '30', 'Division': '1', 'YearMonth': '201001', 'PCP': '2.8', 'TAVG': '21.8'}, 
 {'StateCode': '30', 'Division': '9', 'YearMonth': '201001', 'PCP': '2.42', 'TAVG': '22.4'}, 
 {'StateCode': '30', 'Division': '2', 'YearMonth': '201001', 'PCP': '2.77', 'TAVG': '21.9'}, 
 
 all the rest of the data...
 
 {'StateCode': '30', 'Division': '1', 'YearMonth': '201704', 'PCP': '4.23', 'TAVG': '49.7'}
]

```

## Reading data from a CSV file: Dictionary or Map

The weather data contains data for weather stations throughout New York State. These weather stations are called Divisions. In our plotting exercise, we are going to plot data for a specific weather station (division), so we want to load the data into an array of Dictionary objects for each individual weather station. To do this, we'll create a new function that will create an array of objects keyed by the division code where each entry is the array of observations for that station.

The result will be data that looks like (formatted instead of one line...):
```
{'1': [{'StateCode': 30, 
        'Division': 1, 
        'YearMonth': datetime.datetime(2010, 1, 1, 0, 0), 
        'PCP': 2.8, 
        'TAVG': 21.8}, 
       {'StateCode': 30, 
        'Division': 1,
        'YearMonth': datetime.datetime(2010, 2, 1, 0, 0), 
        'PCP': 1.66, 
        'TAVG': 23.4}, 

        
       {'StateCode': 30, 
        'Division': 9, 
        'YearMonth': datetime.datetime(2017, 4, 1, 0, 0), 
        'PCP': 5.25, 
        'TAVG': 49.6}
      ], 
 '2': [{'StateCode': 30, 
        'Division': 2, 
        'YearMonth': datetime.datetime(2010, 1, 1, 0, 0), 
        'PCP': 2.77, 
        'TAVG': 21.9}, 
       {'StateCode': 30, 
        'Division': 2, 
        'YearMonth': datetime.datetime(2010, 2, 1, 0, 0), 
        'PCP': 3.37, 
        'TAVG': 24.3}, 
        
        85 more entries...
           
       {'StateCode': 30, 
        'Division': 5, 
        'YearMonth': datetime.datetime(2017, 4, 1, 0, 0), 
        'PCP': 3.85, 
        'TAVG': 52.1}
      ], 
      
 similar structures for divisions '3', '4', '5', '6', '7', '8', '9'
 
 '10': [{'StateCode': 30, 
         'Division': 10, 
         'YearMonth': datetime.datetime(2010, 1, 1, 0, 0), 
         'PCP': 2.06, 
         'TAVG': 22.8}, 
        {'StateCode': 30, 
         'Division': 10, 
         'YearMonth': datetime.datetime(2010, 2, 1, 0, 0), 
         'PCP': 2.06, 
         'TAVG': 24.5}, 
       
       85 more entries...
        
        {'StateCode': 30, 
         'Division': 6, 
         'YearMonth': datetime.datetime(2017, 4, 1, 0, 0), 
         'PCP': 5.57, 
         'TAVG': 48.7}
       ]
}
```

Below we still load the data into an array of Dictionary objects, but we create a dictionary (we'll call it map) with the Division as the key to store each array. If we haven't had read a row for that division, we need to put a new array with that key in the map first. Because our data is not ordered by division, each time we read a row, we need to get the object from our dictionary to append to. Then we can add the entry to that data array object. 

Also, we want a nicer way to format the month, so we create a new function to convert the YearMonth from a number like 201004 to a string like '2010, 04'.

Python routines to load weather CSV file into a python dictionary (map) using Division as key and convert yearmonth number into a string.

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

# Convert string of form yyyymm into a datetime object
def convert_yearmonth_to_date (ym):
    # 201002
    str_date = str(ym)
    str_yyyy = str_date[0:4]
    str_mm = str_date[4:6]
    d = datetime.datetime(int(str_yyyy), int(str_mm), 1)
    return d
```

### Exercise

Create a new file, readweather.py. Copy the function definitions into your file.

Create a main section to call one or the other and print some information so that you are confident the function worked. Use the debugger to also inspect variables as the data is loaded.


[< Previous (Weather Analysis Overview)](WeatherAnalysisOverview.md) | [Day4](../README.md)| [Next (Plotting) >](SimplePlotting.md) |
|----|----|----|
