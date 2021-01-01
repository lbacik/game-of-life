
from tkinter import Canvas

DEFAULT_COLUMNS = 20
DEFAULT_ROWS = 20

ceil_size = 0

def draw(canvas: Canvas):
    canvas_width = canvas.winfo_width()

    global ceil_size
    ceil_size = canvas_width // DEFAULT_COLUMNS

    for i in range(1, DEFAULT_COLUMNS):
        canvas.create_line(ceil_size * i, 0, ceil_size * i, ceil_size * DEFAULT_ROWS, fill="gray")

    for j in range(1, DEFAULT_ROWS):
        canvas.create_line(0, ceil_size * j, canvas_width, ceil_size * j, fill="gray")
