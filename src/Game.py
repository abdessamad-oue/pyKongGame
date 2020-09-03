import os, sys
import pygame
from src.Config import Config
from src.Kong import Kong

main_dir = os.path.split(os.path.abspath(__file__))[0]

RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'


class dummysound:
    def play(self):
        pass

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0

    def load_sound(self, file):
        filepath = os.path.join(main_dir, '..', 'sounds', file)
        try:
            sound = pygame.mixer.Sound(filepath)
            return sound
        except pygame.error:
            print('Warning, unable to load, %s' % file)
        return dummysound()

    def loop(self):
        clock = pygame.time.Clock()

        pygame.init()
        if pygame.mixer and not pygame.mixer.get_init():
            print('Warning, no sound')
            pygame.mixer = None

        pos_x = (Config['game']['width'] - 30) / 2
        pos_y = (Config['game']['height'] - 30) / 2

        tile = Config['kong'][LEFT]
        speed = Config['kong']['speed']

        # kong_surface = pygame.image.load(tile)
        # kong_rect = kong_surface.get_rect().move(pos_x, pos_y)

        background_image = pygame.image.load(Config['game']['background']).convert()

        direction = RIGHT
        kong = Kong(self.screen, pos_x, pos_y)
        kong.draw()
        ksurface, krect = kong.draw(direction)

        while True:
            self.screen.blit(background_image, [0, 0])
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN:

                    sound = self.load_sound('smb_kick.wav')
                    # catch event to move kong                     
                    if event.key == pygame.K_LEFT:
                        pos_x = pos_x - speed
                        direction = LEFT
                    elif event.key == pygame.K_RIGHT:
                        pos_x = pos_x + speed
                        direction = RIGHT
                    elif event.key == pygame.K_UP:
                        pos_y = pos_y - speed
                        direction = UP
                    elif event.key == pygame.K_DOWN:
                        pos_y = pos_y + speed
                        direction = DOWN

                    # collision with the wall
                    if pos_x >= Config['game']['width'] - 20:
                        pos_x = pos_x - speed
                        sound = self.load_sound('smb_bump.wav')

                    if pos_x < 0:
                        pos_x = 0
                        sound = self.load_sound('smb_bump.wav')

                    if pos_y >= Config['game']['height'] - 20:
                        pos_y = pos_y - speed
                        sound = self.load_sound('smb_bump.wav')

                    if pos_y < 0:
                        pos_y = 0
                        sound = self.load_sound('smb_bump.wav')

                    sound.play()
                    kong = Kong(self.screen, pos_x, pos_y)
                    ksurface, krect = kong.draw(direction)

            self.screen.blit(ksurface, krect)
            # self.screen.blit(kong_surface, kong_rect)

            pygame.display.flip()
            clock.tick(Config['game']['fps'])

        # if pygame.mixer:
        #     pygame.mixer.music.fadeout(1000)
