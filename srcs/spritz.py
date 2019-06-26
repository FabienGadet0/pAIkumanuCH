import pygame
from pygame.locals import *


class Spritz(pygame.sprite.Sprite):
    def __init__(self, pos, direction, genre):
        super().__init__()
        self.sprite_pos = pos
        self.direction = direction[0]
        self.genre = genre[0]
        self.animation = "1"
        file = "sprites/" + self.genre + self.direction + self.animation + ".png"
        self.image = pygame.image.load(file).convert()
        self.image.set_colorkey(pygame.Color(0, 0, 0))

    def set_sprite_pos(self, pos):
        self.sprite_pos = pos

    def set_direction(self, direction):
        self.direction = direction[0]

    def update_animation():
        if self.animation == "1":
            self.animation = "2"
        if self.animation == "2":
            self.animation = "1"
        self._assume_gender()

    def get_image():
        return self.image

    def _assume_gender(self):
        file = "sprites/" + self.genre + self.direction + self.animation + ".png"
        self.image = pygame.image.load(file).convert()

        # Set our transparent color
        self.image.set_colorkey(BLACK)
