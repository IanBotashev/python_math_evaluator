from enum import Enum


class TokenType(Enum):
    NUMBER = 0
    ADDITION = 1
    SUBTRACTION = 2
    DIVISION = 3
    MULTIPLICATION = 4
    IGNORE = 5
    RIGHT_PARENTHESIS = 6
    LEFT_PARENTHESIS = 7
    EXPONENT = 8


class Token:
    def __init__(self, tokentype: TokenType, value=None):
        self.type = tokentype
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f"Token({self.type}, {self.value})"
        else:
            return f"Token({self.type})"
