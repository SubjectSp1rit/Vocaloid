import pygame
from config import *


class KeyboardControl:
    def __init__(self):
        self.rect = pygame.Rect(*player_position, 30, 40)
        self.x, self.y = player_position

    @property
    def take_position(self):
        return (self.x, self.y)

    def detect_collision(self, next_x, next_y):
        next_rect = self.rect.copy()
        next_rect.move_ip(next_x, next_y)
        hits = next_rect.collidelistall(collision_walls)
        if len(hits):
            pass
        self.x += next_x
        self.y += next_y

    def keyboard_buttons(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        elif keys[pygame.K_d]:
            next_x = player_speed
            self.detect_collision(next_x, 0)
        elif keys[pygame.K_s]:
            next_y = player_speed
            self.detect_collision(0, next_y)
        elif keys[pygame.K_a]:
            next_x = -player_speed
            self.detect_collision(next_x, 0)
        elif keys[pygame.K_w]:
            next_y = -player_speed
            self.detect_collision(0, next_y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        self.rect.center = self.x, self.y
