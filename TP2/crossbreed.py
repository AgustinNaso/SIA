from individual import Individual
from typing import Final
import numpy as np

X = Individual(np.random.randn(11))
Y = Individual(np.random.randn(11))
GENES_QTY: Final = 11


# Simple Crossbreed: Chosen a random value p from 1 to n where n is the size of the chromosome,
#                    this algorithm takes and copy the alleles of the first individual from locus 0
#                    to locus p - 1 to the first child, then copies the from locus p to the last locus of
#                    the second individual to it.
#                    The same process is used for the second child, but copies the alleles until the locus p - 1
#                    from the second individual to the second child and then copies the rest of the first individual.
# In: a pair of individuals
# Out: an array of 2 individuals resulting from simple crossbreeding the input pair of individuals
def simple_crossbreed(x1, x2):
    children = np.array([Individual(np.random.rand(11)), Individual(np.random.rand(11))])
    chosen_locus = np.random.randint(low=0, high=GENES_QTY)
    children[0].gen = np.append(x1.gen[0:chosen_locus].copy(), x2.gen[chosen_locus: GENES_QTY].copy())
    children[1].gen = np.append(x2.gen[0:chosen_locus].copy(), x1.gen[chosen_locus: GENES_QTY].copy())
    return children


# Multiple Crossbreed: Chosen a random value p from 1 to n where n is the size of the chromosome,
#                      and then a random value t from p to n, this algorithm takes and copy the alleles
#                      of the first individual from locus 0 to p and then from locus t to n and to the first child
#                      then copies from locus p to locus t from the second individual to it.
#                      The same process is used for the second child, but instead copies the alleles from locus 0 to
#                      locus p and from locus t to locus n from the second individual and from locus p to locus t from
#                      the first one.
# In: a pair of individuals
# Out: an array of 2 individuals resulting from multiple crossbreeding the input pair of individuals
def multiple_crossbreed(x1, x2):
    children = np.array([Individual(np.zeros(11, dtype=float)), Individual(np.zeros(11, dtype=float))])
    first_chosen_locus = np.random.randint(low=0, high=GENES_QTY - 1)
    second_chosen_locus = np.random.randint(low=first_chosen_locus, high=GENES_QTY)
    children[0].gen = np.concatenate((x1.gen[0:first_chosen_locus].copy(),
                                      x2.gen[first_chosen_locus: second_chosen_locus].copy(),
                                      x1.gen[second_chosen_locus:GENES_QTY].copy()))
    children[1].gen = np.concatenate((x2.gen[0:first_chosen_locus].copy(),
                                      x1.gen[first_chosen_locus: second_chosen_locus].copy(),
                                      x2.gen[second_chosen_locus:GENES_QTY].copy()))
    return children


# Uniform Crossbreed: Each child locus i can get the value of the first or second individual
#                     locus i with a probability of 0.5.
# In: a pair of individuals
# Out: an array of 2 individuals resulting from uniform crossbreeding the input pair of individuals
def uniform_crossbreed(x1, x2):
    children = np.array([Individual(np.zeros(11, dtype=float)), Individual(np.zeros(11, dtype=float))])
    for idx in range(GENES_QTY):
        p = np.random.randint(2)
        if p == 1:
            children[0].gen[idx] = x1.gen[idx]
            children[1].gen[idx] = x2.gen[idx]
        else:
            children[0].gen[idx] = x2.gen[idx]
            children[1].gen[idx] = x1.gen[idx]
    return children

