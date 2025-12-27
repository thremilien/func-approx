from node.node import Node, UnaryNode, BinaryNode, LeafNode
from node.leaf import Variable, Constant
import random

class NodeSampler:
    def __init__(self, weights, variables, constant_range):
        self.weights = weights
        self.variables = variables
        self.constant_range = constant_range
        self.unary_classes = {k: v for k, v in weights.items() if isinstance(k, type) and issubclass(k, UnaryNode)}
        self.binary_classes = {k: v for k, v in weights.items() if isinstance(k, type) and issubclass(k, BinaryNode)}

    def sample_node(self, max_depth: int = 0) -> Node:
        if max_depth == 0:
            choices = ['Variable', 'Constant']
            weights = [self.weights['Variable'], self.weights['Constant']]
        else:
            choices = list(self.unary_classes.keys()) + list(self.binary_classes.keys()) + ['Variable', 'Constant']
            weights = list(self.unary_classes.values()) + list(self.binary_classes.values()) + [self.weights['Variable'], self.weights['Constant']]

        choice = random.choices(choices, weights=weights, k=1)[0]

        if choice == 'Variable':
            return Variable(random.choice(self.variables))
        elif choice == 'Constant':
            return Constant(random.uniform(*self.constant_range))
        elif issubclass(choice, UnaryNode):
            return choice(child=self.sample_node(max_depth - 1))
        else:
            return choice(left=self.sample_node(max_depth - 1), right=self.sample_node(max_depth - 1))
