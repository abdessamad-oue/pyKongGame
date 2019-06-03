import pygame
from src.Config import Config

class Kong:

    def __init__(self, screen, x, y):
        self.pos_x = x
        self.pos_y = y
        self.screen = screen

    def draw(self, direction='right'):

        tile = Config['kong'][direction]

        kong_surface = pygame.image.load(tile)
        kong_rect = kong_surface.get_rect().move(self.pos_x, self.pos_y)

        return kong_surface, kong_rect


    def move(self, x, y):
        self.pos_x = x
        self.pos_y = y
        print(self.pos_x, self.pos_y)