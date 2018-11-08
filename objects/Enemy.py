import os

import pygame

from settings.Settings import CELL_SIZE


class Enemy(pygame.sprite.Sprite):
    position = (4, 1)

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.image = image = pygame.image.load(os.path.join('assets', 'enemies', 'path823.png')).convert_alpha()
        self.rect = pygame.Rect(self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0],
                                CELL_SIZE[1])


    def getDataForDraw(self):
        print("enemy")
