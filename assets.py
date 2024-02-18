import pygame

pygame.init()
#pygame.mixer.pre_init(44100,-16,2,512)

# Bildschirmauflösung abfragen
infoObject = pygame.display.Info()
screen_width, screen_height = infoObject.current_w, infoObject.current_h

cell_size = 40
cell_number_w = screen_width // cell_size # 1920 / 40 = 48
cell_number_h = screen_height // cell_size # 1080 / 40 = 27
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
font_path = "Font/PoetsenOne-Regular.ttf"

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,80) #bewegung alle 80 ms

head_up = pygame.image.load('Graphics/head_up.png')
head_down = pygame.image.load('Graphics/head_down.png')
head_right = pygame.image.load('Graphics/head_right.png')
head_left = pygame.image.load('Graphics/head_left.png')

tail_up = pygame.image.load('Graphics/tail_up.png')
tail_down = pygame.image.load('Graphics/tail_down.png')
tail_right = pygame.image.load('Graphics/tail_right.png')
tail_left = pygame.image.load('Graphics/tail_left.png')

body_vertical = pygame.image.load('Graphics/body_vertical.png')
body_horizontal = pygame.image.load('Graphics/body_horizontal.png')

body_tr = pygame.image.load('Graphics/body_tr.png')
body_tl = pygame.image.load('Graphics/body_tl.png')
body_br = pygame.image.load('Graphics/body_br.png')
body_bl = pygame.image.load('Graphics/body_bl.png')
crunch_sound = pygame.mixer.Sound('Sounds/crunch.wav')