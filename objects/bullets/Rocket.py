import pygame

from objects.bullets.Bullet import Bullet


class Rocket(Bullet):
    speed = 0.07
    area_of_effect_radius = 2
    damage = 50

    def get_rotated_image(self, angle):
        return pygame.transform.rotate(self.gameCommon.images_dict['rocket'], -angle + 90)

    def explode(self):
        victims = self.__find_targets_in_area_of_effect()
        for victim in victims:
            victim.hit(self)

    def __find_targets_in_area_of_effect(self):
        enemies_in_area = []
        enemies = self.gameCommon.enemies_list
        if enemies != 0:
            for enemy in enemies:
                if self.position.distance_to(enemy.position) < self.area_of_effect_radius:
                    enemies_in_area.append(enemy)
        return enemies_in_area
