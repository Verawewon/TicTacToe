from turtle import *
import Bord
import Player

rectIsTaken = [10, 10, 10, 10, 10, 10, 10, 10, 10]
def takeAInput(alt1, alt2, stringTitle, string, screen):
    goodInput = False
    while (goodInput != True):
        choice=screen.textinput(stringTitle, string)
        if( choice.lower() ==alt1):
            goodInput=True
        elif( choice.lower() ==alt2):
            goodInput=True
    return choice

def emptyRect(rectNr):
    if rectIsTaken[rectNr-1]==10:
        rectIsTaken[rectNr - 1]=player%2
        return True
    else:
        return False

def win():
    if (
            rectIsTaken[3] == rectIsTaken[4] == rectIsTaken[5] != 10 or
            rectIsTaken[7] == rectIsTaken[4] == rectIsTaken[1] != 10 or
            rectIsTaken[0] == rectIsTaken[4] == rectIsTaken[8] != 10 or
            rectIsTaken[6] == rectIsTaken[4] == rectIsTaken[2] != 10):
        if rectIsTaken[4]==0:
            print('P1 win!4')
        else:
            print('P2 win!4')
        return True

    if (
            rectIsTaken[6] == rectIsTaken[7] == rectIsTaken[8] != 10 or
            rectIsTaken[6] == rectIsTaken[3] == rectIsTaken[0] != 10):
        if rectIsTaken[6]==0:
            print('P1 win!6')
        else:
            print('P2 win6')
        return True
    if (
            rectIsTaken[8] == rectIsTaken[5] == rectIsTaken[2] != 10 or
            rectIsTaken[0] == rectIsTaken[1] == rectIsTaken[2] != 10):
        if rectIsTaken[2]==0:
            print('P1 win!2')
        else:
            print('P2 win!2')
        write('win')
        return True
    else:
        return False

def drawMatch():
    if (player>=8):
        print('draw')
        return True
    else:
        return False

def XorO(xo):
    if xo=='x':
        return [Bord.drawx, Bord.drawo]
    else:
        return [Bord.drawo, Bord.drawx]


players = XorO('x')

def tap(x,y):
    global stopTap
    global player
    x= Bord.floor(x)
    y= Bord.floor(y)
    rectNr=Bord.whichRect(x,y)
    draw=players[player%2]
    if emptyRect(rectNr)==True:
        draw(x,y)
        print(rectIsTaken)
        update()
        win()
        drawMatch()
        player+=1


def main():
    input_turtle = Turtle()
    input_turtle.hideturtle()
    screen = input_turtle.getscreen()

    global P1Name
    global P2Name
    global player
    global players
    P1Name = screen.textinput("Enter Name", "Welcome to TicTacToe!\nWhat is your name? ")
    P1XorO = takeAInput("x","o","X or O", "You want to be \n 'X' or 'O':",screen)

    if P1XorO=='o':

        players=XorO('o')

    playAlt= takeAInput("1","2","Enter 1 or 2 ", "1 Play. 2 Play with Computer",screen)

    if(playAlt=="1"):
        global rectIsTaken
        P2Name = screen.textinput("Enter P2's name", "Whats the second players name? ")
        Screen().clear()
        rectIsTaken = [10, 10, 10, 10, 10, 10, 10, 10, 10]
        player = 0
        Bord.main()
        onscreenclick(tap)
        done()

    elif(playAlt=="2"):
        # P2=COMPUTER
        pass


if __name__ == '__main__':
    main()
