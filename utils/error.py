import numpy as np

def norm2(xref, yref, individual):
    return np.sum((individual.evaluate({"x": xref}) - yref)**2)

def r_norm2(xref, yref, individual):
    return np.sum((individual.evaluate({"x": xref}) - yref)**2)/np.sum(yref**2)