
from tkinter import *


def create_canvas(root: Tk):
    canvas = Canvas(root, width=400, height=400)
    print_info(root, canvas)
    return canvas


def print_info(root: Tk, canvas: Canvas):
    pass
    # canvas.create_text(10, 10, text='canvas geometry: %d x %d' % (canvas.winfo_width(), canvas.winfo_height()))
    # canvas.create_text(100, 100, text='canvas geometry: %d x %d' % (canvas.winfo_reqwidth(), canvas.winfo_reqheight()))
    # canvas.create_text(100, 140, text='root geometry: %d x %d' % (root.winfo_reqwidth(), root.winfo_reqheight()))
    # canvas.create_text(100, 160, text='root geometry: %d x %d' % (root.winfo_width(), root.winfo_height()))
    # canvas.create_text(100, 180, text=' ... geometry: %s' % (root.winfo_geometry(),))
    # canvas.create_text(100, 200, text=' ... geometry: %s' % (root.size(),))
    # canvas.create_text(100, 220, text=' ... geometry: %s' % (root.geometry(),))
    # canvas.create_text(100, 240, text='screen geometry: %d x %d' % (root.winfo_screenwidth(), root.winfo_screenheight()))
    # canvas.create_text(100, 220, text=' ... geometry: %s' % (root. ))
