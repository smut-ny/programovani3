import grid
import cell



Grid = grid.Grid(20, 40)
empty_cell = cell.Cell(0)



print(Grid.createGrid(Grid.x_side, Grid.y_side, empty_cell))