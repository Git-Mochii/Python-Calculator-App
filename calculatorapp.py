
# GUI Calculator Project #

import tkinter as tk

text = "" # Text Area

def add_to_area(sth): # Function to add a number to the text area
    global text
    text = text + str (sth)
    area.delete("1.0", "end")
    area.insert("1.0", text)

def cal(): # Function to calculate the answer
    global text
    answer = str(eval(text))
    area.delete("1.0", "end")
    area.insert("1.0", answer)

def empty_area(): # Function to clear the text area
    global text
    text = ""
    area.delete("1.0", "end")

# Window Settings

window=tk.Tk()
window.geometry("300x450")
window.title("Calculator Application")
window.resizable(False, False)

for i in range(5):
    window.columnconfigure(i, weight=1)
for i in range(8):
    window.rowconfigure(i, weight=1)

area = tk.Text(window, height=3, width=24, font=("Calibri", 16, "bold"))
area.grid(row=1, column=0, columnspan=5)  # Use sticky to fill the cell

window.config(padx=5, pady=5, background="#ede8e8")

# Number Buttons

button_1 = tk.Button(window, text="1" , command=lambda: add_to_area(1), width= 5 , font=("Calibri", 16))
button_1.grid(row=4, column=1, padx=10)

button_2 = tk.Button(window, text="2", command=lambda: add_to_area(2), width= 5, font=("Calibri", 16))
button_2.grid(row=4, column=2, padx=10)

button_3 = tk.Button(window, text="3", command=lambda: add_to_area(3), width= 5, font=("Calibri", 16))
button_3.grid(row=4, column=3, padx=10)

button_4 = tk.Button(window, text="4", command=lambda: add_to_area(4), width= 5, font=("Calibri", 16))
button_4.grid(row=3, column=1, padx=10)

button_5 = tk.Button(window, text="5", command=lambda: add_to_area(5), width= 5, font=("Calibri", 16))
button_5.grid(row=3, column=2, padx=10)

button_6 = tk.Button(window, text="6", command=lambda: add_to_area(6), width= 5, font=("Calibri", 16))
button_6.grid(row=3, column=3, padx=10)

button_7 = tk.Button(window, text="7", command=lambda: add_to_area(7), width= 5, font=("Calibri", 16))
button_7.grid(row=2, column=1, padx=10)

button_8 = tk.Button(window, text="8", command=lambda: add_to_area(8), width= 5, font=("Calibri", 16))
button_8.grid(row=2, column=2, padx=10)

button_9 = tk.Button(window, text="9", command=lambda: add_to_area(9), width= 5, font=("Calibri", 16))
button_9.grid(row=2, column=3, padx=10)

button_0 = tk.Button(window, text="0", command=lambda: add_to_area(0), width= 5, font=("Calibri", 16))
button_0.grid(row=5, column=1, padx=10)

# Operators  Buttons

button_plus= tk.Button(window, text="+", command=lambda: add_to_area("+"), width= 5, font=("Calibri", 16))
button_plus.grid(row=5, column=4, padx=10)

button_minus = tk.Button(window, text="-", command=lambda: add_to_area("-"), width= 5, font=("Calibri", 16))
button_minus.grid(row=4, column=4, padx=10)

button_times = tk.Button(window, text="*", command=lambda: add_to_area("*"), width= 5, font=("Calibri", 16))
button_times.grid(row=3, column=4, padx=10)

button_divide = tk.Button(window, text="/", command=lambda: add_to_area("/"), width= 5, font=("Calibri", 16))
button_divide.grid(row=2, column=4, padx=10)

button_clear = tk.Button(window, text="C", command=lambda: empty_area(), width= 5, font=("Calibri", 16))
button_clear.grid(row=5, column=3, padx=10)

button_decimal = tk.Button(window, text=".", command=lambda: add_to_area("."), width= 5, font=("Calibri", 16))
button_decimal.grid(row=5, column=2, padx=10)

button_cal = tk.Button(window, text="=", command=cal, width= 13, font=("Calibri", 16))
button_cal.grid(row=6, column=1, columnspan=2, padx=10)

button_open_brackets = tk.Button(window, text="(" , command=lambda: add_to_area("("), width= 5, font=("Calibri", 16))
button_open_brackets.grid(row=6, column=3, padx=10)

button_closed_brackets = tk.Button(window, text=")", command=lambda: add_to_area(")"), width= 5, font=("Calibri", 16))
button_closed_brackets.grid(row=6, column=4, padx=10)

label = tk.Label(window, text="Git-Mochii's Calculator", font=("Calibri", 10))
label.grid(row=7, column=0, columnspan=4, sticky="nsew")  

# Main Window Loop

window.mainloop()