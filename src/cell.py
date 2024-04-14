from graphics import Point, Line


class Cell:
    def __init__(self, canvas):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = canvas

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        upper_left_point = Point(self._x1, self._y1)
        upper_right_point = Point(self._x2, self._y1)
        lower_left_point = Point(self._x1, self._y2)
        lower_right_point = Point(self._x2, self._y2)
        if self.has_left_wall:
            self._win.draw_line(Line(upper_left_point, lower_left_point))
        if self.has_right_wall:
            self._win.draw_line(Line(upper_right_point, lower_right_point))
        if self.has_top_wall:
            self._win.draw_line(Line(upper_left_point, upper_right_point))
        if self.has_bottom_wall:
            self._win.draw_line(Line(lower_left_point, lower_right_point))
