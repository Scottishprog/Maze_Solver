import time
from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cell()

    def _create_cell(self):
        self._cells = []
        for i in range(0, self.num_cols):
            maze_col = []
            for j in range(0, self.num_rows):
                maze_col.append(Cell(self._win))
            self._cells.append(maze_col)

        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        _x1 = self.x1 + i * self.cell_size_x
        _y1 = self.y1 + j * self.cell_size_y
        _x2 = _x1 + self.cell_size_x
        _y2 = _y1 + self.cell_size_y
        self._cells[i][j].draw(_x1, _y1, _x2, _y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        exit_cell_i = self.num_cols - 1
        exit_cell_j = self.num_rows - 1
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[exit_cell_i][exit_cell_j].has_right_wall = False
        self._draw_cell(exit_cell_i, exit_cell_j)
