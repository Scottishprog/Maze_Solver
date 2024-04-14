from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width=800, height=600, title='Maze Solver'):
        self.__root = Tk()
        self.__root.title(title)
        self.canvas = Canvas(self.__root, bg='white', width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print('Window has been closed')

    def close(self):
        self.__is_running = False

    def draw_line(self, t_line, fill_color="black"):
        t_line.draw(self.canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, t_canvas, fill_color="black"):
        t_canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)
        t_canvas.pack(fill=BOTH, expand=True)


