import runpy as np
import csv
from sklearn.preprocessing import StandardScaler

def import_data(file):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter="\n")
    csv_reader.__next__()
    data = []
    for row in csv_reader:
        aux = str(row).split(',')[1:]
        aux[-1] = aux[-1].split('\'')[0]
        aux = np.array(aux).astype(float)
        data.append(aux)
    return data

def standarize(inputs):
    return StandardScaler().fit_transform(inputs)