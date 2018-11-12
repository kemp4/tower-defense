import os

import pygame

from GameCommon import GameCommon


class AssetsReader:
    gameCommon = GameCommon()

    def __init__(self):
        self.read_images()

    def read_images(self):
        tankImage = pygame.image.load(os.path.join('assets', 'enemies', 'Tank.png')).convert_alpha()
        # pygame.transform.scale(tankImage, (70, 70))
        canonImage = pygame.image.load(os.path.join('assets', 'towers', 'canon.png')).convert_alpha()
        # canonImage = pygame.transform.scale(canonImage, (70, 70))
        mouseImage = pygame.image.load(os.path.join('assets', 'gui', 'mouse.png')).convert_alpha()
        bulletImage = pygame.image.load(os.path.join('assets', 'bullets', 'bullet.png')).convert_alpha()

        self.gameCommon.images_dict.update({'tank': tankImage})
        self.gameCommon.images_dict.update({'mouse': mouseImage})
        self.gameCommon.images_dict.update({'canon': canonImage})
        self.gameCommon.images_dict.update({'bullet': bulletImage})
