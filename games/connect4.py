#Importing necessary libraries and modules for the game
import sys
import numpy as np
import pygame
from game import basegame

#Class to control the game flow and manage the board state
class connect4(basegame):
    #Initializing the game with player names, board dimensions, and setting up the pygame window
    def __init__(self,player1,player2):
        super().__init__(player1,player2,7,7)
        self.length=2400
        self.height=1600    
        self.runningstatus=True
        self.movevalid=True
        if self.Current_player==self.player1:
            self.player=1
        else:           
            self.player=2
        self.blocksize=180
        self.message=""
        pygame.init()
        self.screen=pygame.display.set_mode((self.length, self.height))


    #Function to drop a piece in the selected column 
    def drop_piece(self,col,player):
        #checking whether the selected column is within the valid range and not full, then placing the piece in the lowest available row in that column
        if col>=0 and col<self.Columns:
            if self.board[0][col]!=0:
                self.movevalid=False 
                self.message="Column is full, try another column."
                return 0
            #Dropping the piece in the lowest available row in the selected column
            for r in range(6,-1,-1):
                if self.board[r][col]==0:
                    self.board[r][col]=player
                    #Drawing the piece on the pygame window at the appropriate position based on the row and column
                    pygame.draw.circle(self.screen, (255, 180, 150) if self.player==1 else (180, 160, 255) ,
                                    (int((self.length-self.Columns*self.blocksize)/2+ col*self.blocksize + self.blocksize/2),
                                        int(r*self.blocksize + self.blocksize + self.blocksize/2)),
                                    60)
                    
                    pygame.display.update()
                    return 1
                
            return 0
    
    #Function to check if the board is full (indicating a draw)       
    def board_full(self):
        return np.all(self.board != 0)
    
    #Function to display the winner and end the game
    def show_winner(self):
        self.screen.fill((255,180,150  ))
        font = pygame.font.SysFont("Arial", 150)
        if self.winner != None:
            text = font.render(f"{self.winner} wins! ", True, (0, 0, 0))
        else:
            text = font.render("It's a draw!", True, (0, 0, 0))
        self.screen.blit(text, (self.length//2 - text.get_width()//2, self.height//2 - text.get_height()//2))
        pygame.display.update()
        
    #pygame function to draw the game board
    def draw_board(self, board, screen):
        
        for c in range(self.Columns):
            for r in range(self.Rows):
                pygame.draw.rect(self.screen, ((170, 230, 210)),
                                ((self.length-self.Columns*self.blocksize)/2+c*self.blocksize,r*self.blocksize+self.blocksize,
                                self.blocksize, self.blocksize))

                pygame.draw.circle(self.screen, (255,255,255),
                                (int((self.length-self.Columns*self.blocksize)/2+ c*self.blocksize + self.blocksize/2),
                                    int(r*self.blocksize + self.blocksize + self.blocksize/2)),
                                60)

        pygame.display.update()

    #Function to handle the game loop and user interactions
    def play(self):
            
            self.screen.fill((255, 245, 240))
            self.draw_board(self.board, self.screen)

            while self.runningstatus:
               
                #Displaying messages related to invalid moves or game outcomes at the top of the screen
                font = pygame.font.SysFont(None,80)
                text = font.render(self.message, True, (0,0,0))
                self.screen.blit(text, (700, 10)) 

                self.message=f"{self.Get_current_player()}'s turn. Click to drop a piece."

                for event in pygame.event.get():
                    pygame.display.set_caption("MiniGameHub-Connect4")

                    if event.type==pygame.QUIT:
                        self.runningstatus=False
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        x=event.pos[0]
                        col=int((x-600)/self.blocksize)
                        self.movevalid=True
                        self.drop_piece(col,self.player)
                        if self.movevalid:
                            if self.check_win(self.player):
                                pygame.draw.rect(self.screen, (255,245,240), (0,0,self.length,100))
                                self.message=f"{self.Get_current_player()} wins!"
                                text = font.render(self.message, True, (0,0,0))                                
                                self.screen.blit(text, (700, 10))
                                pygame.display.update()
                                pygame.time.wait(1000)
                                if self.player==1:
                                    self.winner=self.player1
                                elif self.player==2:
                                    self.winner=self.player2
                                self.show_winner()
                                wait_time=4000
                                pygame.time.wait(wait_time)
                                self.runningstatus=False
                            else:
                                self.switch_turn()
                                if self.Get_current_player()==self.player1:
                                    self.player=1
                                elif self.Get_current_player()==self.player2:
                                    self.player=2
                        else:
                            pygame.display.set_caption("Invalid move! Try again.")
                            self.movevalid=True

                pygame.display.update()
                #Checking for a draw condition after each move by verifying if the board is full without any winner
                if self.board_full():
                    self.winner=None
                    self.show_winner()
                    self.runningstatus=False
                
                 #Clearing the message area at the top of the screen before displaying any new messages related to invalid moves or game outcomes
                pygame.draw.rect(self.screen, (255,245,240), (0,0,self.length,100))

            pygame.quit()
            

                         

    #Checking for win conditions in all possible directions (horizontal, vertical, diagonal)
    def check_win(self,player):
        #Creating a boolean array to check for 4 in a row for the current player using masking

        win = (self.board == player)
        #in horizontal direction
        if np.any(win[:, :-3] & win[:, 1:-2] & win[:, 2:-1] & win[:, 3:]):
            return True
        #in vertical direction
        elif np.any(win[:-3, :] & win[1:-2, :] & win[2:-1, :] & win[3:, :]):
            return True
        #in diagonal direction (top-right to bottom-left)
        elif np.any(win[:-3, :-3] & win[1:-2, 1:-2] & win[2:-1, 2:-1] & win[3:, 3:]):
            return True 
        #in diagonal direction (top-left to bottom-right)
        elif np.any(win[:-3, 3:7] & win[1:-2, 2:6] & win[2:-1, 1:5] & win[3:7, 0:4]):
            return True
        else:
            return False



