import threading
import sounddevice as sd
import numpy as np

from keyboard import Keyboard
from render import Render
from config import *

import time


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

pygame.init()

keyboard = Keyboard()
render = Render(screen, keyboard)

running = True
while running:
    render.walls_rendering()
    render.player_rendering()
    keyboard.movement(render.player_rect, volume_level)

    pygame.display.flip()
    clock.tick(20)
