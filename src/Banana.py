import pygame
import random
from src.Config import Config


class Banana:
    def __init__(self, screen, x, y):
        self.pos_x = x
        self.pos_y = y
        self.screen = screen

    def random_position(self):
        self.pos_x = random.randint(50, 450)
        self.pos_y = random.randint(50, 450)

    def draw(self):

        tile = Config['banana']['tile']

        banana_surface = pygame.transform.scale2x(pygame.image.load(tile))
        banana_rect = banana_surface.get_rect().move(self.pos_x, self.pos_y)

        return banana_surface, banana_rect

    def move(self, x, y):
        self.pos_x = x
        self.pos_y = y
        print(self.pos_x, self.pos_y)
