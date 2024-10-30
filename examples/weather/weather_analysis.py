import csv
import datetime

import matplotlib.pyplot as plt
import numpy as np


# Weather Data Columns
# StateCode,Division,YearMonth,PCP,TAVG,PDSI,PHDI,ZNDX,PMDI,CDD,HDD,SP01,SP02,SP03,SP06,SP09,SP12,SP24,TMIN,TMAX


# Read weather data into a list of objects
def load_data_objects(filename):
    data = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_object = {
                'StateCode': int(row['StateCode']),
                'Division': int(row['Division']),
                'YearMonth': convert_yearmonth_to_date(row['YearMonth']),
                'PCP': float(row['PCP']),
                'TAVG': float(row['TAVG'])
            }
            data.append(data_object)
    return data


# Read weather data into a list a map based on Division as key
def load_data_objects_into_map(filename):
    data_object_map = {}
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            division = row['Division']
            if division not in data_object_map:
                data = []
                data_object_map[division] = data

            data = data_object_map[division]

            data_object = {
                'StateCode': int(row['StateCode']),
                'Division': int(row['Division']),
                'YearMonth': convert_yearmonth_to_date(row['YearMonth']),
                'PCP': float(row['PCP']),
                'TAVG': float(row['TAVG'])
            }

            data.append(data_object)

    return data_object_map


# Read weather data and extract selected columns into arrays
def load_data(filename):
    state_code = []
    division = []
    year_month = []
    pcp = []
    tavg = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            state_code.append(row['StateCode'])
            division.append(row['Division'])
            year_month.append(row['YearMonth'])
            pcp.append(row['PCP'])
            tavg.append(row['TAVG'])
    data = {
        'StateCode': state_code,
        'Division': division,
        'YearMonth': convert_yearmonth_to_date(year_month),
        'PCP': pcp,
        'TAVG': tavg,
        'numrows': len(year_month)
    }
    return data


# Convert string of form yyyymm into a datetime object
def convert_yearmonth_to_date(ym):
    # 201002
    str_date = str(ym)
    str_yyyy = str_date[0:4]
    str_mm = str_date[4:6]
    d = datetime.datetime(int(str_yyyy), int(str_mm), 1)
    return d


# Extract attribute from dictionary as an array
def create_attribute_array(data, attribute):
    a = []
    for x in data:
        a.append(x[attribute])
    return a


# Print selected data
def print_data(data):
    for i in range(0, data['numrows']):
        print("{},{},{},{},{}".format(data['YearMonth'][i], data['StateCode'][i], data['Division'][i], data['PCP'][i],
                                      data['TAVG'][i]))


# Convert Fahrenheit to Celsius
def convert_f_to_c(temperature_f):
    temperature_c = (float(temperature_f) - 32) * (5.0 / 9.0)
    return temperature_c


# Convert temperature values from array
def convert_temperature_array(array_f):
    array_c = []
    for f in array_f:
        c = convert_f_to_c(f)
        array_c.append(c)
    return array_c


# Prompt the user for a temperature threshold
def prompt_for_threshold():
    t = input("Enter temperature threshold in Celsius: ")
    return float(t)


# Plot TAVG
def plot_tavg(array_yearmonth, array_tavg):
    plt.plot(array_yearmonth, array_tavg)
    plt.title('Average Temperature')
    plt.show()


# Plot TAVG and PCP for given division data
def plot_division(division_data):
    array_division = create_attribute_array(division_data, 'Division')
    array_yearmonth = create_attribute_array(division_data, 'YearMonth')
    array_tavg = create_attribute_array(division_data, 'TAVG')
    array_pcp = create_attribute_array(division_data, 'PCP')

    plt.subplot(2, 1, 1)
    plt.plot(array_yearmonth, array_tavg, 'ko-')
    # plt.gca().xaxis.set_major_locator(MonthLocator())
    # plt.gcf().autofmt_xdate()
    plt.title('Division ' + str(array_division[0]))
    plt.ylabel('TAVG (F)')

    plt.subplot(2, 1, 2)
    plt.plot(array_yearmonth, array_pcp, 'r.-')
    # plt.gca().xaxis.set_major_locator(MonthLocator())
    # plt.gcf().autofmt_xdate()
    plt.xlabel('YEARMONTH')
    plt.ylabel('PCP')

    plt.show()


# Calculate the mean of an array
def mean(a):
    return sum(a) / float(len(a))


# Calculate statistics for each station
def perform_analysis(data_map):
    stats = []
    for division in data_map:
        division_data = data_map[division]
        array_tavg = create_attribute_array(division_data, 'TAVG')
        array_pcp = create_attribute_array(division_data, 'PCP')
        max_tavg = max(array_tavg)
        min_tavg = min(array_tavg)
        mean_pcp = mean(array_pcp)
        station_stats = {
            "station": int(division),
            "max_TAVG": max_tavg,
            "min_TAVG": min_tavg,
            "mean_PCP": mean_pcp
        }
        stats.append(station_stats)
    print(stats)
    return stats


# Plot min/max TAVG by station as a bar chart
def plot_min_max(station_stats):
    array_station = create_attribute_array(station_stats, 'station')
    array_min_tavg = create_attribute_array(station_stats, 'min_TAVG')
    array_max_tavg = create_attribute_array(station_stats, 'max_TAVG')
    # array_mean_pcp = create_attribute_array(station_stats, 'mean_PCP')

    n = len(array_station)
    ind = np.arange(n)  # the x locations for the groups

    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, array_min_tavg, width, color='b')
    rects2 = ax.bar(ind + width, array_max_tavg, width, color='r')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Average Temperature (F)')
    ax.set_title('Min and Max Temperature by Station')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(array_station)
    ax.legend((rects1[0], rects2[0]), ('Min', 'Max'))
    plt.show()


# Plot min and max TAVG by station as line charts
def plot_stats_temps_by_station(station_stats):
    array_station = create_attribute_array(station_stats, 'station')
    array_min_tavg = create_attribute_array(station_stats, 'min_TAVG')
    array_max_tavg = create_attribute_array(station_stats, 'max_TAVG')
    # array_mean_pcp = create_attribute_array(station_stats, 'mean_PCP')

    plt.subplot(2, 1, 1)
    plt.plot(array_station, array_min_tavg, 'ko')
    plt.title('MIN_TAVG by Station')
    plt.ylabel('MIN_TAVG (F)')

    plt.subplot(2, 1, 2)
    plt.plot(array_station, array_max_tavg, 'ko')
    plt.title('MAX_TAVG by Station')
    plt.ylabel('MAX_TAVG (F)')

    plt.show()


if __name__ == "__main__":
    # Load the data into a map/dictionary by division/station
    weather_file_name = 'data/nystate_climate_indices_2010_2017.csv'
    weather_data_map = load_data_objects_into_map(weather_file_name)

    # Perform analysis: compute min(TAVG_, max(TAVG), mean (PCP) by division
    weather_station_stats = perform_analysis(weather_data_map)

    # Extract the data for division 10
    division10_data = weather_data_map['10']

    # TAVG and PCP for given division/station data
    plot_division(division10_data)

    # Plot min and max TAVG by station/division
    plot_min_max(weather_station_stats)
