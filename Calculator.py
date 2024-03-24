from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
import random

from tkinter import (
    Button,
    Entry,
    Frame,
    END,
    INSERT,
    LEFT,
    TOP,
)

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

class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Kalkulačka")

        # Vytvoření rámečku pro uspořádání widgetů
        self.frame = Frame(self)
        self.frame.pack()

        self.resizable(False, False) 

        self.icon_path = "calc_icon.ico"  
        self.iconbitmap(self.icon_path)  

        # Vytvoření pole pro zadávání výrazu
        self.expression_entry = Entry(self.frame, width=30, justify="right")
        self.expression_entry.pack(side=TOP)

        # Vytvoření pole pro zobrazení výsledku
        self.result_entry = Entry(self.frame, width=30, justify="right")
        self.result_entry.pack(side=TOP)

        # Vytvoření rámečku pro tlačítka s číslicemi
        self.number_frame = Frame(self.frame)
        self.number_frame.pack(side=LEFT)

        # Vytvoření tlačítek pro číslice se zvýšenou velikostí
        for i in range(10):
            button = Button(self.number_frame, text=str(i), command=lambda i=i: self.update_expression(str(i)), width=6, height=2)
            button.grid(row=i // 3, column=i % 3)

        # Vytvoření tlačítka pro desetinnou tečku
        self.dot_button = Button(self.number_frame, text=".", command=lambda: self.update_expression("."), width=6, height=2)
        self.dot_button.grid(row=3, column=2)

        # Vytvoření rámečku pro operátory
        self.operator_frame = Frame(self.frame)
        self.operator_frame.pack(side=LEFT)

        operators = ["+", "-", "*", "/"]

        # Vytvoření tlačítek pro operátory se zvýšenou velikostí
        for operator in operators:
            button = Button(self.operator_frame, text=operator, command=lambda operator=operator: self.update_expression(operator), bg="#FFE4C4", width=6, height=2)
            button.pack(side=TOP)

        # Vytvoření rámečku pro tlačítka výpočtu a mazání
        self.calculation_frame = Frame(self.frame)
        self.calculation_frame.pack(side=LEFT)

        # Vytvoření tlačítek pro výpočet a mazání
        self.equals_button = Button(self.calculation_frame, text="=", command=lambda: self.update_result(self.evaluate(self.expression_entry.get())), bg="plum", width=6, height=2)
        self.equals_button.pack(side=TOP)

        self.c_button = Button(self.calculation_frame, text="C", command=self.clear_all, bg="plum", width=6, height=2)
        self.c_button.pack(side=TOP)

        self.ce_button = Button(self.calculation_frame, text="CE", command=self.clear_last, bg="plum", width=6, height=2)
        self.ce_button.pack(side=TOP)

        # Vytvoření tlačítka pro generování barev
        self.generate_colors_button = Button(self.calculation_frame, text="Colors", command=self.randomize_colors, bg="plum", width=6, height=2)
        self.generate_colors_button.pack(side=TOP)

        # Inicializace proměnných
        self.current_expression = ""
        self.previous_expression = ""
        self.result = 0

    # Funkce pro vyhodnocení zadaného výrazu
    def evaluate(self, expression):
        if expression and expression[-1] in ["+", "-", "*", "/"]:
            return "Chybný výraz"
        if not expression:
            return "Zadejte výraz"
        try:
            return eval(expression)
        except:
            return "Chybný výraz"

    # Funkce pro aktualizaci pole s výsledkem
    def update_result(self, result):
        self.result_entry.delete(0, END)
        self.result_entry.insert(0, result)

    # Funkce pro aktualizaci pole s výrazem
    def update_expression(self, char):
        self.current_expression = self.expression_entry.get()
        cursor_position = self.expression_entry.index(INSERT)
        new_expression = self.current_expression[:cursor_position] + char + self.current_expression[cursor_position:]
        self.expression_entry.delete(0, END)
        self.expression_entry.insert(0, new_expression)

    # Funkce pro vymazání celého výrazu
    def clear_all(self):
        self.expression_entry.delete(0, END)

    # Funkce pro vymazání posledního znaku
    def clear_last(self):
        expression = self.expression_entry.get()
        self.expression_entry.delete(0, END)
        self.expression_entry.insert(0, expression[:-1])

    # Funkce pro generování barev
    def randomize_colors(self):
        for button in self.operator_frame.pack_slaves():
            button["bg"] = random.choice(palette)
        for i in range(10):
            button = self.number_frame.grid_slaves(row=i // 3, column=i % 3)[0]
            button["bg"] = random.choice(palette)
        self.dot_button["bg"] = random.choice(palette)
        self.equals_button["bg"] = random.choice(palette)
        self.c_button["bg"] = random.choice(palette)
        self.ce_button["bg"] = random.choice(palette)
        self.generate_colors_button["bg"] = random.choice(palette)

# Spuštění kalkulačky
calculator = Calculator()
calculator.mainloop()
