import os

import pygame
from pygame.math import Vector2
from pygame.sprite import Group

from AssetsReader import AssetsReader
from GameCommon import GameCommon
from MapReader import MapReader
from TowersManager import TowersManager
from WaveManager import WaveManager
from objects.towers.Tower import Tower
from settings.Settings import WINDOW_SIZE, LEFT_BUTTON, RIGHT_BUTTON

pygame.init()
pygame.font.init()
pygame.display.set_caption("Tower defence")
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.SRCALPHA)

gameCommon = GameCommon()
gameCommon.route = MapReader().get_route()

AssetsReader()
towersManager = TowersManager()
# towersManager.create_new_tower()

map_elements_list = MapReader().get_map_elements()

pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

waveManager = WaveManager()

all_sprites_list = Group(map_elements_list)
all_sprites_list.add(gameCommon.enemies_list)
all_sprites_list.add(gameCommon.towers_list)

# myfont = pygame.font.SysFont(pygame.font.get_default_font(), 30)
# textsurface = myfont.render('Press any kay or click mouse to start', False, (0, 0, 0))

done = False
while not done:
    waveManager.update()
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_BUTTON:
            towersManager.create_new_tower()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT_BUTTON:
            towersManager.cancel_build()
            # if event.type == pygame.MOUSEMOTION:
            # print('mouse at (%d, %d)' % event.pos)

    # for sprite in all_sprites_list:
    #     sprite.update()

    for sprite in map_elements_list:
        if sprite.rect.collidepoint(mouse_position):
            sprite.set_highlighted()
            for temp in gameCommon.temp_group:
                temp.position = Vector2(sprite.position)
        else:
            sprite.clear_highlighted()

    # towersManager.update()

    gameCommon.enemies_list.update()
    gameCommon.towers_list.update()
    gameCommon.bullets_list.update()
    gameCommon.temp_group.update()
    map_elements_list.draw(screen)
    gameCommon.enemies_list.draw(screen)
    gameCommon.bullets_list.draw(screen)
    gameCommon.towers_list.draw(screen)
    gameCommon.temp_group.draw(screen)

    # screen.blit(textsurface, (0, 0))
    screen.blit(gameCommon.images_dict['mouse'], mouse_position)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
