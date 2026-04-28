#Importing required libraries
import sys
import numpy as np
import pygame
from datetime import datetime, date, time
import subprocess

#Class to control the game flow and manage the board state
class basegame:
    
    def __init__(self,player1,player2,Rows,Columns):
        #Initialising player1 and player2
        self.player1=player1
        self.player2=player2

        #Setting the current player to player 1 initially
        self.Current_player=player1

        #Storing Board Dimensions
        self.Rows=Rows
        self.Columns=Columns        
        
        #Defining the board as a 2D array with initial values of 0
        self.board = np.zeros((Rows,Columns))

        #Creating a variable to store winner
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
    # Initialize pygame
    pygame.init()

    # Create display window
    global screen
    screen=pygame.display.set_mode((2400, 1600))

    # Set background color
    screen.fill((230,230,250))

    #Setting window title
    pygame.display.set_caption("MiniGameHub-Menu")
    
    #Setting up fonts and fontsize for the menu text and options
    font1 = pygame.font.SysFont("georgia", 100)
    font= pygame.font.SysFont("comicsansms",80 )
    
    #Drawing the menu interface with options for different games using pygame
    
    pygame.draw.rect(screen,(230,230,250), (825, 300,775 ,150 ))
    text1=font1.render("MINI GAME HUB", True, (0, 0, 0))
    screen.blit(text1, (825, 325))

    pygame.draw.rect(screen, (142,69,123), (950,  500, 500,100 ))
    text2=font.render("1. Tic Tac Toe", True, (255, 255, 255))
    screen.blit(text2, (975, 525))

    pygame.draw.rect(screen, (142,69,123), (950, 700, 500,100 ))
    text3=font.render("2. Othello", True, (255, 255, 255))
    screen.blit(text3, (975, 725))

    pygame.draw.rect(screen, (142,69,123), (950, 900, 500,100 ))
    text4=font.render("3. Connect4", True, (255, 255, 255))
    screen.blit(text4, (975, 925))

    #Updating the display to show all the elements
    pygame.display.update()

    #keeping the menu screen active until the user selects a game or closes the window
    while True:
        for event in pygame.event.get():
            #Event handling quit
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                return
            
#Function to show the sort factors of leader board
def leaderboard():
    # Create the main display window with given resolution
    screen =pygame.display.set_mode((2400,1600))

    # Fill background with a light color
    screen.fill((230,230,250))

    # Set window title
    pygame.display.set_caption("MINIGAMEHUB")

    # Define fonts for headings and options
    font = pygame.font.SysFont(None,100)
    font1=pygame.font.SysFont(None,75)
     
    # Render and display "Leaderboard" title
    text= font.render("Leaderboard",True,(0,0,0))
    screen.blit(text,(1000,200))
    
    # Render and display "Sort by: " sub-title
    text= font1.render("Sort by:",True,(0,0,0))
    screen.blit(text,(1000,400))

    #Drawing buttons for sort options
    pygame.draw.rect(screen,(142,69,123),(900,600,600,100))
    text= font1.render("Player Name",True,(255,255,255))
    screen.blit(text,(925,625))

    pygame.draw.rect(screen,(142,69,123),(900,750,600,100))
    text= font1.render("No. of Wins",True,(255,255,255))
    screen.blit(text,(925,775))

    pygame.draw.rect(screen,(142,69,123),(900,900,600,100))
    text= font1.render("No. of Losses",True,(255,255,255))
    screen.blit(text,(925,925))

    pygame.draw.rect(screen,(142,69,123),(900,1050,600,100))
    text= font1.render("Win-Loss Ratio",True,(255,255,255))
    screen.blit(text,(925,1075))

    #Drawing button to continue
    pygame.draw.rect(screen,(142,69,123),(2000,1300,200,100))
    text= font1.render("Next",True,(255,255,255))
    screen.blit(text,(2025,1325))

     # Update the display to show all elements
    pygame.display.update()
     
    # Event loop to handle user interactions
    while True:
        for event in pygame.event.get():
             # Handle window close event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Handling Mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                #Checking which button is clicked and running bash leaderboard.sh with suitable argument
                if 900 <= x <= 1500 and 600<= y <= 700:
                    subprocess.run(["bash","leaderboard.sh","1"])       
                elif 900 <= x <= 1500 and 750 <= y <= 850:
                    subprocess.run(["bash","leaderboard.sh","2"])
                elif 900 <= x <= 1500 and 900<= y <= 1000:
                    subprocess.run(["bash","leaderboard.sh","3"])
                elif 900 <=x <= 1500 and 1050 <= y<= 1150:
                    subprocess.run(["bash","leaderboard.sh","4"])
                if 2000 <= x <= 2200 and 1300<= y <= 1400:
                    pygame.quit()
                    return

