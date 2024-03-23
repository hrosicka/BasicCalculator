from tkinter import *
import random

palette = [
    "#f5f5f5", "#e8e8e8", "#dcdcdc",
    "#fffacd", "#ffebcd", "#f7f7bd",
    "#f0f8ff", "#e6f5ff", "#d9ecff",
    "#cce5ff", "#bcd2ff", "#a9bfff",
    "#f5f5fa", "#e8e8f5", "#dcdcdc",
    "#fffacd", "#ffebcd", "#f7f7bd",
    "#f7d3d3", "#f0cccc", "#e6c9c9",
    "#d9b3b3", "#c69c9c", "#b38585",
    "#f0f5f0", "#e6f2f2", "#d9edee",
    "#cce5e5", "#bcd2d2", "#a9bfff",
    "#f5faf5", "#e8f8f8", "#dcdcdc",
    "#f0f0f0", "#e6e6e6", "#dedede",
    "#f7f7f7", "#f0f0f0", "#e6e6e6",
]

# Funkce pro vyhodnocení zadaného výrazu
def evaluate(expression):
    if expression and expression[-1] in ["+", "-", "*", "/"]:
        return "Chybný výraz"
    if not expression:
        return "Zadejte výraz"
    try:
        return eval(expression)
    except:
        return "Chybný výraz"

# Funkce pro aktualizaci pole s výsledkem
def update_result(result):
    result_entry.delete(0, END)
    result_entry.insert(0, result)

# Funkce pro aktualizaci pole s výrazem
def update_expression(char):
    current_expression = expression_entry.get()
    cursor_position = expression_entry.index(INSERT)
    new_expression = current_expression[:cursor_position] + char + current_expression[cursor_position:]
    expression_entry.delete(0, END)
    expression_entry.insert(0, new_expression)

# Funkce pro vymazání celého výrazu
def clear_all():
    expression_entry.delete(0, END)

# Funkce pro vymazání posledního znaku
def clear_last():
    expression = expression_entry.get()
    expression_entry.delete(0, END)
    expression_entry.insert(0, expression[:-1])

# Vytvoření okna kalkulačky
window = Tk()
window.title("Kalkulačka")

# Vytvoření rámečku pro uspořádání widgetů
frame = Frame(window)
frame.pack()

# Vytvoření pole pro zadávání výrazu
expression_entry = Entry(frame, width=30)
expression_entry.pack(side=TOP)

# Vytvoření pole pro zobrazení výsledku
result_entry = Entry(frame, width=30)
result_entry.pack(side=TOP)

# Vytvoření rámečku pro tlačítka s číslicemi
number_frame = Frame(frame)
number_frame.pack(side=LEFT)

# Vytvoření tlačítek pro číslice se zvýšenou velikostí
for i in range(10):
    button = Button(number_frame, text=str(i), command=lambda i=i: update_expression(str(i)), width=5, height=2)
    button.grid(row=i // 3, column=i % 3)

# Vytvoření tlačítka pro desetinnou tečku
dot_button = Button(number_frame, text=".", command=lambda: update_expression("."), width=5, height=2)
dot_button.grid(row=3, column=2)

# Vytvoření rámečku pro operátory
operator_frame = Frame(frame)
operator_frame.pack(side=LEFT)

operators = ["+", "-", "*", "/"]

# Vytvoření tlačítek pro operátory se zvýšenou velikostí
for operator in operators:
    button = Button(operator_frame, text=operator, command=lambda operator=operator: update_expression(operator), bg="#FFE4C4", width=5, height=2)
    button.pack(side=TOP)

# Vytvoření rámečku pro tlačítka výpočtu a mazání
calculation_frame = Frame(frame)
calculation_frame.pack(side=LEFT)

# Vytvoření rámečku pro tlačítka výpočtu a mazání
calculation_frame = Frame(frame)
calculation_frame.pack(side=LEFT)

# Vytvoření tlačítek pro výpočet a mazání
equals_button = Button(calculation_frame, text="=", command=lambda: update_result(evaluate(expression_entry.get())), bg="plum", width=5, height=2)
equals_button.pack(side=TOP)

c_button = Button(calculation_frame, text="C", command=clear_all, bg="plum", width=5, height=2)
c_button.pack(side=TOP)

ce_button = Button(calculation_frame, text="CE", command=clear_last, bg="plum", width=5, height=2)
ce_button.pack(side=TOP)

def randomize_colors():
    for button in operator_frame.pack_slaves():
        button["bg"] = random.choice(palette)
    for i in range(10):
        button = number_frame.grid_slaves(row=i // 3, column=i % 3)[0]
        button["bg"] = random.choice(palette)
    equals_button["bg"] = random.choice(palette)
    c_button["bg"] = random.choice(palette)
    ce_button["bg"] = random.choice(palette)


# Vytvoření tlačítka pro generování barev
generate_colors_button = Button(calculation_frame, text="Generovat barvy", command=randomize_colors, bg="plum", width=5, height=2)
generate_colors_button.pack(side=TOP)



# Spuštění okna kalkulačky
window.mainloop()
