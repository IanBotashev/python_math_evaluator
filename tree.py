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
