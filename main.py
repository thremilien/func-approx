import matplotlib.pyplot as plt
import numpy as np

from config import NODE_WEIGHTS, VARIABLES, CONSTANT_RANGE, POPULATION_SIZE
from utils.sampler import NodeSampler
from utils.error import norm2, r_norm2

def ref(x):
    return -x**3 + 2*x

xref = np.linspace(-3, 3, 20)
yref = ref(xref)

sampler = NodeSampler(NODE_WEIGHTS, VARIABLES, CONSTANT_RANGE)
population = [sampler.sample_node(max_depth=4) for _ in range(POPULATION_SIZE)]

min_individual = None
min_error = np.inf
for individual in population:
    error = r_norm2(xref, yref, individual)
    if error < min_error:
        min_individual = individual
        min_error = error

print(min_individual)
print(min_error)

# TODO make a score function that also take into account the number of nodes or the depth of the tree with a parameter
# TODO make a mutate function
# TODO resolve basic cases (unary/binary operators involving constants)

xsample = np.linspace(-4, 4, 1000)
plt.scatter(xref, yref)
plt.plot(xsample, ref(xsample))
plt.plot(xsample, min_individual.evaluate({"x": xsample}))
plt.show()