import tkinter as tk

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
        if self.id is not None:  # Check if a timer ID exists before cancelling
            self.widget.after_cancel(self.id)
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

