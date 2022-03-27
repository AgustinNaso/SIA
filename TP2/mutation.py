from typing import Final
from crossbreed import GENES_QTY
import random

INTERVAL_BOUND: Final = 10
MUTATION_PROBABILITY: Final = 0.01


# mutation: given an individual, each gen of his chromosome has a probability p of getting his allele modified with
#           the formula x' = x + r, where x is the allele of the individual gen, r ~ U(-a, a) with a ϵ R
# In: Individual
# Out: Input Individual with his genes mutated.
def mutation(individual):
    for i in range(GENES_QTY):
        if random.random() <= MUTATION_PROBABILITY:
            individual.gen[i] += random.uniform(-INTERVAL_BOUND, INTERVAL_BOUND)
    return individual


