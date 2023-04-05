import pygame
from config import *


class Render:
    def __init__(self, sc, keyboard):
        self.player_rect = player.get_rect(topleft=player_position)
        self.screen = sc
        self.keyboard = keyboard

    def player_rendering(self):
        self.screen.blit(player, (player_static_position_x, self.keyboard.player_position[1]))

        player_falling_rect = player.get_rect(topleft=self.keyboard.player_position)
        player_falling_rect[1] = player_falling_rect[1] + player_speed
        flag_falling = True
        for elem in sorted(collision_walls):
            if player_falling_rect.colliderect(elem):
                flag_falling = False
        if flag_falling and self.keyboard.player_is_falling:
            self.keyboard.player_position[1] = self.keyboard.player_position[1] + player_speed
            flag_falling = False

    def walls_rendering(self):
        self.screen.fill('white')
        for elem in sorted(collision_walls):
            pygame.draw.rect(self.screen, ('black'), (elem[0] - self.keyboard.world_pos_x, elem[1], elem[2], elem[3]))
