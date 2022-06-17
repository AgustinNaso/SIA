import json
import numpy as np
from TP5.resources.fonts import font_1, font_2, font_3
from TP5.utils import to_bits


with open("config.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

learning_rate = jsonObject["learning_rate"]
epochs = jsonObject["epochs"]
hiddenLayers = np.array(jsonObject["hiddenLayers"])
batch_size = jsonObject["batch_size"]
momentum = jsonObject["momentum"]
adaptive_eta = jsonObject["adaptive_eta"]
set_momentum = False
adaptive_params = None
fonts = jsonObject["fonts"]

if adaptive_eta == 1:
    adaptive_k = int(jsonObject["adaptive_k"])
    adaptive_inc = int(jsonObject["adaptive_inc"])
    adaptive_dec = int(jsonObject["adaptive_dec"])
    adaptive_params = [adaptive_inc, adaptive_dec, adaptive_k]

if momentum == 1:
    set_momentum = True

if fonts == 1:
    expected_output = to_bits(font_1)
elif fonts == 2:
    expected_output = to_bits(font_2)
else:
    expected_output = to_bits(font_3)


