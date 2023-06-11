from enum import Enum
from dataclasses import dataclass


class Operation(Enum):
    NONE = 0
    ADDITION = 1
    SUBTRACTION = 2
    DIVISION = 3
    MULTIPLICATION = 4
    NUMBER = 5
    NEGATIVE = 6
    POSITIVE = 7


class Node:
    def __init__(self, a, b, op: Operation):
        self.a = a
        self.b = b
        self.op = op

    def __repr__(self):
        return f"({self.a} {self.op.name} {self.b})"


if __name__ == "__main__":
    # 5 / ((5 * 5) + 1)
    tree = Node(5, Node(Node(5, 5, Operation.MULTIPLICATION), 1, Operation.ADDITION), Operation.DIVISION)
    print(tree)

    # 1 + 2 * 3
    tree2 = Node(1, Node(2, 3, Operation.MULTIPLICATION), Operation.ADDITION)
    print(tree2)
