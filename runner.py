# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((200, 200, 200))

    # Draw cards
    pygame.draw.rect(screen, (0, 0, 200), (20, 20, 60, 100), 2)
    pygame.draw.rect(screen, (0, 0, 200), (100, 20, 60, 100), 2)
    pygame.draw.rect(screen, (0, 0, 200), (20, 140, 60, 100), 2)
    pygame.draw.rect(screen, (0, 0, 200), (100, 140, 60, 100), 2)

    pygame.draw.rect(screen, (0, 0, 0), (200, 80, 60, 100), 2)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
