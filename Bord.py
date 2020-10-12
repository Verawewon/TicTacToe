from turtle import *
from Player import *

side=133

setupWidth=side*3 # 3 rec
setupHeight=side*3 # 3 rec
setupStartX=0
setupStartY=0

gridpoint1= side/2 # 0.5 rec
gridpoint2=side*1.5 # 1.5 rec



def grid():
    "Draw tic-tac-toe grid."
    line(-gridpoint1, gridpoint2, -gridpoint1, -gridpoint2)
    line(gridpoint1, gridpoint2, gridpoint1, -gridpoint2)
    line(-gridpoint2, -gridpoint1, gridpoint2, -gridpoint1)
    line(-gridpoint2, gridpoint1, gridpoint2, gridpoint1)


def line(a,b,x,y):
    up()
    goto(a, b)
    down()
    goto(x, y)

class Rect:
    def __init(self, side,player,color):
        self.side=side
        self.player=player
        self.color=color

def drawx(x,y):
    line(x,y,x+side,y+side)
    line(x,y+side,x+side,y)

def drawo(x,y):
    up()
    goto(x+side/2,y+5)
    down()
    circle((side-4)/2)

#def floor(value):
#    return((value+side*1.5)//side)*side-side*1.5

state = {'player': 0}
players = [drawx, drawo]

def tap(x,y):
#    x= floor(x)
#    y= floor(y)
    player=state['player']
    draw=players[player]
    draw(x,y)
    update()
    state['player']=not player



setup(setupWidth, setupHeight, setupStartX, setupStartY)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()

