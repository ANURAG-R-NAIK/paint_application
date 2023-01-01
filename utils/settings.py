import pygame  #HERE WE ARE USING PYGAME MODULE FOR THE PAINT APPLICATION
pygame.init()  
pygame.font.init()  # THIS IS TO INITIALISE THE FONT LIBRARY

WHITE = (255,255,255)  #TO DEFINE THE COLOURS THIS IS INN FORMAT (RED,GREEN,BLUE)
BLACK = (0,0,0)
RED = (255,0,0)   #ALL CONSTANTS IN CAPITAL LETTERS
GREEN = (0,255,0)
BLUE = (0,0,255)

FPS = 120 #FRAME RATE OF OUR GAME

WIDTH, HEIGHT = 600,700 #DIMENSIONS OF OUR WINDOW

ROW= COLS =100

TOOLBAR_HEIGHT = HEIGHT-WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOUR = WHITE

DRAW_GRID_LINES= False #MAKE FALSE TO REMOVE THE GRID LINES
def get_font(size):
    return pygame.font.SysFont("robust", size)
 