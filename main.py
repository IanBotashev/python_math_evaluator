#!/usr/bin/env python3
import sys
from tokenizer import Tokenizer
from mathparser import Parser
from interpreter import Interpreter


def main():
    expression = " ".join(sys.argv[1:])
    tokens = Tokenizer(expression).tokenize()
    tree = Parser(tokens).parse()
    print(Interpreter(tree).interpret())


if __name__ == "__main__":
    main()
