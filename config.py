import pygame

clock = pygame.time.Clock()

# Экран
screen_w = 900
screen_h = 600

screen = pygame.display.set_mode((screen_w, screen_h))

# Название / Лого
pygame.display.set_caption('Vocaloid')
pygame.display.set_icon(pygame.image.load('img/icon.png'))

# Параметры игрока
player = pygame.image.load('img/amogus.png').convert()  # convert_alpha() для картинок без фона
player_speed = 5
player_position = [10, 460]
player_is_falling = True

volume_level = 0

microphone_switch = True
# Блоки и карта

world_pos_x = 0
block_size = 100

_ = False
collision_walls = []
map = [
    [_, _, _, _, 1, _, _, _, _],
    [_, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, 1, _, _],
    [1, 1, _, 1, 1, _, 1, 1, 1]
]
for i, column in enumerate(map):
    for j, line in enumerate(column):
        if line:
            collision_walls.append(pygame.Rect(j * block_size, i * block_size, block_size, block_size))
