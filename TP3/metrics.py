def accuracy (confussion_matrix, matrix_dim, element_position):
    rightAnswers = confussion_matrix[element_position][element_position];
    wrongAnwsers = 0
    for i in range(matrix_dim):
        for j in range(matrix_dim):
            if i != element_position and j!= element_position:
                wrongAnwsers+= confussion_matrix[i][j]
    return rightAnswers/wrongAnwsers

def precision(confussion_matrix, matrix_dim, element_position):        
    truePositives = confussion_matrix[element_position][element_position]
    totalPositives = 0
    for j in range(matrix_dim):
        totalPositives+= matrix_dim[element_position][j]
    return truePositives/totalPositives
    
def recall(confussion_matrix, matrix_dim, element_position):
    truePositives = confussion_matrix[element_position][element_position]
    realPositives = 0
    for i in range(matrix_dim):
        realPositives+= confussion_matrix[i][element_position]
    return truePositives/realPositives

def f1_score(confussion_matrix, matrix_dim, element_position):
    precisionResult = precision(confussion_matrix, matrix_dim, element_position)
    recallResult = recall(confussion_matrix, matrix_dim, element_position)
    return 2*precisionResult*recallResult/(precision + recall)






