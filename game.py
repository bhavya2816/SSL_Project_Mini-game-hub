
import sys
import numpy as np
    #Class to control the game flow and manage the board state
class basegame:
    def __init__(self,player1,player2,Rows,Columns):
        self.player1=player1
        self.player2=player2
        self.Current_player=player1        
        #Defining the board as a 2D array with initial values of 0
        self.board = np.zeros((Rows,Columns),dtype=int)

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
    print("MINI GAME HUB")
    print("1. Tic Tac Toe")
    print("2. Othello")
    print("3. Connect4")
    choice = input("Enter Ur choice: ")
    return choice

player1=sys.argv[1]
player2=sys.argv[2]


while True:
        choice=menu()

        if choice == '1':
            from games.tictactoe import tic_tac_toe
            game=tic_tac_toe(basegame,player1,player2)
            
        elif choice == '2':
            from games.othello import othello
            game=othello(basegame,player1,player2)
        elif choice == '3':
            from games.connect4 import connect4
            game=connect4(basegame,player1, player2)   
        else:
            print("Invalid choice. Please try again.")
        game.play()