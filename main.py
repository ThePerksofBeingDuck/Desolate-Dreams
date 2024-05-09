import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (640, 480)

# Create the Pygame window
screen = pygame.display.set_mode(window_size)

# Load the player sprite sheet
player_sprite_sheet = pygame.image.load('idle.png').convert_alpha()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.width = 11
        self.height = 14
        self.image_index = 0
        self.images = []
        # Load the player images from the sprite sheet
        sprite_sheet_path = 'untiteled-game/assets/sprites/idle.png'
        sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        for row in range(4):
            for col in range(4):
                image_rect = pygame.Rect(col * 80, row * 80, 11, 14)
                image = sprite_sheet.subsurface(image_rect)
                self.images.append(image)