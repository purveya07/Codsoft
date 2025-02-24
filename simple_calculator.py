import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


root = tk.Tk()
root.title("Simple Calculator")


label_num1 = tk.Label(root, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=10)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=10)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)


operation_var = tk.StringVar(value="+")

label_operation = tk.Label(root, text="Choose operation:")
label_operation.grid(row=2, column=0, padx=10, pady=10)

operations = ["+", "-", "*", "/"]
for i, op in enumerate(operations):
    rb = tk.Radiobutton(root, text=op, variable=operation_var, value=op)
    rb.grid(row=2, column=i+1, padx=5, pady=10)


calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=4, pady=10)


result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=4, pady=10)


root.mainloop()