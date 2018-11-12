import pygame
from pygame.math import Vector2

from GameCommon import GameCommon
from objects.towers.Tower import Tower


class TowersManager:
    __gameCommon = GameCommon()
    temp_tower = None

    def __init__(self):
        self.create_new_temp_tower()

    def create_new_temp_tower(self):
        self.temp_tower = Tower((0, 0), True)
        self.__gameCommon.temp_group.add_internal(self.temp_tower)
        self.temp_tower.add(self.__gameCommon.temp_group)

    def create_new_tower(self):
        # newTower = Tower(self.__position_in_game_cords())
        if self.temp_tower is not None:
            self.temp_tower.disabled = False
            self.temp_tower.kill()
            self.temp_tower.add(self.__gameCommon.towers_list)
            self.__gameCommon.towers_list.add_internal(self.temp_tower)
            self.create_new_temp_tower()

    # def __position_in_game_cords(self):
    #     return Vector2(self.temp_tower.position)

    def cancel_build(self):
        if self.temp_tower is not None:
            self.temp_tower.kill()
            self.temp_tower = None
