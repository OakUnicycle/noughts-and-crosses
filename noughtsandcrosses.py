import numpy as np


class Board:
    def __init__(self, size_x, size_y, need):  # initialising all the variables
        self.neededToWin = need
        self.won = None
        self.size = (size_x, size_y)
        self.turn = 'x'
        self.board = np.zeros((size_y, size_x), dtype=str)      #board must be refered to as [y,x]

    def __repr__(self):  # what to output when board object is put into print function
        out = ""
        for i in self.board:
            for a in i:
                out += '- ' if a == '' else a + ' '
            out += "\n"
        return out

    def validate(self, space):  # returns false if move is valid else it returns the error
        if space[0] >= self.size[0] or space[0] < 0:
            return 'X index out of range'
        if space[1] >= self.size[1] or space[1] < 0:
            return 'Y index out of range'
        if self.board[space[1], space[0]] != '':   #board must be refered to as [y,x]
            return 'Square already taken'
        return False

    def move(self, space):
        self.board[space[1], space[0]] = self.turn
        self.turn = {'x': 'o', 'o': 'x'}[self.turn]


grid = Board(3, 4, 3)
while True:

    move = input('enter the square in the format x,y:    ')
    try:
        move = [int(i)-1 for i in move.split(',')]
    except ValueError:
        print("invalid input, either input was not an int or was not in the format x,y")
    else:
        validity = grid.validate(move)
        if not validity:
            grid.move(move)
            print(grid)
        else:
            print(validity)
