import tkinter as tk
def evaluate_expression():
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")
def append_to_expression(value):
    entry.insert(tk.END, value)
def clear_entry():
    entry.delete(0, tk.END)
root = tk.Tk()
root.title("Simple Calculator")
result = tk.StringVar()
entry = tk.Entry(root, font=('Arial', 20), textvariable=result, justify='right')
entry.grid(row=0, column=0, columnspan=4, sticky='news')
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3)
]
for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=('Arial', 20), command=lambda value=text: append_to_expression(value))
    button.grid(row=row, column=column, sticky='news')
clear_button = tk.Button(root, text='C', font=('Arial', 20), command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=4, sticky='news')
evaluate_button = tk.Button(root, text='=', font=('Arial', 20), command=evaluate_expression)
evaluate_button.grid(row=5, sticky='news')
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
root.mainloop()