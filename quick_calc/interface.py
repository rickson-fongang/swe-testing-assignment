import tkinter as tk
from calculator import add, subtract, multiply, divide

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)

        result_label.config(text=f"Result: {result}")

    except Exception as e:
        result_label.config(text=f"Error: {e}")


window = tk.Tk()
window.title("Basic Calculator")
window.geometry("300x200")

tk.Label(window, text="Number 1").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="Number 2").pack()
entry2 = tk.Entry(window)
entry2.pack()

operation = tk.StringVar(value="+")

tk.OptionMenu(window, operation, "+", "-", "*", "/").pack()

tk.Button(window, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(window, text="Result:")
result_label.pack()

window.mainloop()