# Improves DPI awareness for high-resolution displays
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


class ColorPalette:
    """A class to manage the color palette for the calculator buttons."""

    def __init__(self):
        self.colors = [
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
        
    def get_random_color(self):
        """Returns a random color from the palette."""
        return random.choice(self.colors)
    
class Tooltip(object):
    """
    Creates a tooltip widget.

    Args:
        widget: The widget to which the tooltip is attached.
        text: The text to display in the tooltip.
        delay: The delay in milliseconds before the tooltip appears.
        follow_mouse: Whether the tooltip should follow the mouse cursor.
    """

    def __init__(self, widget, text=None, delay=50, follow_mouse=False):
        self.widget = widget
        self.text = text
        self.delay = delay
        self.follow_mouse = follow_mouse
        self.tipwindow = None
        self.id = None
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)

    def enter(self, event):
        self.schedule_tip()

    def leave(self, event):
        if self.tipwindow:
            self.tipwindow.destroy()
        self.tipwindow = None
        self.id = None

    def schedule_tip(self):
        self.id = self.widget.after(self.delay, self.show_tip)

    def show_tip(self):
        if self.tipwindow:
            return

        x = y = 0
        if self.follow_mouse:
            x = self.widget.winfo_rootx() + self.widget.winfo_width() + 5
            y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5
        else:
            x = self.widget.winfo_rootx() + self.widget.winfo_width() / 2 - 20
            y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5

        self.tipwindow = tk.Toplevel()
        self.tipwindow.overrideredirect(True)
        self.tipwindow.geometry("+%d+%d" % (x, y))

        label = tk.Label(self.tipwindow, bg="plum2", text=self.text, justify=tk.LEFT, padx=2, pady=2, relief=tk.SOLID, borderwidth=1)
        label.pack(ipadx=1)
        self.tipwindow.lift()

