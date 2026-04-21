import pygame,sys
import numpy as np
from game import basegame
import game
pygame.init()

class othello(basegame):
    def __init__(self,player1,player2):
        super().__init__(player1,player2,8,8)
        self.length=2400
        self.width=1600
        self.running=True
        if self.Current_player==self.player1:
            self.to_move=1
        else:
            self.to_move=-1
        self.cell_size=150
        self.message=" "
        self.screen=pygame.display.set_mode((self.length,self.width))
        pygame.display.set_caption("Othello Game")
        self.BOARD_X=450
        self.BOARD_Y=50
        self.board[3][3]=-1
        self.board[3][4]=1 
        self.board[4][3]=1
        self.board[4][4]=-1
        self.count_black=2
        self.count_white=2


    def draw_board(self):
        for i in range(1,self.Rows):
            pygame.draw.line(self.screen,(0,0,0),(self.BOARD_X,self.BOARD_Y + i*self.cell_size),(self.BOARD_X+self.Columns*self.cell_size,self.BOARD_Y+i*self.cell_size),2)
        for j in range(1,self.Columns):
            pygame.draw.line(self.screen,(0,0,0),(self.BOARD_X+j*self.cell_size,self.BOARD_Y),(self.BOARD_X+j*self.cell_size,self.BOARD_Y+self.Rows*self.cell_size),2)

    def draw_moves(self):
        for row in range(8):
            for col in range(8):
                if self.board[row][col]==1:
                    x=self.BOARD_X+col*self.cell_size+10
                    y=self.BOARD_Y+row*self.cell_size+10
                    pygame.draw.circle(self.screen,(0,0,0),(x+60,y+60),60)
                elif self.board[row][col]==2:
                    x=self.BOARD_X+col*self.cell_size+10
                    y=self.BOARD_Y+row*self.cell_size+10
                    pygame.draw.circle(self.screen,(255,255,255),(x+60,y+60),60)
                else:
                    if self.is_valid_move(row, col, self.to_move):
                        pygame.draw.circle(self.screen, (142,69,133), (self.BOARD_X + col*self.cell_size + self.cell_size//2, self.BOARD_Y + row*self.cell_size + self.cell_size//2), 5)

            
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

    def count_pieces(self):
        self.count_black = np.sum(self.board == 1)
        self.count_white = np.sum(self.board == -1)

    def board_full(self):
        return np.all(self.board != 0)
    

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if self.BOARD_X <= mouse_x < self.BOARD_X + self.Columns*self.cell_size and self.BOARD_Y <= mouse_y < self.BOARD_Y + self.Rows*self.cell_size:
                        col = (mouse_x - self.BOARD_X) // self.cell_size
                        row = (mouse_y - self.BOARD_Y) // self.cell_size
                        if self.is_valid_move(row, col, self.to_move):
                            self.board[row][col] = self.to_move
                            self.change_color(row, col, self.to_move)
                            self.to_move = -self.to_move
                            self.draw_moves()
                            pygame.display.update()
                            self.count_pieces()
                            if np.sum(self.board == 0) == 0 or self.count_black == 0 or self.count_white == 0:
                                pygame.time.wait(500)


                        elif not any(self.is_valid_move(r, c, self.to_move) for r in range(self.Rows) for c in range(self.Columns)):
                            if any(self.is_valid_move(r, c, -self.to_move) for r in range(self.Rows) for c in range(self.Columns)):
                                self.to_move = -self.to_move
                            else:
                                pygame.time.wait(500)
                                self.count_pieces()
                                self.screen.fill((214,234,240))
                                font = pygame.font.SysFont(None, 36)
                                text = font.render("Game Over!", True, (0, 0, 128))
                                self.screen.blit(text, (300, 10))
                                font = pygame.font.SysFont("Arial", 36)
                                if self.count_black > self.count_white:
                                    text = font.render("Black wins!", True, (0, 0, 128))
                                    self.winner= self.player1
                                elif self.count_white > self.count_black:
                                    text = font.render("White wins!", True, (0, 0, 128))
                                    self.winner= self.player2
                                else:
                                    text = font.render("It's a tie!", True, (0, 0, 128))
                                self.screen.blit(text, (300, 50))
                                text=font.render(self.winner +"wins the game!", True, (0, 0, 128))
                                self.screen.blit(text, (300, 100))
                                pygame.display.update()
                                pygame.time.wait(3000)
                                self.running=False

            if self.board_full() or self.count_black == 0 or self.count_white == 0:
                pygame.time.wait(500)
                self.screen.fill((214,234,240))
                font = pygame.font.SysFont("Arial", 36)
                text = font.render("Game Over!", True, (0, 0, 128))                        
                self.screen.blit(text, (300, 10))
                if self.count_black > self.count_white:
                    text = font.render("Black wins!", True, (0, 0, 128))
                    self.winner= self.player1
                elif self.count_white > self.count_black:
                    text = font.render("White wins!", True, (0, 0, 128))
                    self.winner= self.player2
                else:
                    text = font.render("It's a tie!", True, (0, 0, 128))
                self.screen.blit(text, (300, 50))
                text=font.render(self.winner +"wins the game!", True, (0, 0, 128))
                self.screen.blit(text, (300, 100))
                pygame.display.update()
                pygame.time.wait(3000)
                self.running = False
            pygame.display.update()
        pygame.quit()
        sys.exit()