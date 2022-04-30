import json
import numpy as np

from TP3.ex3_1 import ex1
from TP3.ex3_2 import ex2
from TP3.ex3_3 import ex3

with open("ex3_config.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

exercise = int(jsonObject["exercise"])
exerciseFile = str(jsonObject["config_file"][exercise])

if exercise == 0:
    ex1(0.01, 100, [2, 2, 2])
elif exercise == 1:
    ex2(0.1, 1000, [9, 6, 2])
else:
    ex3(0.005, 5000, [10, 10])

# print(exerciseFile)


# import the data
# create the model based on the data entry and the config.json
# train
# show the results, metrics and plots
