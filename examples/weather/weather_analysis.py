import csv
import matplotlib.pyplot as plt

import datetime
import matplotlib.ticker as mtick
from matplotlib.dates import DayLocator, DateFormatter, MonthLocator, HourLocator
import numpy as np

# Weather Data Columns
# StateCode,Division,YearMonth,PCP,TAVG,PDSI,PHDI,ZNDX,PMDI,CDD,HDD,SP01,SP02,SP03,SP06,SP09,SP12,SP24,TMIN,TMAX


# Read weather data into a list of objects
def load_data_objects (filename):
    data = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            object = {
                'StateCode' : int(row['StateCode']),
                'Division' : int(row['Division']),
                'YearMonth' : convert_yearmonth_to_date(row['YearMonth']),
                'PCP' : float(row['PCP']),
                'TAVG' : float(row['TAVG'])
            }
            data.append(object)
    return data

# Read weather data into a list a map based on Division as key
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

# Read weather data and extract selected columns into arrays
def load_data (filename):
    StateCode = []
    Division = []
    YearMonth = []
    PCP = []
    TAVG = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            StateCode.append(row['StateCode'])
            Division.append(row['Division'])
            YearMonth.append(row['YearMonth'])
            PCP.append(row['PCP'])
            TAVG.append(row['TAVG'])
    data = { }
    data['StateCode'] = StateCode
    data['Division'] = Division
    data['YearMonth'] = convert_yearmonth_to_date(YearMonth)
    data['PCP'] = PCP
    data['TAVG'] = TAVG
    data['numrows'] = len(YearMonth)
    return data

# Convert string of form yyyymm into a datetime object
def convert_yearmonth_to_date (ym):
    # 201002
    str_date = str(ym)
    str_yyyy = str_date[0:4]
    str_mm = str_date[4:6]
    d = datetime.datetime(int(str_yyyy), int(str_mm), 1)
    return d

# Extract attribuve from dictionary as an array
def create_attribute_array (data, attribute):
    a = []
    for x in data:
        a.append( x[attribute] )
    return a

# Print selected data
def print_data (data):
    for i in range(0,data['numrows']):
        print "{},{},{},{},{}".format(data['YearMonth'][i], data['StateCode'][i], data['Division'][i], data['PCP'][i], data['TAVG'][i])

# Convert Fahrenheight to Celsius
def convertFtoC (temperatureF):
    temperatureC = (float(temperatureF) - 32) * (5.0/9.0)
    return temperatureC

# COnvert temperatere values from array
def convertTemperatureArray (arrayF):
    arrayC = []
    for f in arrayF:
        c = convertFtoC( f)
        arrayC.append ( c )
    return arrayC

# Prompt the user for a temperature threshold
def prompt_for_threshold():
    t = input("Enter temperature threahold in Celsius: ")
    return float(t)

# Plot TAVG
def plot_tavg(array_YEARMONTH, array_TAVG):
    plt.plot(array_YEARMONTH, array_TAVG)
    plt.title('Average Temperature')
    plt.show()

# Plot TAVG and PCP for given division data
def plot_division (division_data):

    array__DIVISION = create_attribute_array(division_data, 'Division')
    array_YEARMONTH = create_attribute_array(division_data, 'YearMonth')
    array_TAVG = create_attribute_array(division_data, 'TAVG')
    array_PCP = create_attribute_array(division_data, 'PCP')

    plt.subplot(2, 1, 1)
    plt.plot(array_YEARMONTH, array_TAVG, 'ko-')
    # plt.gca().xaxis.set_major_locator(MonthLocator())
    # plt.gcf().autofmt_xdate()
    plt.title('Division ' + str(array__DIVISION[0]))
    plt.ylabel('TAVG (F)')

    plt.subplot(2, 1, 2)
    plt.plot(array_YEARMONTH, array_PCP, 'r.-')
    # plt.gca().xaxis.set_major_locator(MonthLocator())
    # plt.gcf().autofmt_xdate()
    plt.xlabel('YEARMONTH')
    plt.ylabel('PCP')

    plt.show()

# Calculate the mean of an array
def mean(a):
    return sum(a) / float(len(a))

def perform_analysis(data_map):

    stats = []
    for division in data_map:
        division_data = data_map[division]
        array_TAVG = create_attribute_array(division_data, 'TAVG')
        array_PCP = create_attribute_array(division_data, 'PCP')
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

def plot_statsX (station_stats):
    array_STATION = create_attribute_array(station_stats, 'station')
    array_MIN_TAVG = create_attribute_array(station_stats, 'min_TAVG')
    array_MAX_TAVG = create_attribute_array(station_stats, 'max_TAVG')
    array_MEAN_PCP = create_attribute_array(station_stats, 'mean_PCP')

    plt.subplot(2, 1, 1)
    plt.plot(array_STATION, array_MIN_TAVG, 'ko')
    plt.title('MIN_TAVG by Station')
    plt.ylabel('MIN_TAVG (F)')

    plt.subplot(2, 1, 2)
    plt.plot(array_STATION, array_MAX_TAVG, 'ko')
    plt.title('MAX_TAVG by Station')
    plt.ylabel('MAX_TAVG (F)')

    plt.show()

if __name__ == "__main__":

    weather_file_name = 'data/nystate_climate_indices_2010_2017.csv';
    # data = load_data(weather_file_name);
    # print_data(data)
    # tempsC = convertTemperatureArray(data['TAVG'])
    # thresholdC = prompt_for_threshold()
    # print "Threshold (C) = " + str(thresholdC)

    # data_objects = load_data_objects(weather_file_name)
    # print data_objects

    data_map = load_data_objects_into_map(weather_file_name)

    division10_data = data_map['10']

    station_stats = perform_analysis(data_map)

    # array_YEARMONTH = create_attribute_array(division10_data, 'YearMonth')
    # array_TAVG = create_attribute_array(division10_data, 'TAVG')
    # plot_tavg(array_YEARMONTH, array_TAVG)

    plot_division(division10_data)

    plot_min_max(station_stats)
