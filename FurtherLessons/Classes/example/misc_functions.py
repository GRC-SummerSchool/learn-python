import re


def get_temperature_from_filename(filename):
    match = re.match(r'^\D*([\d\.]+)K\.txt$',filename,re.IGNORECASE)
    if match:
        temp = match.groups()[0]
        return float(temp)

    else: return None


def parse_firstline(filename):

    with open(filename,'r') as fin:
        firstline = fin.readline()

    r = re.compile(r"\D+: \d+")
    matches = r.findall(firstline)

    metadata = {key.strip(): float(value) for key, value in [m.split(': ') for m in matches]}

    return metadata
