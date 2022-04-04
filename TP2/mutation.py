import json
from typing import Final
from crossbreed import GENES_QTY
import random

with open("settings.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

INTERVAL_BOUND: Final = int(jsonObject['mutation_bound'])
MUTATION_PROBABILITY: Final = float(jsonObject['mutation_rate'])

# mutation: given an individual, each gen of his chromosome has a probability p of getting his allele modified with
#           the formula x' = x + r, where x is the allele of the individual gen, r ~ U(-a, a) with a ϵ R
# In: Individual
# Out: Input Individual with his genes mutated.
mutations = [[0.15, 2], [0.1, 1], [0.05, 1]]


def mutation(individual, i):
    mutation_values = mutations[i]
    for i in range(GENES_QTY):
        if random.random() <= mutation_values[0]:
            individual.gen[i] += random.uniform(-mutation_values[1], mutation_values[1])
    return individual
