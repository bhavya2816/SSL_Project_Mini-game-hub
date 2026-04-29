#Importing necessary libraries and modules
import pygame,sys
import numpy as np
from game import basegame
import game
#Initializing pygame
pygame.init()

#Class to control the game flow and manage the board state for Tic Tac Toe inherits from the basegame class
class tic_tac_toe(basegame):
    def __init__(self,player1,player2):
        super().__init__(player1,player2,10,10)
        self.length=1920
        self.width=1080
        self.running=True
        if self.Current_player==self.player1:
            self.to_move=1
        else:
            self.to_move=2
        self.cell_size=100
        self.message=" "
        self.screen=pygame.display.set_mode((self.length,self.width))
        self.BOARD_X = (self.length - self.Columns * self.cell_size) // 2
        self.BOARD_Y = (self.width - self.Rows * self.cell_size) // 2
        self.win_line=None
        self.winner=None
        #Loading and scaling the images for X and O to be displayed on the board when a player makes a move
        self.X_IMG = pygame.image.load('games/X.png')
        self.O_IMG = pygame.image.load('games/O.png')
        self.X_IMG = pygame.transform.scale(self.X_IMG, (self.cell_size-10, self.cell_size-10))
        self.O_IMG = pygame.transform.scale(self.O_IMG, (self.cell_size-10, self.cell_size-10))

    #Function to draw the game board using pygame by drawing lines to create a grid based on the specified number of rows and columns
    def draw_board(self):
        pygame.display.set_caption("Tic-Tac-Toe")
        for i in range(1,self.Rows):
            pygame.draw.line(self.screen,(0,0,0),(self.BOARD_X,self.BOARD_Y + i*self.cell_size),(self.BOARD_X+self.Columns*self.cell_size,self.BOARD_Y+i*self.cell_size),3)
        for j in range(1,self.Columns):
            pygame.draw.line(self.screen,(0,0,0),(self.BOARD_X+j*self.cell_size,self.BOARD_Y),(self.BOARD_X+j*self.cell_size,self.BOARD_Y+self.Rows*self.cell_size),3)

    #Function to check winning condition
    def check_winner(self):
        #Creating a boolean array to check for 5 in a row for the current player using masking
        win= (self.board==self.to_move)
        #horizontal
        if np.any(win[:-4,:] & win[1:-3,:] & win[2:-2,:] & win[3:-1,:] & win[4:,:]):
            return True
        #vertical
        if np.any(win[:,:-4] & win[:,1:-3] & win[:,2:-2] & win[:,3:-1] & win[:,4:]):                
            return True
        #left-up cross
        if np.any(win[:-4,:-4] & win[1:-3,1:-3] & win[2:-2,2:-2] & win[3:-1,3:-1] & win[4:,4:]):    
            return True
        #right-up cross
        if np.any(win[:-4,4:] & win[1:-3,3:-1] & win[2:-2,2:-2] & win[3:-1,1:-3] & win[4:,:-4]):    
            return True 
        return False

    #Function to check if the board is full (indicating a draw)    
    def board_full(self):
        return not np.any(self.board == 0)
    
    #Function to display the winner and end the game using pygame by filling the screen with a color and displaying a message indicating the winner or if it's a draw
    def show_winner(self):
        self.screen.fill((135,206,250))
        font=pygame.font.SysFont("Ariel", 90)
        if self.winner!=None:
            text=font.render(f"{self.winner} wins!", True, (0,0,0))
        else:
            text=font.render("It's a draw!", True, (0,0,0))
        self.screen.blit(text,(self.length//2-text.get_width()//2,self.width//2-text.get_height()//2))
        pygame.display.update()
        pygame.time.wait(3000)

        
    #Function to handle the game loop and user interactions using pygame by listening for events such as mouse clicks to allow players to make their moves and updating the game state accordingly
    def play(self):
        self.running = True
        self.screen.fill((245,245,220))
        self.draw_board()
        while self.running:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x=event.pos[0]
                    y=event.pos[1]
                    col =int((x - self.BOARD_X)//self.cell_size)
                    row = int((y - self.BOARD_Y)//self.cell_size)
                    if 0<=row<10 and 0<=col<10:
                        if self.board[row][col]==0:
                            self.board[row][col]=self.to_move
                            self.screen.blit(self.X_IMG if self.to_move==1 else self.O_IMG,(self.BOARD_X+col*self.cell_size+5,self.BOARD_Y+row*self.cell_size+5))
                            pygame.display.update()
                            
                            if self.check_winner():
                                self.winner=self.Current_player
                                pygame.time.wait(1000)
                                self.show_winner()
                                self.running=False
                            elif self.board_full():
                                self.winner=None
                                self.show_winner()
                                self.running=False
                            else:
                                self.switch_turn()
                                if self.Get_current_player()==self.player1:
                                    self.to_move=1
                                else:
                                    self.to_move=2

            pygame.display.update()
        pygame.quit()
