import sys

import pygame


# zarzadzanie, sposob dzialania gry
# run_game petla glowna gry
class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Gra")

        def run_game(self):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    pygame.display.flip()
