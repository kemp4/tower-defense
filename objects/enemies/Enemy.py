import os

import pygame
from pygame.math import Vector2
from pygame.rect import Rect

from GameCommon import GameCommon
from objects.enemies.HealthBar import HealthBar
from settings.Settings import CELL_SIZE


class Enemy(pygame.sprite.Sprite):
    destinationIndex = 0
    destinationPosition = Vector2()
    position = Vector2()
    health_bar = None
    # color = (111, 0, 16)
    __gameCommon = GameCommon()
    speed = 0.05
    # surface = pygame.Surface()
    wreck_value = 10

    def __init__(self, max_hp, *groups):
        super().__init__(*groups)
        # self.wreck_value = 10
        self.max_hp = max_hp
        self.hp = max_hp
        self.position = Vector2(self.__gameCommon.route[0])
        self.destinationPosition = Vector2(self.position)
        self.image = pygame.transform.rotate(self.__gameCommon.images_dict['tank'], 0)
        self.health_bar = HealthBar(self)
        self.health_bar.add(self.__gameCommon.gui_list)
        self.__gameCommon.gui_list.add_internal(self.health_bar)


    def __update_rect(self):
        self.rect = pygame.Rect(self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0],
                                CELL_SIZE[1])

    def __find_new_destination_position(self):
        self.destinationIndex += 1
        if self.destinationIndex >= len(self.__gameCommon.route):
            self.__gameCommon.game_variables['lifes'] -= 1
            # print(self.__gameCommon.lifes)
            self.kill()
            self.health_bar.kill()
        else:
            self.destinationPosition = self.__gameCommon.route[self.destinationIndex]
            angle = Vector2(-1, 0).angle_to(self.destinationPosition - self.position)
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
        self.health_bar.update_health()
        # print(self.hp)
        if self.hp <= 0:
            self.kill()
            self.health_bar.kill()
            self.__gameCommon.game_variables['cash'] += self.wreck_value
            self.__gameCommon.game_variables['points'] += self.wreck_value
            self.wreck_value=0
