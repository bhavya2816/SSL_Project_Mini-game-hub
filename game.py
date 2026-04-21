
import sys
import numpy as np
import pygame
from datetime import datetime, date, time
import subprocess

pygame.init()
    #Class to control the game flow and manage the board state
class basegame:
    def __init__(self,player1,player2,Rows,Columns):
        self.player1=player1
        self.player2=player2
        self.Current_player=player1
        self.Rows=Rows
        self.Columns=Columns        
        #Defining the board as a 2D array with initial values of 0
        self.board = np.zeros((Rows,Columns))
        self.winner=None
    #Function to get current player
    def Get_current_player(self):
        return self.Current_player
    
    #Function for printing the board
    def print_board(self):
        print(self.board)

    #Function that switches the current player after each move
    def switch_turn(self):
        if self.Current_player == self.player1:
           self.Current_player = self.player2
        else:
            self.Current_player = self.player1
    #Function to check for a win condition (to be implemented in each game subclass)
    def check_win(self):
           pass

#Function to display the menu and get the user's choice
def menu():

    global screen
    screen=pygame.display.set_mode((2400, 1600))
    screen.fill((230,230,250))
    pygame.display.set_caption("MiniGameHub-Menu")
    #Setting up fonts and fontsize for the menu text and options
    font1 = pygame.font.SysFont("georgia", 100)
    font= pygame.font.SysFont("comicsansms",80 )
    #Drawing the menu interface with options for different games using pygame
    
    pygame.draw.rect(screen,(230,230,250), (825, 300,775 ,150 ))
    text1=font1.render("MINI GAME HUB", True, (0, 0, 0)), (825, 325)
    screen.blit(text1[0], text1[1])

    pygame.draw.rect(screen, (142,69,123), (950,  500, 500,100 ))
    text2=font.render("1. Tic Tac Toe", True, (255, 255, 255)), (975, 525)
    screen.blit(text2[0], text2[1])

    pygame.draw.rect(screen, (142,69,123), (950, 700, 500,100 ))
    text3=font.render("2. Othello", True, (255, 255, 255)), (975, 725)
    screen.blit(text3[0], text3[1])

    pygame.draw.rect(screen, (142,69,123), (950, 900, 500,100 ))
    text4=font.render("3. Connect4", True, (255, 255, 255)), (975, 925)
    screen.blit(text4[0], text4[1])


    pygame.display.update()
    #keeping the menu screen active until the user selects a game or closes the window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                return      

#Creating a fn to run the menu , the leaderboard and analysis          
def gameloop():
    winner=None
    running=True
    menu()
    while running:        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False
                    pygame.quit()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y =event.pos
                    if 950 <= x <= 1450 and 500 <= y <= 600:
                        from games.tic_tac_toe import tic_tac_toe
                        game=tic_tac_toe(player1,player2)
                        game.play()
                        pygame.init()
                        winner=game.winner
                        game_played="Tic Tac Toe"
                    elif 950 <= x <= 1450 and 700 <= y <= 800:
                        from games.othello import othello
                        game=othello(player1,player2)
                        game.play()
                        pygame.init()
                        winner=game.winner
                        game_played="Othello"
                    elif 950 <= x <= 1450 and 900 <= y <= 1000:
                        from games.connect4 import connect4
                        game=connect4(player1, player2)
                        game.play()   
                        pygame.init()
                        winner=game.winner
                        game_played="Connect4"
                            

                    if winner==player1:
                        loser=player2
                    elif winner==player2:
                        loser=player1
                    else:
                        loser="Draw"
                        winner="Draw"
                    #Storing the winner of the game in history.csv
                    with open("history.csv", "a") as f:
                        f.write(f"{winner},{loser},{date.today()},{datetime.now().strftime('%H:%M:%S')},{game_played}\n")  
                    
                    #Displaying leaderboard
                    subprocess.run(["bash","leaderboard.sh"])
                    #Displaying matplot graphs of games that are played most


                    #Asking whether to continue to the menu or exit

                    gameloop()
        
            






if __name__ == "__main__" :
    player1=sys.argv[1]
    player2=sys.argv[2]
    gameloop()