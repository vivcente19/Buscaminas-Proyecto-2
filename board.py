import random
from cell import Cell

class Board:
    def __init__(self, rows, cols: int, mines_quantity: int):
        self.rows = rows
        self.cols = cols
        self.mines_quantity = mines_quantity
        self.grid = [[Cell(r, c, 1) for c in range(cols)] for r in range(rows)]
        
    def __str__(self):
        '''Simple visual test'''
        mesa = []
        for fila in self.grid:
            fila_str = "".join(str(celda) for celda in fila)
            mesa.append(fila_str)
        return "\n".join(mesa)

Table = Board(6, 6, 6)
print(Table)

input()