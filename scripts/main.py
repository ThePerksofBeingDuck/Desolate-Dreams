import pygame
import random
from environment import EnvironmentGenerator


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

# Create the environment generator
environment = EnvironmentGenerator()

# Generate initial environment tiles
environment.generate_tiles(300)

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Generate new environment tiles as needed
    if environment.current_row * environment.tiles_per_col < len(environment.tiles) - 300:
        environment.generate_tiles(100)

    # Draw environment tiles
    environment.draw_tiles(screen)

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(fps)

# Quit Pygame
pygame.quit()