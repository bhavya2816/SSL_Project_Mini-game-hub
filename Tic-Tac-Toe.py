import pygame,sys
 
pygame.init()

screen = pygame.display.set_mode((800,600))
running = True
pygame.display.set_caption("Tic-Tac-Toe")
icon = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)
BOARD = pygame.image.load('bruh.png')
X_IMG = pygame.image.load('X.png')
O_IMG = pygame.image.load('O.png')
board = [[1,2,3],[4,5,6],[7,8,9]]
graphical_board = [[[None,None],[None,None],[None,None]],
                   [[None,None],[None,None],[None,None]],
                   [[None,None],[None,None],[None,None]]]
to_move = 'X'
screen.fill((255,255,255))
image_rect = BOARD.get_rect(center=(400,300))
screen.blit(BOARD,image_rect)
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
