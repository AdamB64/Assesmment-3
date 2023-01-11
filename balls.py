import random
class ball:
    def __init__(self,rows,cols,chars):
        self.row = rows
        self.col =cols
        self.char =chars
    
    def getChar(self,):
        return self.char

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

class goldenssnitch(ball):
    def __init__(self, rows, cols, chars):
        super().__init__(rows, cols, chars)
        self.movement=None
        self.caught=False

    def movement(self):
        self.movement = random.randint(0,3)
        return self.movement

class Bludgers(ball):
    def __init__(self, rows, cols, chars):
        super().__init__(rows, cols, chars)
        self.movement=None

class quaffle(ball):
    def __init__(self, rows, cols, chars):
        super().__init__(rows, cols, chars)
        self.movement =None
        self.caught=False