#Defining a funtion to plot matplotlib graphs
def graph_Analysis():
    pass

#Creating a window to ask wheter to continue or Exit
def Continue_Or_Not():
    pygame.init()
     # Create the main display window with given resolution
    screen =pygame.display.set_mode((1200,800))

    # Fill background with a light color
    screen.fill((230,230,250))

    # Set window title
    pygame.display.set_caption("MINIGAMEHUB")

    #Setting up fonts and fontsize for the menu text and options
    font1 = pygame.font.SysFont("comicsansms", 100)
    font= pygame.font.SysFont("comicsansms",80 )

    text= font1.render("Do you want to continue or exit?",True,(0,0,0))
    screen.blit(text,(100,200))

    pygame.draw.rect(screen,(142,69,123),(200,500,300,100))
    text= font.render("Continue",True,(255,255,255))
    screen.blit(text,(225,525))
    pygame.draw.rect(screen,(142,69,123),(600,500,200,100))
    text= font.render("Exit",True,(255,255,255))
    screen.blit(text,(625,525))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
             # Handle window close event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #Handling Mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if 200 <=x<= 500 and 500<=y<=600:
                    gameloop()
                if 600 <=x<=900 and 500<=y<=600:
                    pygame.quit()
                    sys.exit()

# Main game loop that controls menu, game selection, and result handling     
def gameloop():
    winner=None                         
    running=True                        #Controls the main loop execution
    
    menu()                              #Displaying the menu before entering the loop
    
    while running:        
            for event in pygame.event.get():
                
                # Handle window close event
                if event.type == pygame.QUIT:
                    running=False
                    pygame.quit()
                    sys.exit()

                # Handle mouse click events (game selection)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y =event.pos                         #Getting the mouse click coordinates

                    #If tic-tac-toe is selected
                    if 950 <= x <= 1450 and 500 <= y <= 600:
                        from games.tic_tac_toe import tic_tac_toe
                        game=tic_tac_toe(player1,player2)           #Initialize the game class
                        game.play()                                 #play the game
                        pygame.init()                               # Re initializing pygame after the end of the game
                        winner=game.winner                          #Storing the winner
                        game_played="Tic Tac Toe"

                    #If Othello is selected
                    elif 950 <= x <= 1450 and 700 <= y <= 800:
                        from games.othello import othello
                        game=othello(player1,player2)
                        game.play()                                 #Play the game
                        pygame.init()                               # Re initializing pygame after the end of the game
                        winner=game.winner                          #Storing the winner
                        game_played="Othello"

                    #If Connect4 is chosen
                    elif 950 <= x <= 1450 and 900 <= y <= 1000:
                        from games.connect4 import connect4
                        game=connect4(player1, player2)
                        game.play()                                # play the game
                        pygame.init()                              # Re initializing pygame after the end of the game
                        winner=game.winner                         #Storing the winner
                        game_played="Connect4"
                            
                    #Determining the loser from wonner
                    if winner==player1:
                        loser=player2
                    elif winner==player2:
                        loser=player1
                    else:
                        loser="Draw"
                        winner="Draw"
                    
                    #Storing the winner of the game in history.csv
                    if winner!="Draw":
                        with open("history.csv", "a") as f:
                            f.write(f"{winner},{loser},{date.today()},{datetime.now().strftime('%H:%M:%S')},{game_played}\n")  
                        
                        #Displaying leaderboard
                        leaderboard()
                        
                        #Displaying matplot graphs of games that are played most
                        graph_Analysis()

                        #Asking whether to continue to the menu or exit
                        Continue_Or_Not()


if __name__ == "__main__" :
    player1=sys.argv[1]
    player2=sys.argv[2]
    gameloop()