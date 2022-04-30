import csv
import numpy as np


def normalize(output):
    min_expected = min(output)
    max_expected = max(output)
    return np.array(list(map(lambda x: 2 * ((x - min_expected) / (max_expected - min_expected)) - 1, output)))


def import_data(file, quantity):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter=" ")
    data = []
    entry = []
    row_count = 0
    for row in csv_reader:
        if quantity == 1:
            entry = [float(a) for a in row if a != '']
            data.append(entry)
        else:
            row_count += 1
            for a in row:
                if a != '':
                    entry.append(float(a))
            if row_count == quantity:
                data.append(entry)
                entry = []
                row_count = 0
    return data
