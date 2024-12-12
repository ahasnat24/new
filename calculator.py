import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        # Display field
        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        if text == "=":
            btn = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 18),
                            command=self.calculate)
        elif text == "C":
            btn = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 18),
                            command=self.clear)
        else:
            btn = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 18),
                            command=lambda t=text: self.append_to_expression(t))

        btn.grid(row=row, column=col, padx=5, pady=5)

    def append_to_expression(self, value):
        self.expression += value
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.expression = str(result)
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
