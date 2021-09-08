import pygame
from Mover import check_move

'''Class for main character'''


class Yawn:
    def __init__(self, screen, scale):
        self.screen = screen
        self.scale = scale

        # Returns surface of the loaded image
        self.image = pygame.image.load("images/big_mouth_dude.jpg")

        # Get dimensions of the image
        (self.x_dim, self.y_dim) = self.image.get_rect().size

        # Change scale of image
        self.image = pygame.transform.scale(self.image, (int(self.x_dim / scale), int(self.y_dim / scale)))

        # Create new rect with size of image and x, y coordinates (0, 0)
        self.rect = self.image.get_rect()

        # Create new rect with size of screen
        self.screen_rect = self.screen.get_rect()

        # Put image at the center and bottom part of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def update(self, cache, current):

        # Note that the bottom of the screen is 480 and the top is 0
        move_right, move_down, move_left, move_up = check_move(cache, current)

        # Check for movements and boundary values
        if move_up and self.rect.top > 0:
            self.rect.centery -= 7
        elif move_down and self.rect.bottom <= self.screen_rect.bottom - 10:
            self.rect.centery += 7

        if move_left and self.rect.left > 0:
            self.rect.centerx -= 7
        elif move_right and self.rect.right <= self.screen_rect.right:
            self.rect.centerx += 7

    def paste_on_screen(self):
        self.screen.blit(self.image, self.rect)
        pass

    # get the x coord of image
    def get_x_pos(self):
        # Store image's x-coordinate position
        x = float(self.rect.x)
        return x

    # get the y coord of image
    def get_y_pos(self):
        y = float(self.rect.y)
        return y
