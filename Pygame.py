import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

#Run until the user asks to quit
running = True
while running:
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    # Fill the background of the window with white
    screen.fill((255, 255, 255))

    # Draw a blue circle in the center
    pygame.draw.circle(screen, (100, 0, 255), (250, 250), 150)
    
    # Flip the display
    pygame.display.flip()

# Quit the code
pygame.quit()