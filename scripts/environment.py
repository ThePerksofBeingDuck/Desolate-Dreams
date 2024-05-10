import random
import pygame

class EnvironmentGenerator:
    def __init__(self):
        self.tile_size = 32
        self.tiles_per_row = 20
        self.tiles_per_col = 15
        self.current_row = 0
        self.current_col = 0
        self.tiles = []

    def generate_tile(self):
        # Generate a new environment tile
        tile_type = random.choice(["grass", "water", "sand", "rock"])
        tile_image = pygame.image.load(tile_type + ".png").convert_alpha()
        tile_rect = tile_image.get_rect()
        tile_rect.x = self.current_col * self.tile_size
        tile_rect.y = self.current_row * self.tile_size
        self.tiles.append((tile_image, tile_rect))
        self.current_col += 1
        if self.current_col > self.tiles_per_row:
            self.current_col = 0
            self.current_row += 1

    def generate_tiles(self, num_tiles):
        # Generate a specified number of environment tiles
        for i in range(num_tiles):
            self.generate_tile()

    def draw_tiles(self, surface):
        # Draw the environment tiles on the screen
        for tile in self.tiles:
            surface.blit(tile[0], tile[1])