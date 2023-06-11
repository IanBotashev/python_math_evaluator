# python_math_evaluator
Quick and dirty, terminal-based, math expression evaluator created in python.  
Follows the order of operations for PEMDAS.  

## Supported Syntax
Currently, the following syntax is supported:
- Basic operations; `+, -, /, *`   
- Parentheses; `()`  
- Negation, turning an expression into a negative; `-`  

## Running
Start `main.py` with it's passed-in argument being the expression to evaluate, i.e. `python3 main.py "2 + 2"`.  
While the quotation marks are not required, unintended bugs may happen from the shell, for example, expanding wildcards.  
