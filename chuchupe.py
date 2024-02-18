import pygame,sys
from pygame.math import Vector2
import assets
from fruits import FRUIT
from snake import SNAKE
from menu import Menu

pygame.init()

class MAIN:
    def __init__(self):
            self.snake = SNAKE()
            self.fruit = FRUIT()

    def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

    def draw_elements(self):
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.draw_score()

    def check_collision(self):
            if self.fruit.pos == self.snake.body[0]:
                self.fruit.randomize()
                self.snake.add_block()
                self.snake.play_crunch_sound()

            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()

    def check_fail(self):
        if gamemode == "openBorder":
            # Wenn die Schlange den linken Rand erreicht
            if self.snake.body[0].x < 0:
                self.snake.body[0].x = assets.cell_number_w - 1
            # Wenn die Schlange den rechten Rand erreicht
            if self.snake.body[0].x >= assets.cell_number_w:
                self.snake.body[0].x = 0
            # Wenn die Schlange den oberen Rand erreicht
            if self.snake.body[0].y < 0:
                self.snake.body[0].y = assets.cell_number_h - 1
            # Wenn die Schlange den unteren Rand erreicht
            if self.snake.body[0].y >= assets.cell_number_h:
                self.snake.body[0].y = 0
        
        if gamemode == "closedBorder":
            if not 0 <= self.snake.body[0].x < assets.cell_number_w or not 0 <= self.snake.body[0].y < assets.cell_number_h:
                self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    def game_over(self):
            global game_state
            game_state = "menu"
            self.snake.reset()

    def reset_game():
        global main_game, is_paused, game_state
        is_paused = False
        main_game = MAIN()
        game_state = "game"

    def draw_grass(self):
            grass_color = (167,209,61)
            for row in range(assets.cell_number_h):
                if row % 2 == 0: 
                    for col in range(assets.cell_number_w):
                        if col % 2 == 0:
                            grass_rect = pygame.Rect(col * assets.cell_size,row * assets.cell_size,assets.cell_size,assets.cell_size)
                            pygame.draw.rect(assets.screen,grass_color,grass_rect)
                else:
                    for col in range(assets.cell_number_w):
                        if col % 2 != 0:
                            grass_rect = pygame.Rect(col * assets.cell_size,row * assets.cell_size,assets.cell_size,assets.cell_size)
                            pygame.draw.rect(assets.screen,grass_color,grass_rect)			

    def draw_score(self):
            score_text = str(len(self.snake.body) - 2)
            score_surface = assets.game_font.render(score_text,True,(56,74,12))
            score_x = assets.cell_size * assets.cell_number_w - 60
            score_y = assets.cell_size * assets.cell_number_h - 40
            score_rect = score_surface.get_rect(center = (score_x,score_y))
            assets.apple_rect = assets.apple.get_rect(midright = (score_rect.left,score_rect.centery))
            bg_rect = pygame.Rect(assets.apple_rect.left,assets.apple_rect.top,assets.apple_rect.width + score_rect.width + 6,assets.apple_rect.height)

            pygame.draw.rect(assets.screen,(167,209,61),bg_rect)
            assets.screen.blit(score_surface,score_rect)
            assets.screen.blit(assets.apple,assets.apple_rect)
            pygame.draw.rect(assets.screen,(56,74,12),bg_rect,2)

def menu():
    global game_state, active_button_index
    menu = Menu(assets.screen)   
    buttons = [menu.start_button, menu.trophy_button, menu.stats_button, menu.quit_button]

    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            for i, button in enumerate(buttons):
                if button.rect.collidepoint(mouse):
                    active_button_index = i
                    break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttons[active_button_index].rect.collidepoint(mouse):  # Verbesserte Logik
                if active_button_index == 0:  # Start
                    MAIN.reset_game()
                    game_state = "game"
                elif active_button_index == 3:  # Quit
                    sys.exit()
                # Füge hier zusätzliche Aktionen für Trophies und Stats ein
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                active_button_index = (active_button_index - 1) % len(buttons)  # Flexible Anpassung
            elif event.key == pygame.K_DOWN:
                active_button_index = (active_button_index + 1) % len(buttons)
            elif event.key == pygame.K_RETURN:
                if active_button_index == 0:
                    MAIN.reset_game()
                    game_state = "game"
                elif active_button_index == 3:
                    sys.exit()
                # Füge hier zusätzliche Aktionen für Trophies und Stats ein

    # Zeichne die Buttons basierend auf dem aktuellen aktiven Button
    for i, button in enumerate(buttons):
        button.set_active(i == active_button_index)
        button._draw_element()

    pygame.display.update()  # Aktualisiere den Bildschirm einmal nach dem Zeichnen aller Elemente

def game():
    global is_paused

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == assets.SCREEN_UPDATE and not is_paused:
            # Aktualisiere das Spiel nur, wenn es nicht pausiert ist
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Umschalten zwischen pausiertem und nicht pausiertem Zustand
                is_paused = not is_paused
            if not is_paused and not main_game.snake.changed_direction:
                # Richtungsänderungen nur verarbeiten, wenn das Spiel nicht pausiert ist
                if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
                    main_game.snake.changed_direction = True
                elif event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
                    main_game.snake.changed_direction = True
                elif event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
                    main_game.snake.changed_direction = True
                elif event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
                    main_game.snake.changed_direction = True

    if is_paused:
        pause_font = pygame.font.Font(assets.font_path, 250)
        pause_text = pause_font.render("PAUSE", True, (255, 255, 255))
        pause_rect = pause_text.get_rect(center=(assets.screen_width / 2, assets.screen_height / 2))
        #assets.screen.fill((175,215,70))  # Fülle den Bildschirm, um frühere Zeichnungen zu löschen
        assets.screen.blit(pause_text, pause_rect)
    else:
        # Zeichne das Spiel, wenn es nicht pausiert ist
        assets.screen.fill((175,215,70))
        main_game.draw_elements()

    pygame.display.update()




main_game = MAIN() 
gamemode = "openBorder"
game_state = "menu"
active_button_index = -1
global is_paused
is_paused = False

while True:
    if game_state == "menu":
         menu()
    elif game_state == "game":
         game()
    


    
    assets.clock.tick(60)