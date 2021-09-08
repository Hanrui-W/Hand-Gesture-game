import pygame
from pygame.sprite import Sprite

'''Representation of a single bullet'''


# class child_class(parent_class)
class Bullet(Sprite):

    # limit the maximum amount of bullets that one can have on screen
    max_cartridge = 3

    def __init__(self, screen, yawn):

        # Call the super class constructor
        super().__init__()
        self.screen = screen

        # Build a rect, tore rectangular coordinates (x_pos, y_pos, width, height)
        self.rect = pygame.Rect(0, 0, 3, 5)

        # Center rect at ship center
        self.rect.centerx = yawn.rect.centerx

        # Center rect at ship's top
        self.rect.top = yawn.rect.top

        self.y = float(self.rect.y)

        self.color1 = (60, 60, 60)
        self.speed_factor = 10

    # Move bullet up the screen (override method in parent class Sprite)
    def update(self):
        # Move bullet up
        self.y -= self.speed_factor

        # update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw the bullet to the screen: Draws a rectangle at specified positions with specific colors
        pygame.draw.rect(self.screen, self.color1, self.rect)
