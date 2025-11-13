class Cell:
    def __init__(self, x_pos: int, y_pos: int, grid_size: int):
        '''Defines main variables of the Cell class'''
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.is_mine = False
        self.is_revealed = False
        self.is_flag = False
        self.neighbor_mines = 0
        self.kaboom = False
        self.grid_size = grid_size # Useful to know how to draw the cell
        
    def __str__(self):
        if self.is_revealed:
            state = "⬜"
            # state = "░░"
        else:
            state = "⬛"
            # state = "██"
        return state