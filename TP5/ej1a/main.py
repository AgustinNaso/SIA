from seaborn import heatmap
import matplotlib.pyplot as plt
import numpy as np
from TP5.resources.fonts import font_1
from TP5.helpers.font_helper import to_bin_array, print_letter
from TP5.helpers.mlp_helper import create_multilayer_perceptron_and_train

nested_set = np.array(list(map(to_bin_array, font_1)))
sets = np.array(list(map(np.concatenate, nested_set)))
layers = np.array([35, 20, 2, 20, 35])
learning_rate = 0.0005
epoch: int = 100

perceptron = create_multilayer_perceptron_and_train(sets, sets, learning_rate, epoch, layers, 100, momentum=True)
# outputs = perceptron.test_input(sets)
midPoints = perceptron.enc_bulk(sets)
print(f'element     mid points')
for i in range(len(midPoints)):
    print(f'{i}    {midPoints[i]}')

decs = perceptron.dec_bulk(midPoints)
print(f'element     errors')
for i in range(len(decs)):
    print(f'{i}    {sets[i] - decs[i]}')


# for i in range(len(outputs)):
#     print(sets[i])
#     print(outputs[i])
#     print_letter(sets[i])
#     print_letter(outputs[i])

