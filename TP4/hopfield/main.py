import json
from TP4.utils import get_network_patterns, get_noisy_pattern
from TP4.hopfield.hopfield import Hopfield

with open("config.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

letters = jsonObject["letters"]
letter_to_modify = jsonObject["letter_to_modify"]
probability = jsonObject["probability"]
iterations = jsonObject["iterations"]
conserve_pattern = True if str(jsonObject["conserve_pattern"]) == 'True' else False

network_patterns = get_network_patterns(letters)
noisy_pattern = get_noisy_pattern(network_patterns, letter_to_modify, probability, conserve_pattern)
hopfield_network = Hopfield(network_patterns)
found, pattern = hopfield_network.train(noisy_pattern, iterations)
print(f"Found: {found}")
if found:
    print("Pattern found")
else:
    print("Pattern not found")
print(f"Final pattern: {pattern}")