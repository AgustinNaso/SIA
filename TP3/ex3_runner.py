import json
import numpy as np

from TP3.ex3_1 import ex1
from TP3.ex3_2 import ex2

with open("ex3_config.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

exercise = int(jsonObject["exercise"])
exerciseFile = str(jsonObject["config_file"][exercise])

if exercise == 0:
    ex1(0.01, 100, [2, 2, 2])
elif exercise == 1:
    ex2(0.01, 10, [6])
else:
    ex1(0.01, 100, [1])

# print(exerciseFile)


# import the data
# create the model based on the data entry and the config.json
# train
# show the results, metrics and plots
