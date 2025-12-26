from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def evaluate(self, variables):
        pass

    @abstractmethod
    def __str__(self):
        pass

class LeafNode(Node, ABC):
    def __init__(self, value):
        self.value = value

    def evaluate(self, variables):
        return self.apply(variables)

    @abstractmethod
    def apply(self, variables):
        pass

    @abstractmethod
    def symbol(self):
        pass

    def __str__(self):
        return self.symbol()

class UnaryNode(Node, ABC):
    def __init__(self, child):
        self.child = child

    def evaluate(self, variables):
        child_value = self.child.evaluate(variables)
        return self.apply(child_value)

    @abstractmethod
    def apply(self, value):
        pass

    @abstractmethod
    def symbol(self):
        pass

    def __str__(self):
        return f"{self.symbol()}({self.child})"

class BinaryNode(Node, ABC):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, variables):
        left_value = self.left.evaluate(variables)
        right_value = self.right.evaluate(variables)
        return self.apply(left_value, right_value)

    @abstractmethod
    def apply(self, left, right):
        pass

    @abstractmethod
    def symbol(self):
        pass

    def __str__(self):
        return f"({self.left} {self.symbol()} {self.right})"