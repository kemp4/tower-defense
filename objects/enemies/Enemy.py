import os

import pygame
from pygame.math import Vector2
from pygame.rect import Rect

from GameCommon import GameCommon
from settings.Settings import CELL_SIZE


class Enemy(pygame.sprite.Sprite):
    destinationIndex = 0
    destinationPosition = Vector2()
    position = Vector2()
    hp = 100
    # color = (111, 0, 16)
    __gameCommon = GameCommon()
    speed = 0.05
    # surface = pygame.Surface()

    def __init__(self, *groups):
        super().__init__(*groups)
        self.position = Vector2(self.__gameCommon.route[0])
        self.destinationPosition = Vector2(self.position)
        self.image = pygame.transform.rotate(self.__gameCommon.images_dict['tank'], 0)

    def __update_rect(self):
        self.rect = pygame.Rect(self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0],
                                CELL_SIZE[1])

    def __find_new_destination_position(self):
        self.destinationIndex += 1
        if self.destinationIndex >= len(self.__gameCommon.route):
            self.__gameCommon.lifes -= 1
            # print(self.__gameCommon.lifes)
            self.kill()
        else:
            self.destinationPosition = self.__gameCommon.route[self.destinationIndex]
            angle = Vector2(-1, 0).angle_to(self.destinationPosition-self.position)
            # print(angle)
            self.image = pygame.transform.rotate(self.__gameCommon.images_dict['tank'], -angle)

    def get_rect(self):
        return self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]

    def __get_dist_to_destination_position(self):
        return self.position.distance_to(self.destinationPosition)

    def update(self):
        distance = self.__get_dist_to_destination_position()
        if distance < 0.03:
            self.__find_new_destination_position()
        diff = self.destinationPosition - self.position
        diff = diff.normalize() * self.speed
        self.position += diff
        self.__update_rect()

    def __str__(self):
        return self.__class__.__name__ + 'pos :' + str(self.position)

    def hit(self, bullet):
        self.hp -= bullet.damage
        print(self.hp)
        if self.hp <= 0:
            self.kill()
