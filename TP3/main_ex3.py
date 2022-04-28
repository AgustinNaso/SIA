import csv
import constants


def import_data(file, data_type):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter=" ")
    data = []
    for row in csv_reader:
        if data_type == constants.MULTIPLE:
            entry = [float(a) for a in row if a != '']
            data.append(entry)
        else:
            data.append(row[-1])
    return data


inputs = import_data('data/ex3_training_set', constants.MULTIPLE)
outputs = import_data('data/ex3_expected_output', constants.SINGLE)
print(outputs)
