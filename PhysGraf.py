""" 
This is a drawing of an appt building (based on one from Physical Grafitti)
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

BLUE = (5, 5, 250)
PURPLE = (144, 5, 250)
YELLOW = (242, 250, 5)
ORANGE = (250, 136, 5)
BROWNISH_GREY = (110,106,105)
GREY_BUILDING = (196,189,187)

PI = 3.141592653

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (900, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Nondescript Building")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREY_BUILDING)
 
    # --- Drawing code should go here
    
    # building one   
    pygame.draw.rect(screen, BROWNISH_GREY, [[0,0],[450,800]],5)
    #building two
    pygame.draw.rect(screen, BROWNISH_GREY, [[450,0],[450,800]],5)
    
    #windows
    x_offset = 0
    while x_offset < 900:
        pygame.draw.rect(screen, WHITE,
                         [[x_offset+50, 150], [50, 100]], 0)
        x_offset = x_offset + 150

    x_offset = 0 
    while x_offset < 900:
        pygame.draw.line(screen, BLACK, [x_offset+50, 200],
                         [x_offset+100, 200], 3)
        x_offset = x_offset + 150
        
   
    #stairs
    y_offset = 0
    x_offset = 0
    while y_offset<125 and x_offset<400:
        pygame.draw.rect(screen, WHITE, [[40+x_offset, 800-y_offset],
                        [500-x_offset, 25]], 0)
        y_offset = y_offset + 25
        x_offset = x_offset + 30

    y_offset = 0
    x_offset = 0
    while y_offset<125 and x_offset<800:
        pygame.draw.rect(screen, WHITE, [[500, 800-y_offset],
                        [350-x_offset, 25]], 0)
        y_offset = y_offset + 25
        x_offset = x_offset + 30
    
    #lines that represent the different floors
    y_offset = 0
    while y_offset<900:
        pygame.draw.line(screen, BLACK, [0, 100+y_offset], [900, 100+y_offset],
                         3)
        y_offset = y_offset + 200

    #left stairwells
    y_offset = 0
    while y_offset < 400:
        pygame.draw.line(screen, BROWNISH_GREY, [150, 100+y_offset],
                         [350, 300+y_offset], 3)
        y_offset = y_offset + 200
   
    #right stairwells
    y_offset = 0
    while y_offset < 400:
        pygame.draw.line(screen, BROWNISH_GREY, [550, 300+y_offset],
                         [750, 100+y_offset], 3)
        y_offset = y_offset + 200

    #left doorway
    pygame.draw.circle(screen, BLACK, (250, 500), 90)
    pygame.draw.rect(screen, BLACK, [[160,500], [180, 200]], 0)

    #right doorway
    pygame.draw.circle(screen, BLACK, (640, 500), 90)
    pygame.draw.rect(screen, BLACK, [[550,500], [180, 200]], 0)
   
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
