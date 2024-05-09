import pygame

# Initialize Pygame
pygame.init()

# Set the window size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the UI images
ui_image = pygame.image.load("assets/ui/ui_elements.png")
settings_image = pygame.image.load("assets/ui/settings.png")

# Extract the normal and pressed states of the play button
play_button_normal_rect = pygame.Rect(163, 210, 90, 27)
play_button_normal_surface = ui_image.subsurface(play_button_normal_rect)
play_button_pressed_rect = pygame.Rect(259, 212, 90, 27)
play_button_pressed_surface = ui_image.subsurface(play_button_pressed_rect)

# Extract the normal, hover, and pressed states of the settings button
settings_button_normal_rect = pygame.Rect(0, 0, 50, 50)
settings_button_normal_surface = settings_image.subsurface(settings_button_normal_rect)
settings_button_hover_rect = pygame.Rect(50, 0, 50, 50)
settings_button_hover_surface = settings_image.subsurface(settings_button_hover_rect)
settings_button_pressed_rect = pygame.Rect(100, 0, 50, 50)
settings_button_pressed_surface = settings_image.subsurface(settings_button_pressed_rect)

# Set the initial state of the play and settings buttons
play_button_state = "normal"
settings_button_state = "normal"

# Setting x any y positions of the play and settings buttons
play_button_xpos = 350
play_button_ypos = 350
settings_button_xpos = 700
settings_button_ypos = 500

# Define the play and settings button rectangles
play_button_rect = pygame.Rect(play_button_xpos, play_button_ypos, 90, 27)
settings_button_rect = pygame.Rect(settings_button_xpos, settings_button_ypos, 50, 50)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the play or settings button was clicked
            if play_button_rect.collidepoint(event.pos):
                play_button_state = "pressed"
            elif settings_button_rect.collidepoint(event.pos):
                settings_button_state = "pressed"
        elif event.type == pygame.MOUSEBUTTONUP:
            play_button_state = "normal"
            settings_button_state = "normal"

    # Clear the screen
    screen.fill((173, 216, 230))

    # Draw the play and settings buttons
    if play_button_state == "normal":
        screen.blit(play_button_normal_surface, (play_button_xpos, play_button_ypos))
    elif play_button_state == "pressed":
        screen.blit(play_button_pressed_surface, (play_button_xpos, play_button_ypos))

    if settings_button_rect.collidepoint(pygame.mouse.get_pos()):
        settings_button_state = "hover"
    else:
        settings_button_state = "normal"

    if settings_button_state == "normal":
        screen.blit(settings_button_normal_surface, (settings_button_xpos, settings_button_ypos))
    elif settings_button_state == "hover":
        screen.blit(settings_button_hover_surface, (settings_button_xpos, settings_button_ypos))
    elif settings_button_state == "pressed":
        screen.blit(settings_button_pressed_surface, (settings_button_xpos, settings_button_ypos))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()