import pygame, random
import assets
from pygame.math import Vector2

class FRUIT:
	def __init__(self):
		self.randomize()

	def draw_fruit(self):
		fruit_rect = pygame.Rect(self.pos.x * assets.cell_size, self.pos.y * assets.cell_size, assets.cell_size, assets.cell_size)
		assets.screen.blit(assets.apple,fruit_rect)
		

	def randomize(self):
		self.x = random.randint(0,assets.cell_number_w - 1)
		self.y = random.randint(0,assets.cell_number_h - 1)
		self.pos = Vector2(self.x,self.y)