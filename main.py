import matplotlib.pyplot as plt
import numpy as np

from config import NODE_WEIGHTS, VARIABLES, CONSTANT_RANGE
from node.sampler import NodeSampler


sampler = NodeSampler(NODE_WEIGHTS, VARIABLES, CONSTANT_RANGE)

# Generate multiple random trees
plt.figure(figsize=(12, 8))

for i in range(4):
    # Generate random tree with depth 3
    random_tree = sampler.sample_node(max_depth=8)

    print(f"Random tree {i + 1}: {random_tree}")

    # Evaluate and plot
    xsample = np.linspace(-3, 3, 100)
    try:
        ysample = random_tree.evaluate({"x": xsample})
        plt.subplot(2, 2, i + 1)
        plt.plot(xsample, ysample)
        plt.title(str(random_tree), fontsize=10)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
    except Exception as e:
        print(f"Error evaluating tree {i + 1}: {e}")

plt.tight_layout()
plt.show()