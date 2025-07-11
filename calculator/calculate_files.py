import tkinter as tk

def press(num):
    entry_var.set(entry_var.get() + str(num))

def clear():
    entry_var.set("")

def equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Setup window
screen = tk.Tk()
screen.title("Python Calculator")
screen.geometry("300x400")
entry_var = tk.StringVar()

entry = tk.Entry(screen, textvariable=entry_var, font=('Arial', 20), bd=10, justify='right')
entry.pack(fill='both')

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for row in buttons:
    frame = tk.Frame(screen)
    frame.pack(expand=True, fill='both')
    for btn in row:
        if btn == '=':
            action = equal
        elif btn == 'C':
            action = clear
        else:
            action = lambda x=btn: press(x)

        tk.Button(frame, text=btn, font=('Arial', 18), command=action).pack(side='left', expand=True, fill='both')

screen.mainloop()