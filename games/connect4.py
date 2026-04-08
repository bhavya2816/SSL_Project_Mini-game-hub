import sys
import numpy as np


print("Welcome to Connect4!")

#Class to control the game flow and manage the board state
class connect4():
    def __init__(self,basegame,player1,player2):
        self.base=basegame(player1,player2,7,7)
        self.runningstatus=True
        self.winner=None
        self.turn=0
        self.movevalid=True
        self.player=self.base.Get_current_player()
    #Function to drop a piece in the selected column 
    def drop_piece(self,col,player):
        #checking whether the column is full or not before dropping the piece
        if self.base.board[0][col]!=0:
            self.movevalid=False
            return 0
        for r in range(6,-1,-1):
            if self.base.board[r][col]==0:
                self.base.board[r][col]=player
                return r
        return 0
    def play(self):
        while self.runningstatus:
            self.base.print_board()
            player=self.base.Get_current_player()
            print(f"{player}'s turn")
            col=int(input("Enter the column number (0-6) to drop your piece: "))
            row=self.drop_piece(col,player)
            if not self.movevalid:
                print("Column is full. Try again.")
                self.movevalid=True
                continue
            if self.check_win(player):
                self.winner=player
                self.runningstatus=False
                print(f"Congratulations {self.winner}! You win!")
                self.base.print_board()
                break
            self.base.switch_turn()
    
#Checking for win conditions in all possible directions (horizontal, vertical, diagonal)
    def check_win(self,player):
        #creating a boolean array to check for 4 in a row for the current player
        win = (self.base.board == player)
        #in horizontal direction
        if np.any(win[:, :-3] & win[:, 1:-2] & win[:, 2:-1] & win[:, 3:]):
            return True
        #in vertical direction
        if np.any(win[:4, :] & win[1:5, :] & win[2:6, :] & win[3:, :]):
            return True
        #in diagonal direction (top-right to bottom-left)
        if np.any(win[:4, 3:7] & win[1:5, 2:6] & win[2:6, 1:5] & win[3:7, 0:4]):
            return True
        #in diagonal direction (top-left to bottom-right)
        if np.any(win[3:7, 3:7] & win[2:6, 2:6] & win[1:5, 1:5] & win[0:4, 0:4]):
            return True
        return False


