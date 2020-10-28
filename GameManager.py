from turtle import *
import Bord
import Player

class GameManager:
    def __init__(self, player,players,rect_is_taken,win_message,player_list):
        self.player=player
        self.players=players
        self.rect_is_taken=rect_is_taken
        self.win_message=win_message
        self.player_list=player_list

        text_turtle = Turtle()
        text_turtle.hideturtle()
        text_turtle.pencolor("black")
        self.text_turtle=text_turtle

    def emptyRect(self,rect_nr):
        if self.rect_is_taken[rect_nr - 1]==10:
            self.rect_is_taken[rect_nr - 1]= self.player % 2
            return True
        else:
            return False

    def win(self):
        if (
                self.rect_is_taken[3] == self.rect_is_taken[4] == self.rect_is_taken[5] != 10 or
                self.rect_is_taken[7] == self.rect_is_taken[4] == self.rect_is_taken[1] != 10 or
                self.rect_is_taken[0] == self.rect_is_taken[4] == self.rect_is_taken[8] != 10 or
                self.rect_is_taken[6] == self.rect_is_taken[4] == self.rect_is_taken[2] != 10):
            if self.rect_is_taken[4]==0:
                self.win_message=self.player_list[0].name +' win!'
            else:
                self.win_message=self.player_list[1].name +' win!'
            return True

        if (
                self.rect_is_taken[6] == self.rect_is_taken[7] == self.rect_is_taken[8] != 10 or
                self.rect_is_taken[6] == self.rect_is_taken[3] == self.rect_is_taken[0] != 10):
            if self.rect_is_taken[6]==0:
                self.win_message=self.player_list[0].name +' win!'
            else:
                self.win_message=self.player_list[1].name +' win!'
            return True
        if (
                self.rect_is_taken[8] == self.rect_is_taken[5] == self.rect_is_taken[2] != 10 or
                self.rect_is_taken[0] == self.rect_is_taken[1] == self.rect_is_taken[2] != 10):
            if self.rect_is_taken[2]==0:
                self.win_message=self.player_list[0].name +' win!'
            else:
                self.win_message=self.player_list[1].name +' win!'
            return True
        else:
            return False

    def tap(self,x,y):
        x= Bord.floor(x)
        y= Bord.floor(y)
        rectNr=Bord.whichRect(x,y)
        draw=self.players[self.player%2]
        if self.emptyRect(rectNr)==True:
            draw(x,y)
            #print(self.rect_is_taken)
            if (self.win()==True):
                Screen().clear()
                self.text_turtle.write(self.win_message, font=("Arial", 30, "normal"))
            elif(self.player>=8):
                Screen().clear()
                self.text_turtle.write(f"Draw!", font=("Arial", 30, "normal"))
            update()
            self.player+=1

def XorO(xo):
    if xo=='x':
        return [Bord.drawx, Bord.drawo]
    else:
        return [Bord.drawo, Bord.drawx]

def takeAInput(alt1, alt2, string_title, string, screen):
    good_input = False
    while (good_input != True):
        choice=screen.textinput(string_title, string)
        if( choice.lower() ==alt1):
            good_input=True
        elif( choice.lower() ==alt2):
            good_input=True
    return choice


def main():
    input_turtle = Turtle()
    input_turtle.hideturtle()
    screen = input_turtle.getscreen()

    p1_name = screen.textinput("Enter Name", "Welcome to TicTacToe!\nWhat is your name? ")
    P1XorO = takeAInput("x","o","X or O", "You want to be \n 'X' or 'O':",screen)

    if P1XorO=='o':
        players=XorO('o')
        p1 = Player.Player(p1_name)
    else:
        players = XorO('x')
        p1 = Player.Player(p1_name)

    rect_is_taken = [10, 10, 10, 10, 10, 10, 10, 10, 10]

    p2_name = screen.textinput("Enter p2's name", "Whats the second players name? ")
    p2 = Player.Player(p2_name)
    player_list=[p1,p2]

    Screen().clear()
    Bord.main()

    my_game_menager = GameManager(0, players, rect_is_taken, '', player_list)
    if(my_game_menager.win()==True):
        Screen().clear()
        screen.textinput("Enter p2's name", "Whats the second players name? ")
    onscreenclick(my_game_menager.tap)


    done()



if __name__ == '__main__':
    main()
