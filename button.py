import pygame
import assets

from Text_Element import Textelement

class Button(Textelement):
    """Represents the menu Buttons"""
    def __init__(self, screen, text, color, font_size, x_position, y_position):
        super().__init__(screen, text, color, font_size, x_position, y_position)
        self.button_width = 200
        self.button_height = 50
        self.active = False
        self.rect = pygame.Rect(x_position, y_position, self.button_width, self.button_height)
        
    def set_active(self, active):
        self.active = active
    
    def _draw_element(self):
        """Displays Button on screen"""
        mouse = pygame.mouse.get_pos() 
        button_text = assets.game_font.render(self.text, True, self.font_color)
        text_rect = button_text.get_rect()
        
        # Setze die Button-Farbe basierend auf dem aktiven Zustand oder ob die Maus über dem Button ist
        if self.rect.collidepoint(mouse):
            button_color = (51,204,51)  # Helle Farbe, wenn die Maus über dem Button ist
        else:
            button_color = (51,204,51) if self.active else (47,47,47)  # Unterscheide zwischen aktivem und normalem Zustand
        
        # Zeichne den Button
        self.rect = pygame.draw.rect(
                self.screen, 
                button_color,
                [self.x_position, self.y_position, self.button_width, self.button_height])
        
        # Berechne die neue X- und Y-Position für den Text, um ihn im Button zu zentrieren
        text_x_position = self.x_position + (self.button_width - text_rect.width) / 2
        text_y_position = self.y_position + (self.button_height - text_rect.height) / 2

        # Blit den Text in der neuen, zentrierten Position
        self.screen.blit(button_text, (text_x_position, text_y_position))


 
        