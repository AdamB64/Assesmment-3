import random
class ball:
    def __init__(self,rows,cols,chars):
        self.row = rows
        self.col =cols
        self.char =chars

class goldenssnitch(ball):
    def __init__(self, rows, cols, chars):
        super().__init__(rows, cols, chars)
        self.movement=None

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