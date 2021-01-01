
from tkinter import *
from src.gui.draw.canvas import create_canvas, print_info
from src.gui.draw.grid import draw as grid_draw
import src.gui.draw.grid as grid
from src.game_of_life.factory import Factory as GFactory
from src.gui.draw.ceil import draw_ceils


def clear():
    canvas.delete("all")
    grid_draw(canvas)


def refresh(event=None):
    clear()
    print_info(root, canvas)
    draw_ceils(canvas, gol, grid.ceil_size)


def change_ceil_state(event):
    x = event.x // grid.ceil_size
    y = event.y // grid.ceil_size
    if gol.field().state(x, y):
        gol.field().set(x,y, False)
    else:
        gol.field().set(x,y, True)
    refresh()


def nextg():
    gol.next_generation()
    refresh()


gol = GFactory.create(20, 20)

root = Tk()
canvas = create_canvas(root)
canvas.pack(fill=BOTH, expand=True)

button = Button(root, text='next generation', command = nextg)
button.pack()

button_clear = Button(root, text='clear', command = clear)
button_clear.pack()

canvas.bind( "<Button-1>", change_ceil_state)
canvas.bind( "<Configure>", refresh)

root.geometry("500x500+400+200")
root.mainloop()
