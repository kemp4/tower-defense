import pygame

from GameCommon import GameCommon
from objects.enemies.Enemy import Enemy


class WaveManager:
    NEW_ENEMY_EVENT = pygame.USEREVENT + 1
    __gameCommon = GameCommon()
    enemies_wave_left = 0
    wave_num = 0

    def update(self):
        if len(self.__gameCommon.enemies_list) == 0 and self.enemies_wave_left <= 0:
            self.start_new_wave()
        if pygame.event.get(self.NEW_ENEMY_EVENT):
            self.spawn_new_enemy()
        if self.enemies_wave_left <=0:
            pygame.time.set_timer(self.NEW_ENEMY_EVENT, 0)

    def start_new_wave(self):
        self.wave_num += 1
        self.enemies_wave_left = 5*(self.wave_num/2)
        print(self.enemies_wave_left)
        pygame.time.set_timer(self.NEW_ENEMY_EVENT, 250)

    def spawn_new_enemy(self):
        newEnemy = Enemy((self.wave_num/4)*100)
        newEnemy.add(self.__gameCommon.enemies_list)
        self.__gameCommon.enemies_list.add_internal(newEnemy)
        self.enemies_wave_left -= 1
        # print (newEnemy.hp)
