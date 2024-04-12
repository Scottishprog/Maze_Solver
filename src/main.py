from graphics import Window, Point, Line


def main():
    win = Window(800, 600)
    point1 = Point(100, 100)
    point2 = Point(200, 100)
    line1 = Line(point1, point2)
    win.draw_line(line1, "Red")
    win.wait_for_close()


main()