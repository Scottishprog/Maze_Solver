from graphics import Window, Point
from src.cell import Cell


def main():
    win = Window(800, 600)
    point1 = Point(100, 100)
    point2 = Point(200, 200)
    point3 = Point(200, 100)
    point4 = Point(300, 200)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell1.has_left_wall = False
    cell1.has_top_wall = False
    cell2.has_right_wall = False
    cell2.has_bottom_wall = False
    cell1.draw(point1.x, point1.y, point2.x, point2.y)
    cell2.draw(point3.x, point3.y, point4.x, point4.y)
    win.wait_for_close()


main()