class Calculator(tk.Tk):
    """A simple yet functional calculator application."""

    def __init__(self):
        super().__init__()

        # Set window title and prevent resizing
        self.title("Calculator")
        self.resizable(False, False)

        # Set application icon (if "calc_icon.ico" exists)
        self.icon_path = "calc_icon.ico"
        try:
            self.iconbitmap(self.icon_path)
        except tk.TclError:
            print(f"Warning: Could not load icon from '{self.icon_path}'.")
        
        self.initialize_widgets()

    def initialize_widgets(self):
        """Initializes all the widgets used in the calculator."""

        # Create a frame to hold all widgets
        self.frame = Frame(self, borderwidth=5, relief=tk.RIDGE)
        self.frame.pack()

        # Entry widget for user to input expression (right-aligned)
        self.expression_entry = Entry(self.frame, width=30, justify="right", borderwidth=15, relief=tk.FLAT)
        self.expression_entry.pack(side=TOP)

        # Tooltip for input expression
        self.expression_entry_tooltip = "Enter your mathematical expression here."
        #Hovertip(self.expression_entry, self.expression_entry_tooltip)

        # Entry widget to display the result (right-aligned)
        self.result_entry = Entry(self.frame, width=30, justify="right", state="readonly", borderwidth=15, relief=tk.FLAT)
        self.result_entry.pack(side=TOP)

        # Tooltip for display the result
        self.result_entry_tooltip = "This field displays the calculated result."
        #Hovertip(self.result_entry, self.result_entry_tooltip)

        # Frame to hold number buttons
        self.number_frame = Frame(self.frame)
        self.number_frame.pack(side=LEFT)

        # Create number buttons with increased size
        for i in range(10):
            button = Button(self.number_frame, text=str(i), command=lambda i=i: self.update_expression(str(i)), width=6, height=2)
            button.grid(row=i // 3, column=i % 3)

        # Button for decimal point
        self.dot_button = Button(self.number_frame, text=".", command=lambda: self.update_expression("."), width=6, height=2)
        self.dot_button.grid(row=3, column=2)

        # Frame to hold operator buttons
        self.operator_frame = Frame(self.frame)
        self.operator_frame.pack(side=LEFT)

        # List of operators
        operators = ["+", "-", "*", "/"]

        # Create operator buttons with increased size and light yellow background
        for operator in operators:
            button = Button(self.operator_frame, text=operator, command=lambda operator=operator: self.update_expression(operator), bg="#FFE4C4", width=6, height=2)
            button.pack(side=TOP)

        # Frame to hold buttons for calculation and clearing
        self.calculation_frame = Frame(self.frame)
        self.calculation_frame.pack(side=LEFT)

        # Button to evaluate the expression (light plum background)
        self.equals_button = Button(self.calculation_frame, text="=", command=lambda: self.update_result(self.evaluate(self.expression_entry.get())), bg="plum", width=6, height=2)
        self.equals_button.pack(side=TOP)

        # Button to clear the entire expression (light plum background)
        self.c_button = Button(self.calculation_frame, text="C", command=self.clear_all, bg="plum", width=6, height=2)
        self.c_button.pack(side=TOP)

        # Button to clear the last character (light plum background)
        self.ce_button = Button(self.calculation_frame, text="CE", command=self.clear_last, bg="plum", width=6, height=2)
        self.ce_button.pack(side=TOP)

        # Button to generate random colors for buttons (light plum background)
        self.generate_colors_button = Button(self.calculation_frame, text="Colors", command=self.randomize_colors, bg="plum", width=6, height=2)
        self.generate_colors_button.pack(side=TOP)

        # Tooltip for generate random colors for buttons
        self.generate_colors_button_tooltip = "Click to change the button colors for a fun!"
        #Hovertip(self.generate_colors_button, self.generate_colors_button_tooltip)

        # Initialize variables
        self.current_expression = ""
        self.previous_expression = ""
        self.result = 0

        self.set_button_padding(self.operator_frame.pack_slaves())
        
        for i in range(10):
            button = self.number_frame.grid_slaves(row=i // 3, column=i % 3)[0]

        self.set_button_padding(self.number_frame.grid_slaves())
        self.set_button_padding(self.dot_button)
        self.set_button_padding(self.equals_button)
        self.set_button_padding(self.c_button)
        self.set_button_padding(self.ce_button)
        self.set_button_padding(self.generate_colors_button)

        expression_entry_tooltip = Tooltip(self.expression_entry, text="Enter your mathematical expression here.")
        result_entry_tooltip = Tooltip(self.result_entry, text="This field displays the calculated result.")
        generate_colors_button_tooltip = Tooltip(self.generate_colors_button, text="Click to change the button colors for a fun!")

    # Function to evaluate the entered expression
    def evaluate(self, expression):
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
        self.result_entry['state'] = 'normal'
        self.result_entry.delete(0, END)
        self.result_entry.insert(0, result)
        self.result_entry['state'] = 'readonly'

    # Function to update the expression entry widget
    def update_expression(self, char):
        self.current_expression = self.expression_entry.get()
        cursor_position = self.expression_entry.index(INSERT)
        new_expression = self.current_expression[:cursor_position] + char + self.current_expression[cursor_position:]
        self.expression_entry.delete(0, END)
        self.expression_entry.insert(0, new_expression)

    # Function to clear the entire expression
    def clear_all(self):
        self.result_entry['state'] = 'normal'
        self.expression_entry.delete(0, END)
        self.result_entry['state'] = 'normal'
        self.result_entry.delete(0, END)
        self.result_entry['state'] = 'readonly'

     # Function to clear the last character
    def clear_last(self):
        expression = self.expression_entry.get()
        self.expression_entry.delete(0, END)
        self.expression_entry.insert(0, expression[:-1])
        self.result_entry['state'] = 'normal'
        self.result_entry.delete(0, END)
        self.result_entry['state'] = 'readonly'

    # Function to generate random colors for buttons
    def randomize_colors(self):
        color_palette = ColorPalette()
        for button in self.operator_frame.pack_slaves():
            button["bg"] = color_palette.get_random_color()
        for i in range(10):
            button = self.number_frame.grid_slaves(row=i // 3, column=i % 3)[0]
            button["bg"] = color_palette.get_random_color()
        self.dot_button["bg"] = color_palette.get_random_color()
        self.equals_button["bg"] = color_palette.get_random_color()
        self.c_button["bg"] = color_palette.get_random_color()
        self.ce_button["bg"] = color_palette.get_random_color()
        self.generate_colors_button["bg"] = color_palette.get_random_color()

    def set_button_padding(self, buttons, pad_x=10, pad_y=5):
        """Sets the padding for the given button or list of buttons.

        Args:
            buttons (Button or list[Button]): The button or list of buttons.
            pad_x (int, optional): The padding in the horizontal direction. Defaults to 10.
            pad_y (int, optional): The padding in the vertical direction. Defaults to 5.
        """

        if isinstance(buttons, list):
            # If buttons is a list, iterate over each button
            for button in buttons:
                button.config(padx=pad_x, pady=pad_y)
        else:
            # If buttons is a single button, set the padding directly
            buttons.config(padx=pad_x, pady=pad_y)


# Run the calculator
calculator = Calculator()
calculator.mainloop()
