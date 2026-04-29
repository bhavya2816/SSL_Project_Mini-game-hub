#importing necessary libraries and modules for the game
import pygame,sys
import numpy as np
from game import basegame
import game
#initializing pygame
pygame.init()

#class to control the game flow and manage the board state for Othello inherits from the basegame class
class othello(basegame):
    #initializing the game state, including the board, player turns, and visual elements for the Othello game
    def __init__(self,player1,player2):
        super().__init__(player1,player2,8,8)
        self.length=1920
        self.width=1080
        self.running=True
        self.to_move=1
        self.cell_size=100
        self.message=" "
        self.screen=pygame.display.set_mode((self.length,self.width))
        pygame.display.set_caption("Othello")
        self.BOARD_X=(self.length - self.Columns * self.cell_size) / 2
        self.BOARD_Y = (self.width - self.Rows * self.cell_size) / 2
        self.board[3][3]=-1
        self.board[3][4]=1 
        self.board[4][3]=1
        self.board[4][4]=-1
        self.count_black=2
        self.count_white=2
        self.winner=None

    #function to draw the game board using pygame by drawing lines to create a grid based on the specified number of rows and columns, and also display the current score for both players
    def draw_board(self):
        for i in range(1,self.Rows):
            pygame.draw.line(self.screen,(0,0,0),(self.BOARD_X,self.BOARD_Y + i*self.cell_size),(self.BOARD_X+self.Columns*self.cell_size,self.BOARD_Y+i*self.cell_size),2)
        for j in range(1,self.Columns):
            pygame.draw.line(self.screen,(0,0,0),(self.BOARD_X+j*self.cell_size,self.BOARD_Y),(self.BOARD_X+j*self.cell_size,self.BOARD_Y+self.Rows*self.cell_size),2)
        font = pygame.font.SysFont("comicsansms",80)
        text=font.render(f"{self.player1} : {self.count_black}",True,(0,0,0))
        self.screen.blit(text,(100,400))
        text=font.render(f"{self.player2} : {self.count_white}",True,(255,255,255))
        self.screen.blit(text,(100,550))

    #function to draw moves on the board based on the current state of the game, displaying black and white pieces for each player and indicating valid moves with small circles
    def draw_moves(self):
        for row in range(8):
            for col in range(8):
                x=self.BOARD_X+col*self.cell_size+self.cell_size//2
                y=self.BOARD_Y+row*self.cell_size+self.cell_size//2
                if self.board[row][col]==1:

                    pygame.draw.circle(self.screen,(0,0,0),(x,y),40)
                    pygame.draw.circle(self.screen,(44,44,44),(x,y),30)
                    pygame.draw.circle(self.screen,(0,0,0),(x,y),20)
                elif self.board[row][col]==-1:

                    pygame.draw.circle(self.screen,(255,255,255),(x,y),40)
                    pygame.draw.circle(self.screen,(220,221,220),(x,y),30)
                    pygame.draw.circle(self.screen,(255,255,255),(x,y),20)
                else:
                    if self.is_valid_move(row, col, self.to_move):
                        
                        pygame.draw.circle(self.screen, (142,69,133), (x,y), 10)

    #function to check if the move made by the current player is valid or not
    def is_valid_move(self, row, col, player):
        if self.board[row][col] != 0:
            return False
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            has_opponent_piece = False
            while 0 <= r < self.Rows and 0 <= c < self.Columns:
                if self.board[r][c] == -player:
                    has_opponent_piece = True
                elif self.board[r][c] == player:
                    if has_opponent_piece:
                        return True
                    break
                else:
                    break
                r += dr
                c += dc
        return False
    
    #function to flip the coins on the board after a valid move is made by the current player, changing the color of the pieces according to the rules of Othello
    def change_color(self,row, col, player):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            pieces_to_flip = []
            while 0 <= r < self.Rows and 0 <= c < self.Columns:
                if self.board[r][c] == -player:
                    pieces_to_flip.append((r, c))
                elif self.board[r][c] == player:
                    for rr, cc in pieces_to_flip:
                        self.board[rr][cc] = player
                    break
                else:
                    break
                r += dr
                c += dc

    #function to count the number pieces in the board for white and black
    def count_pieces(self):
        self.count_black = np.sum(self.board == 1)
        self.count_white = np.sum(self.board == -1)

    #function to check if the board is full
    def board_full(self):
        return np.all(self.board != 0)
    

    #function to handle the game loop and user interaction using pygame by listening for events such as mouse clicks to allow players to make their moves and updating the game state accordingly, also checking for valid moves and determining the winner at the end of the game
    def play(self):  
        
        while self.running:
            self.screen.fill((54,117,136))
            pygame.draw.rect(self.screen, (0,0,0), (self.BOARD_X-10, self.BOARD_Y-10, self.Columns*self.cell_size+20, self.Rows*self.cell_size+20))
            pygame.draw.rect(self.screen, (0,171,102), (self.BOARD_X, self.BOARD_Y, self.Columns*self.cell_size, self.Rows*self.cell_size))
            self.draw_board()
            self.draw_moves()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if self.BOARD_X <= mouse_x < self.BOARD_X + self.Columns*self.cell_size and self.BOARD_Y <= mouse_y < self.BOARD_Y + self.Rows*self.cell_size:
                        col = int((mouse_x - self.BOARD_X) // self.cell_size)
                        row = int((mouse_y - self.BOARD_Y) // self.cell_size)
                        #check if the move is valid and update the board state accordingly, also checking for valid moves for both players and determining the winner at the end of the game
                        if self.is_valid_move(row, col, self.to_move):
                            self.board[row][col] = self.to_move
                            self.change_color(row, col, self.to_move)
                            self.to_move = -self.to_move
                            self.draw_moves()
                           
                            pygame.display.update()
                            self.count_pieces()
                            if np.sum(self.board == 0) == 0 or self.count_black == 0 or self.count_white == 0:
                                pygame.time.wait(500)

                        #check if the current player has any valid moves left, if not switch to the other player, and if neither player has valid moves then determine the winner based on the count of pieces on the board
                        elif not any(self.is_valid_move(r, c, self.to_move) for r in range(self.Rows) for c in range(self.Columns)):
                            if any(self.is_valid_move(r, c, -self.to_move) for r in range(self.Rows) for c in range(self.Columns)):
                                self.to_move = -self.to_move
                            else:
                                pygame.time.wait(500)
                                self.count_pieces()
                                self.screen.fill((214,234,240))
                                font = pygame.font.SysFont("Arial", 100)
                                if self.count_black > self.count_white:
                                    self.winner= self.player1
                                elif self.count_white > self.count_black:
                                    self.winner= self.player2
                                else:
                                    text = font.render("It's a tie!", True, (0, 0, 128))
                                    self.screen.blit(text, (300, 50))
                                text=font.render(self.winner + " wins the game!", True, (0, 0, 128))
                                self.screen.blit(text, (500, 500))
                                pygame.display.update()
                                pygame.time.wait(3000)
                                self.running=False

            #check if the board is full or if either player has no pieces left, and determine the winner based on the count of pieces on the board
            if self.board_full() or self.count_black == 0 or self.count_white == 0:
                pygame.time.wait(500)
                self.screen.fill((214,234,240))
                font = pygame.font.SysFont("Arial", 100)
                if self.count_black > self.count_white:
                    self.winner= self.player1
                elif self.count_white > self.count_black:
                    self.winner= self.player2
                else:
                    text = font.render("It's a tie!", True, (0, 0, 128))
                    self.screen.blit(text, (500, 500))
                text=font.render(self.winner + " wins the game!", True, (0, 0, 128))
                self.screen.blit(text, (500, 500))
                pygame.display.update()
                pygame.time.wait(3000)
                self.running = False
            pygame.display.update()
        pygame.quit()
        