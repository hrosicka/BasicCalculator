import random

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
