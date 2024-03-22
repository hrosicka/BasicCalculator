from tkinter import *

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

# Vytvoření rámečku pro operátory
operator_frame = Frame(frame)
operator_frame.pack(side=LEFT)

operators = ["+", "-", "*", "/"]

# Vytvoření tlačítek pro operátory se zvýšenou velikostí
for operator in operators:
    button = Button(operator_frame, text=operator, command=lambda operator=operator: update_expression(operator), bg="orange", width=5, height=2)
    button.pack(side=TOP)

# Vytvoření rámečku pro tlačítka výpočtu a mazání
calculation_frame = Frame(frame)
calculation_frame.pack(side=LEFT)

# Vytvoření rámečku pro tlačítka výpočtu a mazání
calculation_frame = Frame(frame)
calculation_frame.pack(side=LEFT)

# Vytvoření tlačítek pro výpočet a mazání
equals_button = Button(calculation_frame, text="=", command=lambda: update_result(evaluate(expression_entry.get())), bg="plum", width=5, height=4)
equals_button.pack(side=TOP)

c_button = Button(calculation_frame, text="C", command=clear_all, bg="plum", width=5, height=2)
c_button.pack(side=TOP)

ce_button = Button(calculation_frame, text="CE", command=clear_last, bg="plum", width=5, height=2)
ce_button.pack(side=TOP)


# Spuštění okna kalkulačky
window.mainloop()
