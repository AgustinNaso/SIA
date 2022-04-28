import numpy as np


def accuracy(confussion_matrix, matrix_dim, element_position):
    right_ans = confussion_matrix[element_position][element_position];
    wrong_ans = 0
    for i in range(matrix_dim):
        for j in range(matrix_dim):
            if i != element_position and j != element_position:
                wrong_ans += confussion_matrix[i][j]
    return right_ans / wrong_ans


def precision(confusion_matrix, matrix_dim, element_position):
    true_positives = confusion_matrix[element_position][element_position]
    total_positives = 0
    for j in range(matrix_dim):
        total_positives += matrix_dim[element_position][j]
    return true_positives / total_positives


def recall(confusion_matrix, matrix_dim, element_position):
    true_positives = confusion_matrix[element_position][element_position]
    real_positives = 0
    for i in range(matrix_dim):
        real_positives += confusion_matrix[i][element_position]
    return true_positives / real_positives


def f1_score(confusion_matrix, matrix_dim, element_position):
    precision_value = precision(confusion_matrix, matrix_dim, element_position)
    recall_value = recall(confusion_matrix, matrix_dim, element_position)
    return 2 * precision_value * recall_value / (precision_value + recall_value)


def getMetrics(results, expected, input, matrix_dim):
    confussion_matrix = np.zeros(shape=(matrix_dim, matrix_dim))
    # corro x cantidad de veces para armar la matriz
