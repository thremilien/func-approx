from node.node import BinaryNode

class Addition(BinaryNode):
    def apply(self, left, right): return left + right
    def symbol(self): return "+"

class Subtraction(BinaryNode):
    def apply(self, left, right): return left - right
    def symbol(self): return "-"

class Multiplication(BinaryNode):
    def apply(self, left, right): return left * right
    def symbol(self): return "*"

class Division(BinaryNode):
    def apply(self, left, right): return left / right
    def symbol(self): return "/"


