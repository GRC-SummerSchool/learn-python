# Convert Fahrenheight to Celsius
def convertFtoC (temperatureF):
    temperatureC = (float(temperatureF) - 32) * (5.0/9.0)
    return temperatureC

def test_conversion():
    assert (convertFtoC(32) == 0)
    assert (convertFtoC(212) == 100)

