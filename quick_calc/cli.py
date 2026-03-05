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

if __name__ == "__main__":
    from quick_calc.calculator import Calculator

    calc = Calculator()

    print("Quick-Calc CLI")
    print("Example: 5 + 3")

    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if operator == "+":
        result = calc.add(a, b)
    elif operator == "-":
        result = calc.subtract(a, b)
    elif operator == "*":
        result = calc.multiply(a, b)
    elif operator == "/":
        result = calc.divide(a, b)
    else:
        raise ValueError("Invalid operator")

    print("Result:", result)