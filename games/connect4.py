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

        #Screen dimensions
        self.length=1920
        self.height=1080

        #Varibale indicating game state    
        self.runningstatus=True
        self.movevalid=True

        #Assigning a numeric value to current player
        if self.Current_player==self.player1:
            self.player=1
        else:           
            self.player=2

        #Blocksize for each grid
        self.blocksize=120

        #centering the board on screen
        self.X_posn=(self.length-self.Columns*self.blocksize)/2
        self.Y_posn=(self.height-self.Rows*self.blocksize)/2

        #Initializing pygame window
        pygame.init()
        self.screen=pygame.display.set_mode((self.length, self.height))
        
    #pygame function to draw the game board
    def draw_board(self, board, screen):
        self.screen.fill((245,245,220))

        # Draw outer board rectangle
        pygame.draw.rect(self.screen,(0,0,255),(self.X_posn-100,self.Y_posn-50,
                         self.Columns*self.blocksize+200,self.blocksize*self.Rows+100))
        
       # Draw border  
        pygame.draw.rect(self.screen,(0,0,0),(self.X_posn-100,self.Y_posn-50,
                         self.Columns*self.blocksize+200,self.blocksize*self.Rows+100),8)
        
        # Draw grid cells and empty circles
        for c in range(self.Columns):
            for r in range(self.Rows):
                pygame.draw.rect(self.screen, ((0,0,255)),
                                ((self.length-self.Columns*self.blocksize)/2+c*self.blocksize,r*self.blocksize+self.blocksize,
                                self.blocksize, self.blocksize))
                
                #Drawing slot
                pygame.draw.circle(self.screen, (245,245,220),(int((self.length-self.Columns*self.blocksize)/2+ c*self.blocksize + self.blocksize/2),
                                    int(r*self.blocksize + self.blocksize + self.blocksize/2)),45)
                
                #drawing Slot Border
                pygame.draw.circle(self.screen,(0,0,0),(int((self.length-self.Columns*self.blocksize)/2+ c*self.blocksize + self.blocksize/2),
                                    int(r*self.blocksize + self.blocksize + self.blocksize/2)),45,5)
                
                pygame.draw.circle(self.screen,(0,0,0),(int((self.length-self.Columns*self.blocksize)/2+ c*self.blocksize + self.blocksize/2),
                                    int(r*self.blocksize + self.blocksize + self.blocksize/2)),53,5)
               

    #to get previous board after each move
    def get_board(self):
        for r in range(7):
            for c in range(7):
                if self.board[r][c] !=0:
                    pygame.draw.circle(self.screen,(255,0,0) if self.board[r][c]==1 else (255,255,0),
                                       (self.X_posn+c*self.blocksize+self.blocksize/2,
                                        self.Y_posn+r*self.blocksize+self.blocksize/2),40)


    #Function for animating the drop
    def drop_animation(self,col,final_row,Player):
        x=self.X_posn+col*self.blocksize+self.blocksize//2
        y=80                         #Starting height
        target_y=self.Y_posn+final_row*self.blocksize+self.blocksize/2      # Final y 

        while y<=target_y+10:
            self.draw_board(self.board,self.screen)
            self.get_board()

            pygame.draw.circle(self.screen,(255,0,0) if Player==1 else (255,255,0),(x,y),40)
            pygame.display.update()
            clock=pygame.time.Clock()
            clock.tick(60)                      # Control Animation speed

            y+=20


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
                    
                    self.drop_animation(col,r,player)
                    self.board[r][col]=player
                    
                    pygame.display.update()                    
                    return 1                
            return 0

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

    #Function to check if the board is full (indicating a draw)       
    def board_full(self):
        return np.all(self.board != 0)
    
    #Function to display the winner and end the game
    def show_winner(self):
        self.screen.fill((255,180,150))
        font = pygame.font.SysFont("Arial", 150)
        if self.winner != None:
            text = font.render(f"{self.winner} wins! ", True, (0, 0, 0))
        else:
            text = font.render("It's a draw!", True, (0, 0, 0))
        self.screen.blit(text, (self.length//2 - text.get_width()//2, self.height//2 - text.get_height()//2))
        pygame.display.update()
        pygame.time.wait(2000)
    
        
    
    #Function to handle the game loop and user interactions
    def play(self):

            while self.runningstatus:
                self.draw_board(self.board,self.screen)
                self.get_board()
                #Displaying whose turn it is now
                font = pygame.font.SysFont(None,80)
                text = font.render(f"{self.Current_player}'s turn. Click to drop a piece.", True, (0,0,0))
                self.screen.blit(text, (500, 10)) 

                for event in pygame.event.get():
                    pygame.display.set_caption("MiniGameHub-Connect4")

                    #Quit event Handling
                    if event.type==pygame.QUIT:
                        self.runningstatus=False
                        pygame.quit()
                        sys.exit()

                    #handling mouse click
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        x=event.pos[0]
                        #Finding column from X-Co-ordinate
                        col=int((x-self.X_posn)/self.blocksize)
                        self.movevalid=True
                        self.drop_piece(col,self.player)
                        if self.movevalid:

                            #Check for win
                            if self.check_win(self.player):
                                self.message=f"{self.Current_player} wins!"
                                text = font.render(self.message, True, (0,0,0))                                
                                self.screen.blit(text, (500, 10))
                                pygame.display.update()
                                pygame.time.wait(1000)
                                if self.player==1:
                                    self.winner=self.player1
                                elif self.player==2:
                                    self.winner=self.player2
                                self.show_winner()
                                self.runningstatus=False
                            #Check for draw
                            elif self.board_full():
                                self.winner=None
                                self.show_winner()
                                self.runningstatus=False 
                            # Switching turns if game is not over   
                            else:
                                self.switch_turn()
                                if self.Current_player==self.player1:
                                    self.player=1
                                elif self.Current_player==self.player2:
                                    self.player=2
                        #Asking to chose another move if move is not invalid i.e, col is full
                        else:
                            pygame.display.set_caption("Invalid move! Try again.")
                            self.movevalid=True

                pygame.display.update()
            pygame.quit()  
    
            

                         

    