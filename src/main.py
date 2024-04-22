from graphics import Window
from src.maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 10, 14, 50, 50, win, 32425)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)

    win.wait_for_close()


main()
