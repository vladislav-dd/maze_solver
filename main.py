from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    num_rows = 12
    num_cols = 12
    margin = 50
    screen_x = 800
    screen_y = 800
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_cols, num_rows, cell_size_x, cell_size_y, win)

    win.wait_for_close()


main()
