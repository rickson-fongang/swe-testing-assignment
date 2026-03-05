from quick_calc.calculator import Calculator

def calculate_expression(a, operator, b):
    calc = Calculator()

    if operator == "+":
        return calc.add(a, b)
    elif operator == "-":
        return calc.subtract(a, b)
    elif operator == "*":
        return calc.multiply(a, b)
    elif operator == "/":
        return calc.divide(a, b)
    else:
        raise ValueError("Invalid operator")

def clear_display():
    calc = Calculator()
    return calc.clear()