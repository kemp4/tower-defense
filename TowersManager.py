import pygame
from pygame.math import Vector2

from GameCommon import GameCommon
from objects.towers.Tower import Tower


class TowersManager:
    __gameCommon = GameCommon()
    temp_tower = None

    def __init__(self):
        # self.create_new_temp_tower()
        pass

    def create_new_temp_tower(self):
        if self.temp_tower is None:
            self.temp_tower = Tower(Vector2(-1, -1), True)
            self.__gameCommon.temp_group.add_internal(self.temp_tower)
            self.__gameCommon.highlightable.add_internal(self.temp_tower)
            self.temp_tower.add(self.__gameCommon.highlightable, self.__gameCommon.temp_group)

    def create_new_tower(self):
        # newTower = Tower(self.__position_in_game_cords())
        if self.temp_tower is not None:
            if self.__gameCommon.game_variables['cash'] - self.temp_tower.cost < 0:
                return
            free_grass = self.find_free_grass()
            if free_grass is None:
                return
            free_grass.set_tower(self.temp_tower)
            self.temp_tower.disabled = False
            self.temp_tower.kill()
            self.temp_tower.add(self.__gameCommon.towers_list)
            self.__gameCommon.towers_list.add_internal(self.temp_tower)
            self.temp_tower = None
            self.create_new_temp_tower()
            self.__gameCommon.game_variables['cash'] -= self.temp_tower.cost
    # def __position_in_game_cords(self):
    #     return Vector2(self.temp_tower.position)

    def cancel_build(self):
        if self.temp_tower is not None:
            self.temp_tower.kill()
            self.temp_tower = None

    def find_free_grass(self):
        # if len(self.__gameCommon.highlighted)>1:
        #     print('duzoooooo')
        for highlighted in self.__gameCommon.highlighted:
            if highlighted.is_free():
                return highlighted
        return None

