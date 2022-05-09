import json
import numpy as np

from ex3_1 import ex1
from ex3_2 import ex2
from ex3_3 import ex3

with open("ex3_config.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

exercise = int(jsonObject["exercise"])
exerciseFile = str(jsonObject["config_file"][exercise])

with open(exerciseFile) as jsonFile:
    configJsonObject = json.load(jsonFile)
    jsonFile.close()

learning_rate = configJsonObject["learning_rate"]
epochs = configJsonObject["epochs"]
hiddenLayers = np.array(configJsonObject["hiddenLayers"])


if exercise == 0:
    ex1(learning_rate, epochs, hiddenLayers)
elif exercise == 1:
    ex2(learning_rate, epochs, hiddenLayers)
else:
    ex3(learning_rate, epochs, hiddenLayers)


# import the data
# create the model based on the data entry and the config.json
# train
# show the results, metrics and plots
