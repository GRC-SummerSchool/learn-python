# Convert Fahrenheit to Celsius
def convert_f_to_c(temperature_f):
    temperature_c = (float(temperature_f) - 32) * (5.0 / 9.0)
    return temperature_c


def test_conversion():
    assert (convert_f_to_c(32) == 0)
    assert (convert_f_to_c(212) == 100)
