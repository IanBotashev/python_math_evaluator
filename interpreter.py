from tree import Node, Operation


class Interpreter:
    def __init__(self, tree):
        self.tree = tree

    """
    Entry point into the class.
    """
    def interpret(self):
        return self.evaluate(self.tree)

    """
    Tries to evaluate a node, by adding up any of it's content.
    """
    def evaluate(self, node):
        if node.op in [Operation.POSITIVE, Operation.NUMBER]:
            return node.a

        elif node.op == Operation.ADDITION:
            return self.evaluate(node.a) + self.evaluate(node.b)

        elif node.op == Operation.SUBTRACTION:
            return self.evaluate(node.a) - self.evaluate(node.b)

        elif node.op == Operation.MULTIPLICATION:
            return self.evaluate(node.a) * self.evaluate(node.b)

        elif node.op == Operation.DIVISION:
            return self.evaluate(node.a) / self.evaluate(node.b)

        elif node.op == Operation.NEGATIVE:
            return -node.a

        elif node.op == Operation.EXPONENT:
            return self.evaluate(node.a) ** self.evaluate(node.b)
