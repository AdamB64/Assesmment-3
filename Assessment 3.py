from setuptools import Command
from field import field
from players import player
from balls import ball,quaffle,goldenssnitch,Bludgers

f = field()

g=goldenssnitch(8,3,"G")
g1=g.getChar()
g2=g.getRow()
g3=g.getCol()

f.placeball(g1,g3,g2)

p1 = player(1,1,"v",0)
p2 = player(5,1,"R",0)
play = [p1,p2]

c = play[0].getChar()
x = play[0].getRow()
y = play[0].getCol()

f.placePlayer(c,x,y)

r =play[1].getChar()
a =play[1].getRow()
b =play[1].getCol()

f.placePlayer(r,a,b)


print(f.toString())

p=True
r = None
count = 1
while g.caught ==False & (p1.ate>=100 or p2.ate>=100):
    if count == 1:
        r = p1
        print("Player 1")
    elif count ==2:
        r = p2
        print("Player 2")
        count =0
#getting command from the end user
    print("you are currently here \n" + r.toString())
    command = input("\nWhich direction do you want to move D=down,U+up,L=left and R=right or press Q to quit ")
    command = command.upper()
    while command not in ("D","U","L","R","Q"):
        command = input("You did not type D U L R or Q, try again ")
        command = command.upper()
    if command == "Q":
        quit()
#a if statement to check if the user is going down and that he is able to
    if f.canMove(x+1,y) == True and command =="D":
    # a if statement to check if the direction the user is going in has a sprout 
    #if f.getCharAtPos(x+1,y) =="@":
        #f.eatSprouts()
        #r.sproutAte()
        #s = s -1
    #function to clear the last postion 
        f.clearAtPos(x,y)
    #function to move the x axis down 
        x= r.moveDown()
    #function to place the rat on the maze
        f.placePlayer(play[count-1].getChar,x,y)
# a elif that says if not able to move in that direction tell user
    elif f.canMove(x+1,y) == False and command =="D":
        print("\nCant go that way pick another direction")
        p=False
#a if statement to check if the user is going up  and that he is able to
    if f.canMove(x-1,y) == True and command == "U":
    # a if statement to check if the direction the user is going in has a sprout 
    #if f.getCharAtPos(x-1,y)=="@":
        #f.eatSprouts()
        #r.sproutAte()
        #s = s -1
    #function to clear the last postion
        f.clearAtPos(x,y)
    #function to move the x axis up
        x =r.moveUp()
    #function to place the rat on the maze
        f.placePlayer(play[count-1].getChar,x,y)
# a elif that says if not able to move in that direction tell user
    elif f.canMove(x-1,y) == False and command == "U":
        print("\nCant go that way, pick another direction")
        p=False
#a if statement to check if the user is going left and that he is able to
    if f.canMove(x,y-1) == True and command =="L":
    # a if statement to check if the direction the user is going in has a sprout 
    #if f.getCharAtPos(x,y-1)=="@":
        #f.eatSprouts()
       # r.sproutAte()
       # s = s -1
    #function to clear the last postion
        f.clearAtPos(x,y)
    #function to move the x axis left
        y = r.moveLeft()
    #function to place the rat on the maze
        f.placePlayer(play[count-1].getChar,x,y)
# a elif that says if not able to move in that direction tell user
    elif f.canMove(x,y-1) ==False and command =="L":
        print("\nCant go that way, pick another direction")
        p=False
#a if statement to check if the user is going right and that he is able to
    if f.canMove(x,y+1) == True and command == "R":
    # a if statement to check if the direction the user is going in has a sprout 
    #if f.getCharAtPos(x,y+1) =="@":
        #f.eatSprouts()
       # r.sproutAte()
      #  s = s -1
    #function to clear the last postion
        f.clearAtPos(x,y)
    #function to move the x axis right
        y = r.moveRight()
    #function to place the rat on the maze
        f.placePlayer(play[count-1].getChar,x,y)
# a elif that says if not able to move in that direction tell user
    elif f.canMove(x,y+1) == False and command =="R":
        print("\nCant go that way, pick another direction")
        p= False
