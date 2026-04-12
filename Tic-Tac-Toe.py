import pygame,sys
import numpy as np
pygame.init()
screen = pygame.display.set_mode((700,610))
running = True 
win_line = None
pygame.display.set_caption("Tic-Tac-Toe")
icon = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)
X_IMG = pygame.image.load('X.png')
O_IMG = pygame.image.load('O.png')
ROWS = 10
COLS = 10
CELL_SIZE = 60
BOARD_X = 50
BOARD_Y = 5
X_IMG = pygame.transform.scale(X_IMG, (CELL_SIZE, CELL_SIZE))
O_IMG = pygame.transform.scale(O_IMG, (CELL_SIZE, CELL_SIZE))
def draw_board():
    
    for i in range(1,ROWS):
        pygame.draw.line(screen,(0,0,0),(BOARD_X,BOARD_Y + i*CELL_SIZE),(BOARD_X+COLS*CELL_SIZE,BOARD_Y+i*CELL_SIZE),2)
    
    for j in range(1,COLS):
        pygame.draw.line(screen,(0,0,0),(BOARD_X+j*CELL_SIZE,BOARD_Y),(BOARD_X+j*CELL_SIZE,BOARD_Y+ROWS*CELL_SIZE),2)

#creates a 10x10 grid (list of lists)
board = np.zeros((10,10),dtype=int)
#shows whose turn it is and first turn is of 'X'
to_move = 1
def draw_moves():
    for row in range(10):
        for col in range(10):
            if board[row][col]==1:
                x=BOARD_X+col*CELL_SIZE
                y=BOARD_Y+row*CELL_SIZE
                screen.blit(X_IMG,(x,y))
            elif board[row][col]==2:
                x=BOARD_X+col*CELL_SIZE
                y=BOARD_Y+row*CELL_SIZE
                screen.blit(O_IMG,(x,y))

def check_winner():
    global running,win_line
    #horizontal
    for row in range(10):
        L=board[row]
        for col in range(6):
            if L[col]==L[col+1]==L[col+2]==L[col+3]==L[col+4] :
                win_line = ((row,col),(row,col+4))
                if L[col]==1:
                    draw_line()
                    print("player 'X' is winner!!")
                    running = False
                elif L[col]==2:
                    draw_line()
                    print("player 'O' is winner!!")
                    running = False
    #vertical
    for col in range(10):
        for row in range(6):
            if board[row][col]==board[row+1][col]==board[row+2][col]==board[row+3][col]==board[row+4][col]:
                win_line=((row,col),(row+4,col))
                if board[row][col]==1:
                    draw_line()
                    print("winner is player 'X'")
                    running=False
                elif board[row][col]==2:
                    draw_line()
                    print("winner is player 'O'")
                    running=False
    #left-up cross
    for row in range(6):
        for col in range(6):
            if board[row][col]==board[row+1][col+1]==board[row+2][col+2]==board[row+3][col+3]==board[row+4][col+4]:
                win_line=((row,col),(row+4,col+4))
                if board[row][col]==1:
                    draw_line()
                    print("winner is player 'X' !!")
                    running=False
                elif board[row][col]==2:
                    draw_line()
                    print("winner is player 'O' !!")
                    running=False
    #right-up cross
    for row in range(9,3,-1):
        for col in range(6):
            if board[row][col]==board[row-1][col+1]==board[row-2][col+2]==board[row-3][col+3]==board[row-4][col+4]:
                win_line=((row,col),(row-4,col+4))
                if board[row][col]==1:
                    draw_line()
                    print("winner is player 'X' !!")
                    running=False
                elif board[row][col]==2:
                    draw_line()
                    print("winner is player 'O' !!")
                    running=False
    if not np.any(board == 0):
        print("Draw!")
        running=False
    
def draw_line():
    (r1,c1),(r2,c2)=win_line
    start = (BOARD_X+c1*CELL_SIZE+CELL_SIZE//2,BOARD_Y+r1*CELL_SIZE+CELL_SIZE//2)
    end=(BOARD_X+c2*CELL_SIZE+CELL_SIZE//2,BOARD_Y+r2*CELL_SIZE+CELL_SIZE//2)
    pygame.draw.line(screen,(255,0,0),start,end,6)
        

while running:
    screen.fill((245,245,220))
    draw_board()
    draw_moves()
    check_winner()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()

            col = (mouse_x - BOARD_X)//CELL_SIZE
            row = (mouse_y - BOARD_Y)//CELL_SIZE
            if 0<=row<10 and 0<=col<10:
                if board[row][col]==0:
                    board[row][col]=to_move
                    if to_move==1:
                        to_move=2
                    else:
                        to_move=1
    pygame.display.update()
