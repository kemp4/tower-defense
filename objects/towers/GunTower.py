import pygame

from objects.bullets.Bullet import Bullet
from objects.bullets.SlowBullet import SlowBullet
from objects.towers.Tower import Tower


class GunTower(Tower):
    cost = 20
    range = 3
    load_speed = 10

    def create_new_bullet(self, target):
        return Bullet(target, self)

    def get_rotated_image(self):
        return pygame.transform.rotate(self.gameCommon.images_dict['canon'], -self.angle + 90)
