import os

import pygame
from pygame.math import Vector2

from GameCommon import GameCommon
from settings.Settings import CELL_SIZE


class Bullet(pygame.sprite.Sprite):
    position = Vector2()
    gameCommon = GameCommon()
    speed = 0.18
    target_enemy = None
    parent_tower = None
    damage = 20

    def __init__(self, target_enemy, parent_tower, *groups):
        super().__init__(*groups)
        self.target_enemy = target_enemy
        self.parent_tower = parent_tower
        self.position = Vector2(self.parent_tower.position)
        self.image = self.get_rotated_image(0)

    def __update_rect(self):
        self.rect = pygame.Rect(self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0],
                                CELL_SIZE[1])

    def get_rect(self):
        return self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]

    def __get_dist_to_destination_position(self):
        return self.position.distance_to(self.target_enemy.position)

    def get_rotated_image(self, angle):
        return pygame.transform.rotate(self.gameCommon.images_dict['bullet'], -angle + 90)

    def aim(self):
        angle = Vector2(-1, 0).angle_to(self.target_enemy.position - self.position)
        image = self.get_rotated_image(angle)
        self.image = image  # pygame.transform.scale(image, CELL_SIZE)

    def update(self):
        distance = self.__get_dist_to_destination_position()
        self.aim()
        if self.out_of_range():
            self.forfeit()
        if distance < self.speed:
            self.explode()
            self.kill()
        else:
            diff = self.target_enemy.position - self.position
            diff = diff.normalize() * self.speed
            self.position += diff
            self.__update_rect()

    def explode(self):
        self.target_enemy.hit(self)

    def out_of_range(self):
        return self.parent_tower.position.distance_to(self.position) > self.parent_tower.range

    def forfeit(self):
        self.kill()
