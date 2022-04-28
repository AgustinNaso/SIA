def accuracy(confusion_matrix, matrix_dim, element_position):
    right_ans = confusion_matrix[element_position][element_position];
    wrong_ans = 0
    for i in range(matrix_dim):
        for j in range(matrix_dim):
            if i != element_position and j != element_position:
                wrong_ans += confusion_matrix[i][j]
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


# Ejercicio 1 - XOR: 1 -1
# Ejercicio 2 - par/impar: par = 1, impar = -1
# Ejercicio 3 - digito: 1 0
def get_confusion_matrix(classes, real_output, expected_output):
    matrix = [[0, 0], [0, 0]]
    for i in range(len(real_output)):
        if real_output[i] == expected_output[i]:
            if real_output[i] == classes[0]:
                matrix[0][0] += 1
            else:
                matrix[1][1] += 1
        else:
            if real_output == classes[0]:
                matrix[1][0] += 1
            else:
                matrix[0][1] += 1
    return matrix
