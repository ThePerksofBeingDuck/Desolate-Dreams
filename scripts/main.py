import pygame
import random


# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Untitled Survival Game")

# Set up the icon
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

# Set up the clock
clock = pygame.time.Clock()
fps = 60

# Set up game variables
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(fps)

# Quit Pygame
pygame.quit()