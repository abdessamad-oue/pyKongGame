import pygame

from src.Game import Game
from src.Config import Config

def main():
    pygame.init()
    screen = pygame.display.set_mode((
        Config['game']['width'],
        Config['game']['height'],
    ))
    pygame.display.set_caption(Config['game']['caption'])

    game = Game(screen)
    game.loop()

if __name__ == '__main__':
    main()


