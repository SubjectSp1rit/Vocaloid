import pygame
import sounddevice as sd
import numpy as np
import asyncio
import sys
import threading

from keyboard import KeyboardControl
from config import *


class Audio:
    @staticmethod
    def audio_callback(indata, frames, time, status):
        volume = np.linalg.norm(indata) * 6
        global volume_level
        volume_level = int(volume)

    @staticmethod
    def listen():
        with sd.InputStream(callback=Audio.audio_callback):
            sd.sleep(1000000000)


x = threading.Thread(target=Audio.listen, daemon=True)
x.start()

keyboard = KeyboardControl()

pygame.init()

running = True
while running:

    player_rect = player.get_rect(topleft=player_position)

    if volume_level > 10 and microphone_switch:
        player_is_falling = False

        next_x = player_speed
        player_rect[0] = player_rect[0] + next_x
        for elem in sorted(collision_walls):
            if player_rect.colliderect(elem):
                next_x = 0
        player_position[0] += next_x
        world_pos_x += next_x

        player_position[1] = player_position[1] - player_speed
    else:
        player_is_falling = True

    player_falling_rect = player.get_rect(topleft=player_position)
    player_falling_rect[1] = player_falling_rect[1] + player_speed
    flag_falling = True
    for elem in sorted(collision_walls):
        if player_falling_rect.colliderect(elem):
            flag_falling = False
    if flag_falling and player_is_falling:
        player_position[1] = player_position[1] + player_speed
        flag_falling = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:  # вкл/вкл карту
                if microphone_switch:
                    microphone_switch = False
                else:
                    microphone_switch = True

    screen.fill('white')
    screen.blit(player, (player_static_position_x, player_position[1]))
    for elem in sorted(collision_walls):
        pygame.draw.rect(screen, ('black'), (elem[0] - world_pos_x, elem[1], elem[2], elem[3]))

    pygame.display.flip()
    clock.tick(20)
