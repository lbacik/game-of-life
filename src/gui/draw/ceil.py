
from tkinter import Canvas
from src.abstract.gol_interface import GameOfLife
from src.game_of_life.point import Point


def draw_ceils(canvas: Canvas, gol: GameOfLife, ceil_size: int):
    for p in gol.field():
        if gol.field().state_point(p):
            draw_ceil(p, ceil_size, canvas)


def draw_ceil(p: Point, ceil_size: int, canvas: Canvas):
    canvas.create_rectangle(
        (p.x * ceil_size) + 2,
        (p.y * ceil_size) + 2,
        ((p.x + 1) * ceil_size) - 2,
        ((p.y + 1) * ceil_size) - 2,
        fill='black'
    )
