import csv
import numpy as np

def normalize(output):
    min_expected = min(output)
    max_expected = max(output)
    return np.array(list(map(lambda x: 2 * ((x - min_expected) / (max_expected - min_expected)) - 1, output)))

def import_data(file):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter=" ")
    data = []
    for row in csv_reader:
        entry = [float(a) for a in row if a != '']
        data.append(entry)
    return data
