class field:
    """A 2D Maze"""

    def __init__(self):
        """The Maze constructor
        (none) -> none
        start by declaring attributes"""
        self.field = [['#','#','#','#','#','#','#','#','#','#','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],      
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#','#','#','#','#','#','#','#','#','#','#']]
        self.height = 7
        self.width = 7

    def toString(self):
        printme = ""
        for i in range (0, len(self.field)):
            for j in self.field[i]:
                printme = printme + j
            printme = printme +"\n"
        return printme 

    def placePlayer (self, Pla_char, row, column):
        self.field[row][column] = Pla_char

    def placeball(self,ba_char,bal_row,bal_col):
        self.field[bal_row][bal_col]=ba_char
                

    def clearAtPos(self, row, col):
        self.field[row][col] = " "

    def canMove(self,row,col):
        p = self.getCharAtPos(row,col)
        if p == "#":
            return False
        else:
            return True

    def goToLevel2(self):
        self.field = [['#','#','#','#','#','#','#'],
                     ['#',' ','#',' ',' ','@','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ',' ','@',' ','#','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ','#',' ',' ','@','#'],
                     ['#','#','#','#','#','#','#']]

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getCharAtPos(self, row, col):
        return self.field[row][col]