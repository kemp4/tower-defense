import os

import pygame
from pygame.math import Vector2
from pygame.rect import Rect

from GameCommon import GameCommon
from settings.Settings import CELL_SIZE

# HEALTH_SURF = pygame.Surface((CELL_SIZE[0], CELL_SIZE[1]/10))
# HEALTH_SURF.set_colorkey((0, 0, 128))
# HEALTH_SURF.set_alpha(200)
# pygame.draw.rect(HEALTH_SURF, (255, 255, 255), (0, 0, CELL_SIZE[0], CELL_SIZE[1]/10), 1)
# pygame.draw.rect(HEALTH_SURF, (255, 0, 0), (2, 2, (CELL_SIZE[0]-4), CELL_SIZE[1]/10-4), 2)


class HealthBar(pygame.sprite.Sprite):
    parent_enemy = None
    position = None

    def __init__(self, parent_enemy, *groups):
        super().__init__(*groups)
        self.parent_enemy = parent_enemy
        self.update_health()

    def __update_rect(self):
        self.rect = pygame.Rect(self.parent_enemy.position[0] * CELL_SIZE[0],
                                self.parent_enemy.position[1] * CELL_SIZE[1],
                                CELL_SIZE[0], CELL_SIZE[1]/10)

    def update_health(self):
        HEALTH_SURF = pygame.Surface((CELL_SIZE[0], CELL_SIZE[1] / 10))
        HEALTH_SURF.set_colorkey((0, 0, 128))
        HEALTH_SURF.set_alpha(200)
        pygame.draw.rect(HEALTH_SURF, (255, 255, 255), (0, 0, CELL_SIZE[0], CELL_SIZE[1] / 10), 1)
        health_factor = self.parent_enemy.hp/self.parent_enemy.max_hp
        pygame.draw.rect(HEALTH_SURF, (255, 0, 0), (2, 2, (CELL_SIZE[0]-4)*health_factor, CELL_SIZE[1] / 10 - 4), 2)
        self.image = HEALTH_SURF

    def get_rect(self):
        return self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]

    def update(self):
        self.__update_rect()
