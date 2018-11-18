import pygame

from objects.bullets.SlowBullet import SlowBullet
from objects.towers.Tower import Tower


class SlowTower(Tower):
    cost = 35
    range = 4
    load_speed = 15

    def create_new_bullet(self, target):
        return SlowBullet(target, self)

    def get_rotated_image(self):
        return pygame.transform.rotate(self.gameCommon.images_dict['slow_tower'], -self.angle + 90)
