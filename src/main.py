from graphics import Window, Point
from src.cell import Cell
from src.maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 10, 14, 50, 50, win)

    win.wait_for_close()


main()
