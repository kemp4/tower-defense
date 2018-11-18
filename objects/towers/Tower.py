import pygame
from pygame.math import Vector2
from pygame.sprite import Sprite

from GameCommon import GameCommon
from objects.bullets.Bullet import Bullet
from objects.towers.Range import Range
from settings.Settings import CELL_SIZE, MAX_LOAD_PROGRESS


class Tower(pygame.sprite.Sprite):
    gameCommon = GameCommon()
    position = Vector2()
    range = None
    load_progress = MAX_LOAD_PROGRESS
    load_speed = None
    disabled = False
    cost = None
    angle = 0
    image = None

    def __init__(self, position, disabled=False, *groups):
        super().__init__(*groups)
        self.disabled = disabled
        self.position = position
        self.update_image()
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
        enemies = self.gameCommon.enemies_list
        if enemies != 0:
            for enemy in enemies:
                if self.position.distance_to(enemy.position) < self.range:
                    enemies_in_range.append(enemy)
        return enemies_in_range

    # to override
    def get_rotated_image(self,):
        return pygame.transform.rotate(self.gameCommon.images_dict['canon'], -self.angle + 90)

    def aim(self, nearest_enemy):
        self.angle = Vector2(-1, 0).angle_to(nearest_enemy.position - self.position)
        self.update_image()

    def __find_nearest_enemy(self, enemies_in_range):
        nearest_enemy = enemies_in_range[0]
        for enemy in enemies_in_range:
            if self.position.distance_to(enemy.position) < self.position.distance_to(nearest_enemy.position):
                nearest_enemy = enemy
        return nearest_enemy

    def create_new_bullet(self, target):
        return Bullet(target, self)

    def shoot(self, nearest_enemy):
        new_bullet = self.create_new_bullet(nearest_enemy)
        self.gameCommon.bullets_list.add_internal(new_bullet)
        new_bullet.add(self.gameCommon.bullets_list)

    def set_highlighted(self):
        Range(self)
        # display range

        # wal
    def is_free(self):
        return False

    def clear_highlighted(self):
        pass

        # if self.range_view is not None:
        #     self.range_view.kill()
        #     self.range_view = None
        # display range

        # def get_center(self):
        #     return Vector2(self.position-Vector2(0.5*self.range, 0.5*self.range))

    def update_image(self):
        image = self.get_rotated_image()
        self.image = pygame.transform.scale(image, CELL_SIZE)

