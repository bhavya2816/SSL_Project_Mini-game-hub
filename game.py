
import sys
import numpy as np

    class game_controls:
        def __init__(self,player1,player2,Rows,Columns):
            
            self.Current_player=player1        
            #Defining the board as a 2D array
            self.board = np.zeros((Rows,Columns))

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

    #Function to display the menu and get the user's choice
    def menu():
        print("MINI GAME HUB")
        print("1. Tic Tac Toe")
        print("2. Othello")
        print("3. Connect4")
        choice = input("Enter Ur choice: ")
        return choice

print("Hii")
player1=sys.argv[1]
player2=sys.argv[2]

print("hello")
while True:
    choice=menu()

    if choice == '1':
        from tic_tac_toe import tic_tac_toe
        tic_tac_toe(player1,player2)
    elif choice == '2':
        from othello import othello
        othello(player1,player2)
    elif choice == '3':
        from connect4 import connect4
        connect4(player1,player2)
    else:
        print("Invalid choice. Please try again.")
