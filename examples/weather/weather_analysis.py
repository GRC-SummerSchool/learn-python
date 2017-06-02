import csv
import matplotlib.pyplot as plt

# Weather Data Columns
# StateCode,Division,YearMonth,PCP,TAVG,PDSI,PHDI,ZNDX,PMDI,CDD,HDD,SP01,SP02,SP03,SP06,SP09,SP12,SP24,TMIN,TMAX


# Read weather data and extract selected columns into arrays
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
    data['YearMonth'] = YearMonth
    data['PCP'] = PCP
    data['TAVG'] = TAVG
    data['numrows'] = len(YearMonth)
    return data

def create_attribute_array (data, attribute):
    a = []
    for x in data:
        a.append( x[attribute] )
    return a

def print_data (data):
    for i in range(0,data['numrows']):
        print "{},{},{},{},{}".format(data['YearMonth'][i], data['StateCode'][i], data['Division'][i], data['PCP'][i], data['TAVG'][i])

def convertFtoC (temperatureF):
    temperatureC = (float(temperatureF) - 32) * (5.0/9.0)
    return temperatureC

def convertTemperatureArray (arrayF):
    arrayC = []
    for f in arrayF:
        c = convertFtoC( f)
        arrayC.append ( c )
    return arrayC

def prompt_for_threshold():
    t = input("Enter temperature threahold in Celsius: ")
    return float(t)

if __name__ == "__main__":

    weather_file_name = 'data/nystate_climate_indices_2010_2017.csv';
    # data = load_data(weather_file_name);
    # print_data(data)
    # tempsC = convertTemperatureArray(data['TAVG'])
    # thresholdC = prompt_for_threshold()
    # print "Threshold (C) = " + str(thresholdC)

    data_objects = load_data_objects(weather_file_name)
    print data_objects

    array_TAVG = create_attribute_array(data_objects, 'TAVG')
    print array_TAVG