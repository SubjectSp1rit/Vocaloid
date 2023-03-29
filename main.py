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
    '''elif keys[pygame.K_d]:
        next_x = player_speed
        player_rect[0] = player_rect[0] + next_x
        for elem in sorted(collision_walls):
            if player_rect.colliderect(elem):
                next_x = 0
        player_position[0] += next_x
    elif keys[pygame.K_s]:
        next_y = player_speed
        player_rect[1] = player_rect[1] + next_y
        for elem in sorted(collision_walls):
            if player_rect.colliderect(elem):
                next_y = 0
        player_position[1] += next_y
    elif keys[pygame.K_a]:
        next_x = player_speed
        player_rect[0] = player_rect[0] - next_x
        for elem in sorted(collision_walls):
            if player_rect.colliderect(elem):
                next_x = 0
        player_position[0] -= next_x
    elif keys[pygame.K_w]:
        next_y = player_speed
        player_rect[1] = player_rect[1] - next_y
        for elem in sorted(collision_walls):
            if player_rect.colliderect(elem):
                next_y = 0
        player_position[1] -= next_y'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:  # вкл/вкл карту
                if microphone_switch:
                    microphone_switch = False
                else:
                    microphone_switch = True

    '''if not player_is_on_fly:
        if keys[pygame.K_SPACE]:
            player_is_on_fly = True
    else:
        if jump_counter >= -8:
            if jump_counter > 0:
                player_position[1] -= (jump_counter ** 2) / 2
            else:
                player_position[1] += (jump_counter ** 2) / 2
            jump_counter -= 1
        else:
            player_is_on_fly = False
            jump_counter = 8'''

    screen.fill('white')
    screen.blit(player, player_position)
    for elem in sorted(collision_walls):
        pygame.draw.rect(screen, ('black'), (elem[0], elem[1], elem[2], elem[3]))

    pygame.display.flip()
    clock.tick(20)
