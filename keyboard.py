import pygame
from config import *


class Keyboard:
    def __init__(self):
        self.x, self.y = player_position
        self.world_pos_x = world_pos_x
        self.microphone_switch = microphone_switch
        self.volume_level = volume_level
        self.player_is_falling = player_is_falling
        self.player_position = player_position

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self, player_rect, volume_level):
        if volume_level > 10 and microphone_switch:
            self.player_is_falling = False

            next_x = player_speed
            player_rect[0] = player_rect[0] + next_x
            for elem in sorted(collision_walls):
                if player_rect.colliderect(elem):
                    next_x = 0

            self.player_position[0] += next_x
            self.world_pos_x += next_x

            self.player_position[1] = self.player_position[1] - player_speed
        else:
            self.player_is_falling = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:  # вкл/вкл карту
                    if self.microphone_switch:
                        self.microphone_switch = False
                    else:
                        self.microphone_switch = True
