import keyboard
import random
import pygame
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
pygame.mixer.init()


def sound(x):
    if x.event_type == 'down':
        resource = 'sound\\'+str(random.randint(1, 6))+'.wav'
        soundwav = pygame.mixer.Sound(resource)
        soundwav.play()


keyboard.hook(sound)
keyboard.wait('ctrl+esc')
