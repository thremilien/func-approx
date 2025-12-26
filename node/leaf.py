from node.node import LeafNode

class Variable(LeafNode):
    def apply(self, variables): return variables[self.value]
    def symbol(self): return self.value

class Constant(LeafNode):
    def apply(self, variables):
        for var_value in variables.values():
            if hasattr(var_value, '__len__'):  # Check if it's array-like
                return self.value + 0 * var_value
        return self.value
    def symbol(self): return f"{self.value:.4g}"