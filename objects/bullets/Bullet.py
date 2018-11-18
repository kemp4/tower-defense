import os

import pygame
from pygame.math import Vector2

from GameCommon import GameCommon
from settings.Settings import CELL_SIZE


class Bullet(pygame.sprite.Sprite):
    position = Vector2()
    __gameCommon = GameCommon()
    speed = 0.09
    target_enemy = None
    parent_tower = None
    damage = 50

    def __init__(self, target_enemy, parent_tower, *groups):
        super().__init__(*groups)
        self.target_enemy = target_enemy
        self.parent_tower = parent_tower
        self.position = Vector2(self.parent_tower.position)
        self.image = pygame.transform.rotate(self.__gameCommon.images_dict['bullet'], 0)

    def __update_rect(self):
        self.rect = pygame.Rect(self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0],
                                CELL_SIZE[1])

    def get_rect(self):
        return self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]

    def __get_dist_to_destination_position(self):
        return self.position.distance_to(self.target_enemy.position)

    def update(self):
        distance = self.__get_dist_to_destination_position()
        if distance < self.speed:
            self.target_enemy.hit(self)
            self.kill()
        else:
            diff = self.target_enemy.position - self.position
            diff = diff.normalize() * self.speed
            self.position += diff
            self.__update_rect()

