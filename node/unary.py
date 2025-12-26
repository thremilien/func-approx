from node.node import UnaryNode
import numpy as np

class Sin(UnaryNode):
    def apply(self, operand): return np.sin(operand)
    def symbol(self): return "sin"

class Cos(UnaryNode):
    def apply(self, operand): return np.cos(operand)
    def symbol(self): return "cos"