#a if statement to check how many sprouts the rat has ate
    if p==True:
        count = count + 1
    g.movements()
    f.placeball(g1,g3,g2)





"""
m.goToLevel2()
print (m.toString() + "\nlevel 2\n")

r3 = field(1,1,"v",r1.ate)
r4 = field(5,1,"R",r2.ate)
rat2=[r3,r4]

c = rat2[0].getChar()
x = rat2[0].getRow()
y = rat2[0].getCol()

m.placeRat(c,x,y)

r =rat2[1].getChar()
a =rat2[1].getRow()
b =rat2[1].getCol()

m.placeRat(r,a,b)

print(m.toString())

p=True
r = None
count = 1
s = m.sprouts
while s > 0:
    p=True
    if count == 1:
        r = r1
        print("Player 1")
    elif count ==2:
        r = r2
        print("Player 2")
        count =0
    #getting command from the end user
    print("you are currently here \n" + r.toString())
    command = input("\nWhich direction do you wnat to move D=down,U+up,L=left and R=right or press Q to quit ")
    command = command.upper()
    while command not in ("D","U","L","R","Q"):
        command = input("You did not type D U L R or Q, try again ")
        command = command.upper()
    if command == "Q":
        quit()
    #a if statement to check if the user is going down and that he is able to
    if m.canMove(x+1,y) == True and command =="D":
        # a if statement to check if the direction the user is going in has a sprout 
        if m.getCharAtPos(x+1,y) =="@":
            m.eatSprouts()
            r.sproutAte()
            s = s -1
        #function to clear the last postion 
        m.clearAtPos(x,y)
        #function to move the x axis down 
        x= r.moveDown()
        #function to place the rat on the maze
        m.placeRat(rat[count-1].getChar,x,y)
    # a elif that says if not able to move in that direction tell user
    elif m.canMove(x+1,y) == False and command =="D":
        print("\nCant go that way pick another direction")
        p=False
    #a if statement to check if the user is going up  and that he is able to
    if m.canMove(x-1,y) == True and command == "U":
        # a if statement to check if the direction the user is going in has a sprout 
        if m.getCharAtPos(x-1,y)=="@":
            m.eatSprouts()
            r.sproutAte()
            s = s -1
        #function to clear the last postion
        m.clearAtPos(x,y)
        #function to move the x axis up
        x =r.moveUp()
        #function to place the rat on the maze
        m.placeRat(rat[count-1].getChar,x,y)
    # a elif that says if not able to move in that direction tell user
    elif m.canMove(x-1,y) == False and command == "U":
        print("\nCant go that way, pick another direction")
        p=False
    #a if statement to check if the user is going left and that he is able to
    if m.canMove(x,y-1) == True and command =="L":
        # a if statement to check if the direction the user is going in has a sprout 
        if m.getCharAtPos(x,y-1)=="@":
            m.eatSprouts()
            r.sproutAte()
            s = s -1
        #function to clear the last postion
        m.clearAtPos(x,y)
        #function to move the x axis left
        y = r.moveLeft()
        #function to place the rat on the maze
        m.placeRat(rat[count-1].getChar,x,y)
    # a elif that says if not able to move in that direction tell user
    elif m.canMove(x,y-1) ==False and command =="L":
        print("\nCant go that way, pick another direction")
        p=False
    #a if statement to check if the user is going right and that he is able to
    if m.canMove(x,y+1) == True and command == "R":
        # a if statement to check if the direction the user is going in has a sprout 
        if m.getCharAtPos(x,y+1) =="@":
            m.eatSprouts()
            r.sproutAte()
            s = s -1
         #function to clear the last postion
        m.clearAtPos(x,y)
        #function to move the x axis right
        y = r.moveRight()
        #function to place the rat on the maze
        m.placeRat(rat[count-1].getChar,x,y)
    # a elif that says if not able to move in that direction tell user
    elif m.canMove(x,y+1) == False and command =="R":
        print("\nCant go that way, pick another direction")
        p= False
    #a if statement to check how many sprouts the rat has ate
    if p==True:
      count = count + 1"""