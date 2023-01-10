class player:
    """A class to make a rat object for putting in a maze
    Attributes will include row and column settings 
    (row,col,char) -> Rat
    0,5,'x' -> returns a rat obect at postion 0,5"""

    def __init__(self,row,col,char,ate):
        self.row = row
        self.col = col
        self.char = char 
        self.ate = ate

    def toString(self):
        info = "characteristics of a player " + self.char
        info = info + "\npostion = row " + str(self.row)
        info = info + "\npostion = column " + str(self.col)
        info = info + "\nsprouts ate " + str(self.ate)
        return info

#we now want to place the rat in the maze.
#use the getter method in rat to find out the character 
#then pass them all to the maze using this method
#    def placeRat (self, rat_char, row, column):
#        self.maze[row][column] = rat_char

#adding setters

    def setChar(self,chars):
        self.char = chars

    def setRow(self,rows):
        self.row = rows

    def setCol(self,cols):
        self.col = cols

#adding getters
    def getChar(self,):
        return self.char

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def moveUp(self):
        self.row = self.row - 1
        return self.row

    def moveDown(self):
        self.row = self.row + 1
        return self.row

    def moveRight(self):
        self.col = self.col + 1 
        return self.col

    def moveLeft(self):
        self.col = self.col - 1
        return self.col
