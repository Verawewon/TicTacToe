from turtle import *
from Player import *

side=250
rectNr=0

setupWidth=side*3 # 3 rec
setupHeight=side*3 # 3 rec
setupStartX=0
setupStartY=0

gridpoint1= side/2 # 0.5 rec
gridpoint2=side*1.5 # 1.5 rec

class Rect:
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def area(x,y):
        line(x,y,x+side,y)
        line(x+side, y, x + side, y-side)
        line(x + side, y-side, x, y - side)
        line(x, y-side, x, y)


def grid():
    "Draw tic-tac-toe grid."
    # line(-gridpoint1, gridpoint2, -gridpoint1, -gridpoint2)
    # line(gridpoint1, gridpoint2, gridpoint1, -gridpoint2)
    # line(-gridpoint2, -gridpoint1, gridpoint2, -gridpoint1)
    # line(-gridpoint2, gridpoint1, gridpoint2, gridpoint1)
    Rec1 = Rect.area(side * 0.5 - side * 2, side * 0.5 - side)
    Rec2 = Rect.area(side * 0.5 - side, side * 0.5 - side)
    Rec3 = Rect.area(side * 0.5, side * 0.5 - side)

    Rec4 = Rect.area(side * 0.5 - side * 2, side * 0.5)
    Rec5 = Rect.area(side * 0.5 - side, side * 0.5)
    Rec6 = Rect.area(side * 0.5, side * 0.5)

    Rec7 = Rect.area(side * 0.5 - side * 2, side * 0.5 + side)
    Rec8 = Rect.area(side * 0.5 - side, side * 0.5 + side)
    Rec9 = Rect.area(side * 0.5, side * 0.5 + side)

def line(a,b,x,y):
    up()
    goto(a, b)
    down()
    goto(x, y)

def whichRect(x,y):
    rectNr=0;
    if y==-side*1.5:
        if x==-side*1.5:
            rectNr=1
        elif x==-side*0.5:
            rectNr=2
        else:
            rectNr=3
    elif y==-side*0.5:
        if x == -side * 1.5:
            rectNr = 4
        elif x == -side * 0.5:
            rectNr = 5
        else:
            rectNr = 6
    else:
        if x == -side * 1.5:
            rectNr = 7
        elif x == -side * 0.5:
            rectNr = 8
        else:
            rectNr = 9

    return rectNr


def drawx(x,y):
    line(x,y,x+side,y+side)
    line(x,y+side,x+side,y)

def drawo(x,y):
    up()
    goto(x+side/2,y+5)
    down()
    circle((side-4)/2)

def floor(value):
    # click inside 9 grids area
    return((value+side*1.5)//side)*side-side*1.5

def main():
    setup(setupWidth, setupHeight, setupStartX, setupStartY)
    hideturtle()
    tracer(False)
    grid()



