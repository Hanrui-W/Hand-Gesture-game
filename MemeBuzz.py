import pygame
from pygame.sprite import Sprite

'''Class for meme Buzz'''


class Buzz(Sprite):

    # Some static variables regarding image dimensions
    used_image = pygame.image.load("images/buzz.jpg")
    image_x, image_y = used_image.get_rect().size

    def __init__(self, screen, scale):
        super(Buzz, self).__init__()
        self.screen = screen
        self.scale = scale

        # Set up a hit counter for each buzz
        self.hit_counter = 0

        # Load image
        self.image = pygame.image.load("images/buzz.jpg")

        # Get dimensions of the image
        (self.x_dim, self.y_dim) = self.image.get_rect().size

        # Change scale of image
        self.image = pygame.transform.scale(self.image, (int(self.x_dim / scale), int(self.y_dim / scale)))

        # Get rect attributes
        self.rect = self.image.get_rect()

        # Set image pos: near left, and above screen
        self.rect.x = self.rect.width
        self.rect.y = self.screen.get_rect().top - self.rect.height

    def paste_on_screen(self):
        # Draw image on screen
        self.screen.blit(self.image, self.rect)

    # Draw buzz at a specific x-coordinate
    def set_position(self, x_coord):
        self.rect.x = x_coord

    def update(self):
        # Continuously move down
        self.rect.top += 2

    def move_left(self):
        # move left a designated unit
        self.rect.left -= 2

    def move_right(self):
        # move right a designated unit
        self.rect.right += 2

    # get the x coord of image
    def get_x_pos(self):
        # Store image's x-coordinate position
        x = float(self.rect.x)
        return x

    # get the y coord of image
    def get_y_pos(self):
        y = float(self.rect.y)
        return y

    # increment the hit counter
    def increment_counter(self, debug=False):
        self.hit_counter += 1

        if debug:
            print(self.hit_counter)

    # Delete image if enough hits
    def delete_image(self, threshold=25, debug=False):
        if self.hit_counter >= threshold:
            if debug:
                print("Function call")
            return True
