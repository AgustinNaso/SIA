import json
from TP4.utils import get_network_patterns, get_noisy_pattern
from TP4.hopfield.hopfield import Hopfield, print_state


def run_hopfield(network_patterns, noisy_pattern, iterations):
    hopfield_network = Hopfield(network_patterns)
    return hopfield_network.train(noisy_pattern, iterations)


with open("config.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

letters = jsonObject["letters"]
letter_to_modify = jsonObject["letter_to_modify"]
# expected_pattern = [i for sublist in get_letter(letter_to_modify.upper()) for i in sublist]
probability = jsonObject["probability"]
iterations = jsonObject["iterations"]
conserve_pattern = True if str(jsonObject["conserve_pattern"]) == 'True' else False

network_patterns = get_network_patterns(letters)
noisy_pattern = get_noisy_pattern(network_patterns, letter_to_modify, probability, conserve_pattern)
found, state = run_hopfield(network_patterns, noisy_pattern, iterations)
print(found)
print_state(state)
