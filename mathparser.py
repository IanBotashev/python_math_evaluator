from mathtoken import Token, TokenType
from tree import Node, Operation
from exceptions import InvalidSyntax


operation_map = {
    TokenType.ADDITION: Operation.ADDITION,
    TokenType.SUBTRACTION: Operation.SUBTRACTION,
    TokenType.MULTIPLICATION: Operation.MULTIPLICATION,
    TokenType.DIVISION: Operation.DIVISION,
}


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = iter(tokens)
        self.current_token = None
        self.advance()

    """
    Advances our current position
    """
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    """
    Entry point into starting parsing tokens.
    """
    def parse(self):
        result = self.find_expression()

        # We have some weird leftover statements not doing anything, raise syntax error.
        if self.current_token is not None:
            raise InvalidSyntax()

        return result

    """
    Finds expression
    """
    def find_expression(self):
        result = self.find_term()
        while self.current_token is not None and self.current_token.type in [TokenType.ADDITION, TokenType.SUBTRACTION]:
            operation = operation_map[self.current_token.type]
            self.advance()
            result = Node(result, self.find_term(), operation)

        return result

    """
    Finds term
    """
    def find_term(self):
        result = self.find_factor()
        while self.current_token is not None and self.current_token.type in [TokenType.MULTIPLICATION, TokenType.DIVISION]:
            operation = operation_map[self.current_token.type]
            self.advance()
            result = Node(result, self.find_factor(), operation)

        return result

    """
    Finds factor
    """
    def find_factor(self):
        result = None
        if self.current_token.type == TokenType.LEFT_PARENTHESIS:
            self.advance()
            result = self.find_expression()

            # Unclosed parenthesis if true.
            if self.current_token.type != TokenType.RIGHT_PARENTHESIS:
                raise InvalidSyntax

            self.advance()

        elif self.current_token.type == TokenType.NUMBER:
            result = Node(float(self.current_token.value), None, Operation.NUMBER)
            self.advance()

        elif self.current_token.type == TokenType.ADDITION:
            self.advance()
            result = Node(self.find_factor().a, None, Operation.POSITIVE)

        elif self.current_token.type == TokenType.SUBTRACTION:
            self.advance()
            result = Node(self.find_factor().a, None, Operation.NEGATIVE)

        else:
            raise InvalidSyntax()

        return result
