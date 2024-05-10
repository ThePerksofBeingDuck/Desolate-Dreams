import pygame

# Define some constants for the player character
PLAYER_SPEED = 5
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 32

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        # Handle user input to move the player character
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel_x = -PLAYER_SPEED
        elif keys[pygame.K_RIGHT]:
            self.vel_x = PLAYER_SPEED
        else:
            self.vel_x = 0
        if keys[pygame.K_UP]:
            self.vel_y = -PLAYER_SPEED
        elif keys[pygame.K_DOWN]:
            self.vel_y = PLAYER_SPEED
        else:
            self.vel_y = 0

        # Update the position of the player character
        self.x += self.vel_x
        self.y += self.vel_y
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        # Draw the player character on the screen
        screen.blit(self.image, self.rect)