import pygame
from pygame.math import Vector2

from GameCommon import GameCommon
from objects.bullets.Bullet import Bullet
from settings.Settings import CELL_SIZE, MAX_LOAD_PROGRESS


class Tower(pygame.sprite.Sprite):
    # color = (111, 0, 16)
    __gameCommon = GameCommon()
    position = Vector2()
    range = 2.5
    load_progress = MAX_LOAD_PROGRESS
    load_speed = 1
    disabled = False
    cost = 20

    def __init__(self, position, disabled=False, *groups):
        super().__init__(*groups)
        self.disabled = disabled
        self.position = position
        self.image = self.__gameCommon.images_dict['canon']
        self.__update_rect()

    def __update_rect(self):
        self.rect = pygame.Rect(self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0],
                                CELL_SIZE[1])

    def get_rect(self):
        return self.position[0] * CELL_SIZE[0], self.position[1] * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]

    def update(self):
        self.__update_rect()
        if self.disabled:
            return
        enemies_in_range = self.__find_targets_in_range()
        self.load_progress = MAX_LOAD_PROGRESS if self.load_progress >= MAX_LOAD_PROGRESS else self.load_progress + self.load_speed

        if len(enemies_in_range) > 0:
            nearest_enemy = self.__find_nearest_enemy(enemies_in_range)
            self.aim(nearest_enemy)
            if self.load_progress == MAX_LOAD_PROGRESS:
                self.load_progress = 0
                self.shoot(nearest_enemy)

    def __find_targets_in_range(self):
        enemies_in_range = []
        enemies = self.__gameCommon.enemies_list
        if enemies != 0:
            for enemy in enemies:
                if self.position.distance_to(enemy.position) < self.range:
                    enemies_in_range.append(enemy)
        return enemies_in_range

    def aim(self, nearest_enemy):
        angle = Vector2(-1, 0).angle_to(nearest_enemy.position - self.position)
        image = pygame.transform.rotate(self.__gameCommon.images_dict['canon'], -angle + 90)
        self.image = pygame.transform.scale(image, (70, 70))

    def __find_nearest_enemy(self, enemies_in_range):
        nearest_enemy = enemies_in_range[0]
        for enemy in enemies_in_range:
            if self.position.distance_to(enemy.position) < self.position.distance_to(nearest_enemy.position):
                nearest_enemy = enemy
        return nearest_enemy

    def shoot(self, nearest_enemy):
        new_bullet = Bullet(nearest_enemy, self)
        self.__gameCommon.bullets_list.add_internal(new_bullet)
        new_bullet.add(self.__gameCommon.bullets_list)