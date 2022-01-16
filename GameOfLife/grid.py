class Grid:
    def __init__(self, width, height) -> None:
        self.x_side = width
        self.y_side = height
    
    def getDimensions(self):
        return {"x": self.x_side, "y": self.y_side}
    
    def createGrid(self, x, y, cell):
        grid = []

        for column in y:
            row = []
            for row in x:
                row.append(cell)
            grid.append(row)
        
        return grid
                