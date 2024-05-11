# main.py
import pygame
from pygame.locals import *
from mainmenu import MainMenu

# Initialize Pygame
pygame.init()

# Set the window caption
pygame.display.set_caption('Untitled Game')

# Set the window icon (assuming you have a 32x32 icon.png file in the same directory)
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create the main menu
main_menu = MainMenu(screen)

# Game loop
running = True
while running:
    # Limit the game to run at a certain maximum FPS
    pygame.time.Clock().tick(FPS)

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Draw everything
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Draw the main menu
    main_menu.draw_play_button()
    main_menu.draw_setting_button()

    # Flip the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
