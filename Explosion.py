import pygame
from pygame.sprite import Sprite

'''Class for explosion effects'''


class ExplosionEffects(Sprite):
    def __init__(self, buzz, screen, scale):
        super(ExplosionEffects, self).__init__()

        self.buzz = buzz
        self.screen = screen
        self.scale = scale
        self.image = pygame.image.load("images/explosion.jpg")

        # Get dimensions of the image
        (self.x_dim, self.y_dim) = self.image.get_rect().size

        # Change scale of image
        self.image = pygame.transform.scale(self.image, (int(self.x_dim / scale), int(self.y_dim / scale)))

        # Get rect attributes
        self.rect = self.image.get_rect()

        # Set image pos: near left, and above screen
        self.rect.x = self.buzz.get_x_pos()
        self.rect.y = self.buzz.get_y_pos()

    def paste_on_screen(self):
        # Draw image on screen
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Continuously move down
        self.rect.top += 2
