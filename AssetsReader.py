import os

import pygame

from GameCommon import GameCommon


class AssetsReader:
    gameCommon = GameCommon()

    def __init__(self):
        self.read_images()

    def read_images(self):
        tankImage = pygame.image.load(os.path.join('assets', 'enemies', 'Tank.png')).convert_alpha()
        canonImage = pygame.image.load(os.path.join('assets', 'towers', 'canon.png')).convert_alpha()
        rocketLauncherImage = pygame.image.load(os.path.join('assets', 'towers', 'rocket_launcher.png')).convert_alpha()
        slowTowerImage = pygame.image.load(os.path.join('assets', 'towers', 'slow_tower.png')).convert_alpha()
        mouseImage = pygame.image.load(os.path.join('assets', 'gui', 'mouse.png')).convert_alpha()
        bulletImage = pygame.image.load(os.path.join('assets', 'bullets', 'bullet.png')).convert_alpha()
        rocketImage = pygame.image.load(os.path.join('assets', 'bullets', 'rocket.png')).convert_alpha()
        slowBulletImage = pygame.image.load(os.path.join('assets', 'bullets', 'slow_bullet.png')).convert_alpha()
        heartImage = pygame.image.load(os.path.join('assets', 'gui', 'heart.png')).convert_alpha()
        cashImage = pygame.image.load(os.path.join('assets', 'gui', 'cash.png')).convert_alpha()

        self.gameCommon.images_dict.update({'tank': tankImage})
        self.gameCommon.images_dict.update({'mouse': mouseImage})
        self.gameCommon.images_dict.update({'canon': canonImage})
        self.gameCommon.images_dict.update({'rocket_launcher': rocketLauncherImage})
        self.gameCommon.images_dict.update({'slow_tower': slowTowerImage})
        self.gameCommon.images_dict.update({'bullet': bulletImage})
        self.gameCommon.images_dict.update({'rocket': rocketImage})
        self.gameCommon.images_dict.update({'slow_bullet': slowBulletImage})
        self.gameCommon.images_dict.update({'heart': heartImage})
        self.gameCommon.images_dict.update({'cash': cashImage})

