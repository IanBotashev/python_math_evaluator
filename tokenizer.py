import string
import sys
from mathtoken import Token, TokenType
from dataclasses import dataclass
from exceptions import InvalidCharacter

@dataclass
class TokenMapItem:
    type: TokenType
    characters: list[str]
    stringed: bool


# A map that keeps track of each token, their characters, and if they are stringed.
token_map = [
    TokenMapItem(TokenType.NUMBER, [*string.digits, '.'], True),
    TokenMapItem(TokenType.IGNORE, [" "], True),
    TokenMapItem(TokenType.ADDITION, ["+"], False),
    TokenMapItem(TokenType.SUBTRACTION, ["-"], False),
    TokenMapItem(TokenType.DIVISION, ["/"], False),
    TokenMapItem(TokenType.MULTIPLICATION, ["*"], False),
    TokenMapItem(TokenType.LEFT_PARENTHESIS, ["("], False),
    TokenMapItem(TokenType.RIGHT_PARENTHESIS, [")"], False),
]


class Tokenizer:
    def __init__(self, string_to_tokenize):
        self.current_char = ""
        self.string = iter([*string_to_tokenize])
        self.advance()

    """
    Tokenize an entire string.
    """
    def tokenize(self):
        results = []

        while self.current_char is not None:
            char_map_item = self.get_character_type(self.current_char)

            if char_map_item.type == TokenType.IGNORE:
                self.advance()
                continue

            # If it's not a stringed type
            if not char_map_item.stringed:
                results.append(Token(char_map_item.type))

            else:
                if len(results) == 0 or results[-1].type != char_map_item.type:
                    results.append(Token(char_map_item.type, ""))

                results[-1].value += self.current_char

            self.advance()

        return results

    """
    Advances our current position in the string.
    """
    def advance(self):
        try:
            self.current_char = next(self.string)
        except StopIteration:
            self.current_char = None

    """
    Returns the tokentype of a character.
    """
    def get_character_type(self, character):
        for token_item in token_map:
            if character in token_item.characters:
                return token_item

        raise InvalidCharacter(f"Illegal character '{character}'")


if __name__ == "__main__":
    print(" ".join(sys.argv[1:]))
    tokenizer = Tokenizer(" ".join(sys.argv[1:]))
    print(tokenizer.tokenize())
