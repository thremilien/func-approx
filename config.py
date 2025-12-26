from node.unary import Sin, Cos
from node.binary import Addition, Subtraction, Multiplication, Division

# Node type weights configuration
NODE_WEIGHTS = {
    # Unary operators
    Sin: 1.0,
    Cos: 1.0,

    # Binary operators
    Addition: 1.0,
    Subtraction: 1.0,
    Multiplication: 1.0,
    Division: 0.5,

    # Leaf nodes
    'Variable': 2.0,
    'Constant': 2.0,
}

# Variables that can be used in the trees
VARIABLES = ["x"]

# Range for random constant generation (min, max)
CONSTANT_RANGE = (-10, 10)