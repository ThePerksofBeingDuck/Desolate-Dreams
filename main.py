import pygame

# Initialize Pygame
pygame.init()

# Set the window size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the UI images
ui_image = pygame.image.load("assets/ui/ui_elements.png")

# Extract the normal and pressed states of the play button
play_button_normal_rect = pygame.Rect(163, 210, 90, 27)
play_button_normal_surface = ui_image.subsurface(play_button_normal_rect)
play_button_pressed_rect = pygame.Rect(259, 212, 90, 27)
play_button_pressed_surface = ui_image.subsurface(play_button_pressed_rect)

# Extract the normal and pressed states of the settings button
settings_button_normal_rect = pygame.Rect(163, 178, 90, 27)
settings_button_normal_surface = ui_image.subsurface(settings_button_normal_rect)
settings_button_pressed_rect = pygame.Rect(259, 180, 90, 27)
settings_button_pressed_surface = ui_image.subsurface(settings_button_pressed_rect)

# Set the initial state of the play and settings buttons
play_button_state = "normal"
settings_button_state = "normal"

# Setting x any y positions of the play and settings buttons
play_button_xpos = 350
play_button_ypos = 350
settings_button_xpos = 350
settings_button_ypos = 390

# Define the play and settings button rectangles
play_button_rect = pygame.Rect(play_button_xpos, play_button_ypos, 90, 27)
settings_button_rect = pygame.Rect(settings_button_xpos, settings_button_ypos, 90, 27)

# Load the images for the settings interface

slider_bg_image = ui_image.subsurface(pygame.Rect(2, 194, 44, 12))
slider_fg_image = ui_image.subsurface(pygame.Rect(2, 210, 44, 12))
slider_handle_image = ui_image.subsurface(pygame.Rect(65, 196, 14, 21))

# Define the position and size of the volume slider
volume_slider_xpos = 200
volume_slider_ypos = 200
volume_slider_width = 44
volume_slider_height = 12

# Define the position and size of the brightness slider
brightness_slider_xpos = 200
brightness_slider_ypos = 250
brightness_slider_width = 44
brightness_slider_height = 12

# Define the initial positions of the slider handles
volume_slider_handle_rect = pygame.Rect(volume_slider_xpos, volume_slider_ypos - slider_handle_image.get_height() // 2, slider_handle_image.get_width(), slider_handle_image.get_height())
brightness_slider_handle_rect = pygame.Rect(brightness_slider_xpos, brightness_slider_ypos - slider_handle_image.get_height() // 2, slider_handle_image.get_width(), slider_handle_image.get_height())

# Define variables to keep track of the slider values and dragging state
volume_slider_value = 50
brightness_slider_value = 50
volume_slider_dragging = False
brightness_slider_dragging = False

# Define functions to handle the movement of the sliders
def move_slider(slider_rect, pos, slider_width, slider_handle_width):
    # Calculate the new position of the slider handle
    new_pos = pos - slider_handle_width // 2
    if new_pos < slider_rect.left:
        new_pos = slider_rect.left
    elif new_pos > slider_rect.right - slider_handle_width:
        new_pos = slider_rect.right - slider_handle_width
    # Update the position of the slider handle
    slider_rect.x = new_pos

def get_slider_value(slider_rect, slider_width, min_value, max_value):
    # Calculate the value of the slider based on the position of the slider handle
    slider_range = max_value - min_value
    handle_range = slider_rect.width - slider_width
    handle_pos = slider_rect.x - slider_rect.left
    slider_value = min_value + round(handle_pos / handle_range * slider_range)
    return slider_value

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
                # Check if the volume or brightness slider handles were clicked
                if volume_slider_handle_rect.collidepoint(event.pos):
                    volume_slider_dragging = True
                elif brightness_slider_handle_rect.collidepoint(event.pos):
                    brightness_slider_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            play_button_state = "normal"
            settings_button_state = "normal"
            # Stop dragging the sliders
            volume_slider_dragging = False
            brightness_slider_dragging = False
        elif event.type == pygame.MOUSEMOTION:
            # Move the slider handles if they are being dragged
            if volume_slider_dragging:
                if slider_bg_image.get_rect(x=volume_slider_xpos, y=volume_slider_ypos).collidepoint(event.pos):
                    move_slider(volume_slider_handle_rect, event.pos[0], volume_slider_width, slider_handle_image.get_width())
                    volume_slider_value = get_slider_value(volume_slider_handle_rect, slider_handle_image.get_width(), 0, 100)
                else:
                    if event.pos[0] < volume_slider_xpos:
                        volume_slider_handle_rect.x = volume_slider_xpos - slider_handle_image.get_width() // 2
                    elif event.pos[0] > volume_slider_xpos + volume_slider_width:
                        volume_slider_handle_rect.x = volume_slider_xpos + volume_slider_width - slider_handle_image.get_width() // 2
            elif brightness_slider_dragging:
                if slider_bg_image.get_rect(x=brightness_slider_xpos, y=brightness_slider_ypos).collidepoint(event.pos):
                    move_slider(brightness_slider_handle_rect, event.pos[0], brightness_slider_width, slider_handle_image.get_width())
                    brightness_slider_value = get_slider_value(brightness_slider_handle_rect, slider_handle_image.get_width(), 0, 100)
                else:
                    if event.pos[0] < brightness_slider_xpos:
                        brightness_slider_handle_rect.x = brightness_slider_xpos - slider_handle_image.get_width() // 2
                    elif event.pos[0] > brightness_slider_xpos + brightness_slider_width:
                        brightness_slider_handle_rect.x = brightness_slider_xpos + brightness_slider_width - slider_handle_image.get_width() // 2

    # Clear the screen
    screen.fill((173, 216, 230))

    # Draw the play and settings buttons
    if play_button_state == "normal":
        screen.blit(play_button_normal_surface, (play_button_xpos, play_button_ypos))
    elif play_button_state == "pressed":
        screen.blit(play_button_pressed_surface, (play_button_xpos, play_button_ypos))

    if settings_button_state == "normal":
        screen.blit(settings_button_normal_surface, (settings_button_xpos, settings_button_ypos))
    elif settings_button_state == "pressed":
        # Draw the settings interface
        screen.blit(slider_bg_image, (volume_slider_xpos, volume_slider_ypos))
        screen.blit(slider_fg_image.subsurface(0, 0, round(volume_slider_value / 100 * (volume_slider_width - slider_handle_image.get_width())), slider_fg_image.get_height()), (volume_slider_xpos, volume_slider_ypos))
        screen.blit(slider_handle_image, (volume_slider_handle_rect.x, volume_slider_ypos - slider_handle_image.get_height() // 2))
        screen.blit(slider_bg_image, (brightness_slider_xpos, brightness_slider_ypos))
        screen.blit(slider_fg_image.subsurface(0, 0, round(brightness_slider_value / 100 * (brightness_slider_width - slider_handle_image.get_width())), slider_fg_image.get_height()), (brightness_slider_xpos, brightness_slider_ypos))
        screen.blit(slider_handle_image, (brightness_slider_handle_rect.x, brightness_slider_ypos - slider_handle_image.get_height() // 2))

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()