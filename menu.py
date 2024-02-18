import pygame
from pathlib import Path
import assets
from button import Button
from Text_Element import Textelement

class Menu:
    """Represents game menu"""
    def __init__(self, screen):
        #Screen

        grey_background_color = (128, 128, 128)  # Definiere eine graue Farbe
        screen.fill(grey_background_color)  # Fülle den Bildschirm mit Grau

        #self_background_image = pygame.image.load(Path("Graphics/cake.png"))
        #self_background_image = pygame.transform.scale(self_background_image, (assets.screen_width, assets.screen_height))
        self.title = "Chuchupe"
        self.copyright = "© 2024 - Waldarbeiter AG"
        self.width = assets.screen_width
        self.height = assets.screen_height
        #screen.blit(self_background_image, (0, 0))

        #Buttons
        self.start_button = Button(screen, "Start", (101,123,80), 34, (assets.screen_width // 2) - 100, 400)
        self.start_button._draw_element()
        self.trophy_button = Button(screen, "Trophies", (101,123,80), 34, (assets.screen_width // 2) - 100, 500)
        self.trophy_button._draw_element()
        self.stats_button = Button(screen, "Stats", (101,123,80), 34, (assets.screen_width // 2) - 100, 600)
        self.stats_button._draw_element()
        self.quit_button = Button(screen, "Quit", (101,123,80), 34, (assets.screen_width // 2) - 100, 700)
        self.quit_button._draw_element()

        #Text Elements
        self.header = Textelement(screen, self.title, (124,2,0), 78, (assets.screen_width // 2) - 150, 10)._draw_element()
        self.header = Textelement(screen, self.copyright, (255,255,255), 18, (assets.screen_width // 2) - 150, self.height-50)._draw_element()
        pygame.display.update()  
        
        

