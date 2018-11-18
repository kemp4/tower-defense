import pygame

from objects.bullets.Rocket import Rocket
from objects.towers.Tower import Tower


class RocketLauncher(Tower):
    cost = 50
    range = 5
    load_speed = 5

    def create_new_bullet(self, target):
        return Rocket(target, self)

    def get_rotated_image(self):
        return pygame.transform.rotate(self.gameCommon.images_dict['rocket_launcher'], -self.angle + 90)