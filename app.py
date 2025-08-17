from simpleeval import simple_eval

while True:
    expr = input("Enter your expression or 'q' to quit: ")
    if expr.lower() == 'q':
        break
    else:
        try:
            result_expr = simple_eval(expr)
            print("Result:", result_expr)
        except Exception:
            print("Invalid Input.")
