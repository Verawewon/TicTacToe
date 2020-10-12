from turtle import *
import Bord
import Player

def takeAInput(alt1, alt2, stringTitle, string, screen):
    goodInput = False
    while (goodInput != True):
        choice=screen.textinput(stringTitle, string)
        if( choice.lower() ==alt1):
            goodInput=True
        elif( choice.lower() ==alt2):
            goodInput=True
    return choice

def main():
    # input_turtle = Turtle()
    # input_turtle.hideturtle()
    # screen = input_turtle.getscreen()
    #
    # P1Name = screen.textinput("Enter Name", "Welcome to TicTacToe!\nWhat is your name? ")
    # P1XorO = takeAInput("x","o","X or O", "You want to be \n 'X' or 'O':",screen)
    #
    #
    # playAlt= takeAInput("1","2","Enter 1 or 2 ", "1 Play. 2 Play with Computer",screen)
    #
    # if(playAlt=="1"):
    #     P2Name = screen.textinput("Enter P2's name", "Whats the second players name? ")
    #     Bord()
    # elif(playAlt=="2"):
    Bord()


if __name__ == '__main__':
    main()
