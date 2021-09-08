import pygame
from pygame.locals import KEYDOWN, K_ESCAPE, K_q
import sys

'''Check for events that will exit the pygame system'''


def exit_pygame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q:
                sys.exit(0)
