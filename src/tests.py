import unittest
from maze import Maze, Cell


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_II(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_object_is_cell(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            type(m1._cells[0][0]), type(Cell()))

    def test_open_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        max_cols_index = num_cols - 1
        max_rows_index = num_rows - 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        #m1._break_entrance_and_exit()
        self.assertEqual(m1._cells[0][0].has_left_wall, False)
        self.assertEqual(m1._cells[max_cols_index][max_rows_index].has_right_wall, False)

    def test_visited_cells_false(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
