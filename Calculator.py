import tkinter as tk

def click(button):
    current = entry.get()
    if button == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    elif button == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button)

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 18),
              command=lambda b=button: click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()