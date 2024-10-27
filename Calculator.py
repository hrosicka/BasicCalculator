# Improves DPI awareness for high-resolution displays
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
from ColorPalette import ColorPalette
from Tooltip import *

from tkinter import (
    Button,
    Entry,
    Frame,
    END,
    INSERT,
    LEFT,
    TOP,
)


class Calculator(tk.Tk):
    """A simple yet functional calculator application."""

    def __init__(self):
        """
        Initializes the calculator window and its basic properties.

        - Sets window title and prevents resizing.
        - Sets application icon (if "calc_icon.ico" exists).
        - Creates an instance of the ColorPalette class.
        - Calls the initialize_widgets method to create the UI elements.
        """
        super().__init__()

        self.title("Calculator")
        self.resizable(False, False)

        self.icon_path = "calc_icon.ico"
        try:
            self.iconbitmap(self.icon_path)
        except tk.TclError:
            print(f"Warning: Could not load icon from '{self.icon_path}'.")
        
        self.color_palette = ColorPalette()

        self.initialize_widgets()

    def initialize_widgets(self):
        """
        Initializes all the widgets used in the calculator.

        - Creates frames to hold different groups of widgets (expression entry,
          result entry, buttons, etc.).
        - Creates buttons for numbers, operators, and other functions.
        - Sets up tooltips for some widgets.
        - Initializes internal variables.
        - Sets padding for buttons using the set_button_padding function.
        """

        self.main_container = Frame(self, borderwidth=5, relief=tk.RIDGE)
        self.main_container.pack()

        self.expression_display = Entry(self.main_container, width=30, justify="right", borderwidth=15, relief=tk.FLAT)
        self.expression_display.pack(side=TOP)
        self.expression_display.focus()

        self.result_display = Entry(self.main_container, width=30, justify="right", state="readonly", borderwidth=15, relief=tk.FLAT)
        self.result_display.pack(side=TOP)

        self.number_button_frame = Frame(self.main_container)
        self.number_button_frame.pack(side=LEFT)

        for i in range(10):
            button = Button(self.number_button_frame, text=str(i), command=lambda i=i: self.update_expression(str(i)), width=6, height=2)
            button.grid(row=i // 3, column=i % 3)

        self.dot_button = Button(self.number_button_frame, text=".", command=lambda: self.update_expression("."), width=6, height=2)
        self.dot_button.grid(row=3, column=2)

        self.operator_button_frame = Frame(self.main_container)
        self.operator_button_frame.pack(side=LEFT)

        operators = ["+", "-", "*", "/"]

        for operator in operators:
            button = Button(
                self.operator_button_frame,
                text=operator, command=lambda operator=operator: self.update_expression(operator),
                bg="#FFE4C4",
                width=6, 
                height=2
            )
            button.pack(side=TOP)

        self.function_button_frame = Frame(self.main_container)
        self.function_button_frame.pack(side=LEFT)

        self.evaluate_button = Button(self.function_button_frame, text="=", command=lambda: self.update_result(self.evaluate(self.expression_display.get())), bg="plum", width=6, height=2)
        self.evaluate_button.pack(side=TOP)

        self.c_button = Button(self.function_button_frame, text="C", command=self.clear_all, bg="plum", width=6, height=2)
        self.c_button.pack(side=TOP)

        self.ce_button = Button(self.function_button_frame, text="CE", command=self.clear_last, bg="plum", width=6, height=2)
        self.ce_button.pack(side=TOP)

        self.generate_colors_button = Button(self.function_button_frame, text="Colors", command=self.randomize_colors, bg="plum", width=6, height=2)
        self.generate_colors_button.pack(side=TOP)


        self.current_expression = ""
        self.previous_expression = ""
        self.result = 0

        self.set_button_padding(self.operator_button_frame.pack_slaves())
        
        for i in range(10):
            button = self.number_button_frame.grid_slaves(row=i // 3, column=i % 3)[0]

        self.set_button_padding(self.number_button_frame.grid_slaves())
        self.set_button_padding(self.dot_button)
        self.set_button_padding(self.evaluate_button)
        self.set_button_padding(self.c_button)
        self.set_button_padding(self.ce_button)
        self.set_button_padding(self.generate_colors_button)

        expression_entry_tooltip = Tooltip(self.expression_display, text="Enter your mathematical expression here.")
        result_entry_tooltip = Tooltip(self.result_display, text="This field displays the calculated result.")
        generate_colors_button_tooltip = Tooltip(self.generate_colors_button, text="Click to change the button colors for a fun!")

    # Function to evaluate the entered expression
    def evaluate(self, expression):
        """
        Evaluates the given mathematical expression.
        Args:
            expression (str): The mathematical expression to be evaluated.
        Returns:
            string (str): The result of the evaluation or an error message if the evaluation fails.
        Raises:
            Exceptions: The function handles potential exceptions like SyntaxError, ZeroDivisionError, NameError, and other general exceptions.
        """
        try:
            result = eval(expression)
            return result
        except SyntaxError:
            return "Syntax error"
        except ZeroDivisionError:
            return "Division by zero"
        except NameError:
            return "Undefined variable"
        except Exception as e:
            return f"Error: {str(e)}"

    # Function to update the result entry widget
    def update_result(self, result):
        self.result_display['state'] = 'normal'
        self.result_display.delete(0, END)
        self.result_display.insert(0, result)
        self.result_display['state'] = 'readonly'

    # Function to update the expression entry widget
    def update_expression(self, char):
        self.current_expression = self.expression_display.get()
        cursor_position = self.expression_display.index(INSERT)
        new_expression = self.current_expression[:cursor_position] + char + self.current_expression[cursor_position:]
        self.expression_display.delete(0, END)
        self.expression_display.insert(0, new_expression)

    # Function to clear the entire expression
    def clear_all(self):
        self.result_display['state'] = 'normal'
        self.expression_display.delete(0, END)
        self.result_display['state'] = 'normal'
        self.result_display.delete(0, END)
        self.result_display['state'] = 'readonly'

     # Function to clear the last character
    def clear_last(self):
        expression = self.expression_display.get()
        self.expression_display.delete(0, END)
        self.expression_display.insert(0, expression[:-1])
        self.result_display['state'] = 'normal'
        self.result_display.delete(0, END)
        self.result_display['state'] = 'readonly'

    # Function to generate random colors for buttons
    def randomize_colors(self):
        for button in self.operator_button_frame.pack_slaves():
            button["bg"] = self.color_palette.get_random_color()
        for i in range(10):
            button = self.number_button_frame.grid_slaves(row=i // 3, column=i % 3)[0]
            button["bg"] = self.color_palette.get_random_color()
        self.dot_button["bg"] = self.color_palette.get_random_color()
        self.evaluate_button["bg"] = self.color_palette.get_random_color()
        self.c_button["bg"] = self.color_palette.get_random_color()
        self.ce_button["bg"] = self.color_palette.get_random_color()
        self.generate_colors_button["bg"] = self.color_palette.get_random_color()

    def set_button_padding(self, buttons, pad_x=10, pad_y=5):
        """Sets the padding for the given button or list of buttons.

        Args:
            buttons (Button or list[Button]): The button or list of buttons.
            pad_x (int, optional): The padding in the horizontal direction. Defaults to 10.
            pad_y (int, optional): The padding in the vertical direction. Defaults to 5.
        """

        if isinstance(buttons, list):
            # If buttons is a list, apply padding to each button using a list comprehension
            [button.config(padx=pad_x, pady=pad_y) for button in buttons]
        else:
            # If buttons is a single button, apply padding directly
            buttons.config(padx=pad_x, pady=pad_y)


# Run the calculator
calculator = Calculator()
calculator.mainloop()
