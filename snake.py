import pygame
import assets
from pygame.math import Vector2

class SNAKE:
  
    def __init__(self):
            
        # Tatsächliche Positionen
        self.body = [Vector2(5,10),Vector2(4,10)]
            
        self.direction = Vector2(-1,0) #Startet nach rechts

        self.new_block = False
        self.changed_direction = False          # um sicher zu gehen dass die richtung innerhalb eines updates nur 1x geändert wird
        self.moving = True


            
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = block.x * assets.cell_size
            y_pos = block.y * assets.cell_size
            block_rect = pygame.Rect(x_pos,y_pos,assets.cell_size,assets.cell_size)

            if index == 0: #Kopf
                assets.screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1: #Schwanz
                assets.screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    assets.screen.blit(assets.body_vertical.convert_alpha(),block_rect)
                elif previous_block.y == next_block.y:
                    assets.screen.blit(assets.body_horizontal.convert_alpha(),block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        assets.screen.blit(assets.body_tl.convert_alpha(),block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        assets.screen.blit(assets.body_bl.convert_alpha(),block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        assets.screen.blit(assets.body_tr.convert_alpha(),block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        assets.screen.blit(assets.body_br.convert_alpha(),block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = assets.head_left.convert_alpha()
        elif head_relation == Vector2(-1,0): self.head = assets.head_right.convert_alpha()
        elif head_relation == Vector2(0,1): self.head = assets.head_up.convert_alpha()
        elif head_relation == Vector2(0,-1): self.head = assets.head_down.convert_alpha()

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = assets.tail_left.convert_alpha()
        elif tail_relation == Vector2(-1,0): self.tail = assets.tail_right.convert_alpha()
        elif tail_relation == Vector2(0,1): self.tail = assets.tail_up.convert_alpha()
        elif tail_relation == Vector2(0,-1): self.tail = assets.tail_down.convert_alpha()

    def move_snake(self):
        if self.moving == True:
            if self.new_block == True:
                body_copy = self.body[:]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_block = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy[:]
            self.changed_direction = False  # Zurücksetzen nach jedem Zug

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        assets.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10)]
        self.direction = Vector2(0,0)
