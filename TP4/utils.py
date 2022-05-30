import numpy as np
import csv
from sklearn.preprocessing import StandardScaler
from TP4.hopfield.letters import get_letter


def import_data(file):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter="\n")
    csv_reader.__next__()
    data = []
    countries = []
    for row in csv_reader:
        aux = str(row).split(',')[1:]
        aux[-1] = aux[-1].split('\'')[0]
        aux = np.array(aux).astype(float)
        data.append(aux)
        countries.append(str(row).split(',')[0])
    return countries, data


def standarize(inputs):
    return StandardScaler().fit_transform(inputs)


def get_headers(file):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter="\n")
    headers = csv_reader.__next__()
    aux = str(headers).split(',')[1:]
    aux[-1] = aux[-1].split('\'')[0]
    return aux


def get_network_patterns(letters):
    network_patterns = []
    for letter in letters:
        letter_bitmap = get_letter(letter.upper())
        network_patterns.append([i for sublist in letter_bitmap for i in sublist])
    return network_patterns


def get_noisy_pattern(network_patterns, letter, probability, conserve_pattern):
    if letter == -1:
        aux_idx = np.random.randint(0, len(network_patterns))
        noisy_pattern = network_patterns[aux_idx].copy()
    else:
        letter_bitmap = get_letter(letter.upper())
        noisy_pattern = [i for sublist in letter_bitmap for i in sublist]
    count = 0
    for i in range(len(noisy_pattern)):
        if probability >= np.random.uniform(0, 1):
            if noisy_pattern[i] == 1:
                if not conserve_pattern:
                    noisy_pattern[i] = -1
                    count += 1
            else:
                noisy_pattern[i] = 1
                count += 1
    print(f"Bits modified: {count}")
    return noisy_pattern
