import math
from simpleeval import simple_eval

while True:
    funcs = {
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'log': math.log
    }
    expr = input("Enter your expression or 'q' to quit: ")
    if expr.lower() == 'q':
        break
    else:
        try:
            result_expr = simple_eval(expr, functions=funcs)
            print("Result:", result_expr)
        except Exception:
            print("Invalid Input.")
