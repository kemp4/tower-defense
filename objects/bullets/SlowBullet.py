import pygame

from objects.bullets.Bullet import Bullet


class SlowBullet(Bullet):
    speed = 0.12
    damage = 0

    def get_rotated_image(self, angle):
        return pygame.transform.rotate(self.gameCommon.images_dict['slow_bullet'], -angle + 90)

    def explode(self):
        # self.target_enemy.slow(self.parent_tower.slow_time, self.parent_tower.slow_value)
        self.target_enemy.slow(0.2, 0.5)

