from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DRAWING BOARD")



def init_grid(rows, cols, colour):
    grid = []
 #HERE WE ARE MAKING A GRID PF PIXELS AND EACH PIXEL INSIDE THE GRID IS GOING TO BE A TUPLE INDICATING THE DEFINATION OF THE COLOUR OF THAT PIXEL
 #LIKE (255,0,0)  IF THE PIXEL IS RED IN COLOUR
    for i in range(rows):
        grid.append([])
        for _ in range(cols):  #if u dont want to use the variable in for loop just giving undesccore will run the forloop
            grid[i].append(colour)
    return grid





def draw_grid(win, grid):
    for i, row in enumerate(grid): #ENUMERATE GIVES THE TUPLE VALUE ALONG WITH THE INDEX VALUE 0:[(255,255,255)]
        for j, pixel in enumerate(row): 
            
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE,PIXEL_SIZE,PIXEL_SIZE)) # just take the value of the pixel dimensions and after colouring moves to the next pixel like 25,50,75,100
    
    
                                #the top left corner of the window is our origin
    if DRAW_GRID_LINES:
        for i in range(ROW  + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH , i * PIXEL_SIZE)) #here the statring and ending of x remains same just y varies
            
        for i in range(COLS + 1):
             pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT)) # TO AVOID DRAWING LINES WHERE THE TOOLBAR IS
                    
        



def draw(win, grid, buttons):
    win.fill(BG_COLOUR)  #FILL THE BG COLOUR AS WHITE
    draw_grid(win, grid)
    
    for button in buttons:
        button.draw(win)
    
    pygame.display.update()  #ANY CHANGES MADE SAVE THE CHANGES


def get_row_col_from_pos(pos):
     x, y = pos
     row = y // PIXEL_SIZE
     col = x // PIXEL_SIZE  
     if row >= ROW:
        raise  IndexError  # INCASE WE PRESS ON AN EXCEPTION BUTTON
     return row, col
 

run = True
clock = pygame.time.Clock()
grid = init_grid(ROW, COLS, BG_COLOUR)
drawing_colour= BLACK


button_y= HEIGHT - TOOLBAR_HEIGHT/2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK), 
    Button(70, button_y, 50, 50, RED), 
    Button(130, button_y, 50, 50, GREEN), 
    Button(190, button_y, 50, 50, BLUE),
    Button(250, button_y, 50, 50, WHITE , "Erase" , BLACK),
    Button(310, button_y, 50, 50, WHITE,  "Clear", BLACK)
]


while run: 
    clock.tick(FPS)  # TO MAKE SURE THAT THE GAME RUNS AT THE SAME DPEED FOR ALL THE COMPUTERS
    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #RUN ALL THE CODES THE USER WANTS AND IF EXIT BUTTON IS PRESSED THEN EXIT THE LOOP
            run = False
            
        if pygame.mouse.get_pressed()[0]:   # TO CHECK IF USER PRESSED LEFT MOUSE BUTTON 0-LEFT
                pos = pygame.mouse.get_pos()
                try:
                    row, col= get_row_col_from_pos(pos)
                    grid[row][col] = drawing_colour
                
                
                except IndexError:
                    for button in buttons:
                        if not button.clicked(pos):
                            continue
                        
                        if button.text == "Clear" :
                            grid = init_grid(ROW, COLS, BG_COLOUR)
                            drawing_colour = BLACK
                        
                        drawing_colour = button.colour
                        break

    
    
    draw(WIN, grid, buttons)

pygame.quit()



