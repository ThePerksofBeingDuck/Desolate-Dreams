# mainmenu.py
import pygame

#setting sizes for buttons
main_menu_button_width = 90
main_menu_button_height = 27
play_button_posx = 350
play_button_posy = 350
setting_button_posx = 350
setting_button_posy = 380
mouse_pos = pygame.mouse.get_pos()

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.ui_elements = pygame.image.load('assets/UI/ui_elements.png')

    #setting button
    def get_setting_button(self, x, y, width, height):
        setting_button = pygame.Surface((width, height), pygame.SRCALPHA)  # Use pygame.SRCALPHA to make the background transparent, even though it already is.
        setting_button.blit(self.ui_elements, (0, 0), pygame.Rect(x, y, width, height))
        return setting_button

    def draw_setting_button(self):
        x, y = (163, 178) 
        pygame.Rect(setting_button_posx, setting_button_posy, main_menu_button_width, main_menu_button_height)
        setting_button_sprite = self.get_setting_button(x, y, main_menu_button_width, main_menu_button_height)
        self.screen.blit(setting_button_sprite, (setting_button_posx, setting_button_posy))

    #play button
    def get_play_button(self, x, y, width, height):
        play_button = pygame.Surface((width, height), pygame.SRCALPHA)
        play_button.blit(self.ui_elements, (0, 0), pygame.Rect(x, y, width, height))
        return play_button
    
    def draw_play_button(self):
        x, y = (163, 210)
        pygame.Rect(play_button_posx, play_button_posy, main_menu_button_width, main_menu_button_height)
        play_button_sprite = self.get_play_button(x, y, main_menu_button_width, main_menu_button_height)
        self.screen.blit(play_button_sprite, (play_button_posx, play_button_posy))

        #getting clicked state buttons
    def get_clicked_play(self, x, y, width, height):
        clicked_play_button = pygame.Surface((width, height), pygame.SRCALPHA)
        clicked_play_button.blit(self.ui_elements, (0,0), pygame.Rect(x, y, width, height))
        return clicked_play_button
    
    def get_clicked_settings(self, x, y, width, height):
        clicked_setting_button = pygame.surface((width, height), pygame.SRCALPHA)
        clicked_setting_button.blit(self.ui_elements, (0,0), pygame.Rect(x, y, width, height))
        return clicked_setting_button
    
    

#checking mouse click

'''
#setting sizes for buttons
main_menu_button_width = 90
main_menu_button_height = 27

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.ui_elements = pygame.image.load('assets/UI/ui_elements.png')
        self.setting_button_rect = pygame.Rect(350, 350, main_menu_button_width, main_menu_button_height)
        self.play_button_rect = pygame.Rect(350, 380, main_menu_button_width, main_menu_button_height)

    def get_button(self, x, y, width, height):
        button = pygame.Surface((width, height), pygame.SRCALPHA)  # Use pygame.SRCALPHA to make the background transparent
        button.blit(self.ui_elements, (0, 0), pygame.Rect(x, y, width, height))
        return button

    def draw_button(self, button_rect, normal_position, pressed_position):
        x, y = normal_position if button_rect.collidepoint(pygame.mouse.get_pos()) and not pygame.mouse.get_pressed()[0] else pressed_position
        button_sprite = self.get_button(x, y, main_menu_button_width, main_menu_button_height)
        self.screen.blit(button_sprite, button_rect.topleft)

    def draw_setting_button(self):
        self.draw_button(self.setting_button_rect, (163, 178), (163, 210))

    def draw_play_button(self):
        self.draw_button(self.play_button_rect, (163, 178), (163, 210))
'''