import traceback

import pygame
import sys

from config import HEIGHT, WIDTH, FPS
from debug import Debug
from level import Level


class Main:
    def __init__(self):

        # general setup
        pygame.init()
        pygame.display.set_caption('My Zelda')

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.level = Level(self.screen)
        self.dt = 1.0

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('white')
            self.level.render(self.dt)
            self.level.update()
            # Debug.d(self.dt)

            pygame.display.update()
            self.dt = self.clock.tick(FPS) / 1000


if __name__ == '__main__':
    game = Main()
    try:
        game.run()
    except Exception as e:
        traceback.print_exc()
        input()
