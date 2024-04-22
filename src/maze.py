import time
import random
from cell import Cell


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)


    def _create_cells(self):
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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        # if in destination cell, return.
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return
        while True:
            dest_list = []
            # check for cells to move to - watch for out of range errors!
            if i != 0 and self._cells[i - 1][j].visited == False:
                dest_list.append([i - 1, j])
            if i != self.num_cols - 1 and self._cells[i + 1][j].visited == False:
                dest_list.append([i + 1, j])
            if j != 0 and self._cells[i][j - 1].visited == False:
                dest_list.append([i, j - 1])
            if j != self.num_rows - 1 and self._cells[i][j + 1].visited == False:
                dest_list.append([i, j + 1])

            # if no destinations, return.
            print(f"Destination list: {dest_list}, with length: {len(dest_list)}")
            if len(dest_list) == 0:
                return

            # Pick a random direction, if there is more than one option
            dir_index = random.randrange(0, len(dest_list))
            dest_cell = dest_list[dir_index]

            # Knock down the walls.
            dest_i = dest_cell[0]
            dest_j = dest_cell[1]
            print(f"Breaking walls to: {dest_cell}")
            if dest_i > i:
                self._cells[i][j].has_right_wall = False
                self._cells[dest_i][dest_j].has_left_wall = False
            if dest_i < i:
                self._cells[i][j].has_left_wall = False
                self._cells[dest_i][dest_j].has_right_wall = False
            if dest_j > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[dest_i][dest_j].has_top_wall = False
            if dest_j < j:
                self._cells[i][j].has_top_wall = False
                self._cells[dest_i][dest_j].has_bottom_wall = False
            self._draw_cell(i,j)
            self._draw_cell(dest_i, dest_j)

            # Move to the next cell by calling _break_walls_r
            self._break_walls_r(dest_i, dest_j)